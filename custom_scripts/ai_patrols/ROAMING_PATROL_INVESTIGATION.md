# Roaming/Roaming-Local patrol spawn investigation

## Goal
All 24 `roaming-*` / `roaming-local-*` patrols in `AIPatrolSettings.json` should be spawned
virtually all the time, as long as a player is logged in. In practice, only about half the
roster (roughly 11-13 of 24) has been showing up in any given session.

## Timeline of things tried (didn't fix it)

1. **Per-category load balancing** (`9941856`) — gave roaming patrols their own
   `LoadBalancingCategory` with a higher cap, on the theory the global cap was starving them.
   Re-analysis after a few sessions showed peak concurrent roaming patrols never got anywhere
   close to either the old or new cap (peaked at 12-14), so this wasn't the bottleneck.
2. **Reverted to a single global load-balancing cap** (`3c2b94d`) — simplified back to one
   `Global` category (0-20 players, 60 patrols), since the per-category split wasn't helping and
   might have made things worse.
3. **Raised `RespawnTime` from 5s to 60s** for all roaming patrols (also in `3c2b94d`) — in case
   the very short timer was interfering with the respawn/spawn-trigger cycle. Confirmed via
   `ExpansionAIPatrolBase.c` that the unit is seconds, not minutes.

None of these changed the actual symptom: the same roughly-half of the roster still didn't show
up in the next session's logs.

## What the evidence actually shows

Re-ran `analyze_ai_lifecycle.py` against the session that followed the RespawnTime/load-balancer
change (RPT `DayZServer_x64_2026-07-14_18-43-53.RPT` / `ExpLog_2026-07-14_18-44-19.log`).

- 12 of 24 roaming patrols spawned, in a burst within ~1.4 seconds of the first player logging
  in (41 minutes into the session). The other 12 produced **zero** log output all session — no
  spawn, no error, nothing.
- No clean geometric explanation: distance from the player's login position to patrol waypoint
  did not predict which patrols spawned (a patrol 4.5km away spawned; one 1.1km away didn't;
  MaxDistRadius is 12500 for all of them, larger than the whole map, so distance alone shouldn't
  matter for any of them).
- All 24 roaming patrols share identical `MinDistRadius` (400) / `MaxDistRadius` (12500) /
  `DespawnRadius` (12500) config, so per-patrol config differences don't explain the split.

### Persisted AI save data tells the real story

Expansion persists each patrol's live AI group to
`mpmissions/main.hashima/storage_1/expansion/ai/<sha256(patrol Name)>/` (confirmed the hash
scheme from `ExpansionAIPatrolBase.c::GenerateBaseName()` — it's just `SHA256(Name)`, so folder
hashes were mapped back to patrol names directly).

Checking file mtimes inside each folder against which patrols spawned in the latest session
lines up exactly:

- Every patrol that spawned this session had its save file rewritten at the session-end despawn
  (timestamps match the log to the millisecond).
- Every patrol that *didn't* spawn has a save file that is **weeks old** — the same patrol
  identities, not a different random subset each session.
- One patrol (`roaming-mid-bridge2-nw`) has **no save folder at all** despite spawning and dying
  this session — its group was fully wiped (0 survivors), and `eAIDynamicPatrol::Despawn()` only
  calls `Save()` `if (m_Group.Count())`, i.e. a fully-wiped group's death is never persisted.

The "stale since" dates span a whole month (Jun 20 through Jul 12), a couple of newly-stuck
patrols appearing every few days rather than all at once — see git-history check below.

### Git history check (this did NOT find a smoking-gun commit)

Checked whether a specific config change coincided with patrols going stale:

- The stuck patrols' individual JSON entries are mostly untouched since they were first added
  (`c8bd2d8`, 2026-01-17) — e.g. `roaming-industrial-se-island` has had exactly one commit touch
  it, ever.
- A large rework commit (`07193b5`, 2026-06-21, "work on ai roaming setup") landed close to when
  several patrols first went stale, but it didn't touch those specific patrols' entries, and
  plenty of *other* January-era patrols that weren't touched by it are spawning fine.
- The staleness dates are spread across the whole month rather than clustered right after any
  one commit, which argues against a one-time regression and for an ongoing, recurring failure
  mode — a couple more patrols quietly get stuck every few sessions, and nothing currently gives
  a stuck patrol a second chance once it happens.

## Current best explanation (not fully proven)

Once a patrol's persisted state stops updating (most likely via the "fully wiped group never
gets saved" path, possibly combined with some other stuck-flag/trigger-not-firing condition we
haven't pinned down in source — the `Trigger` base class itself is compiled into the vanilla
game and wasn't available to inspect), it seems to never get spawned again. Whether this is:

- corrupt/stale save data confusing the load path, or
- the spawn trigger simply never firing again for that patrol regardless of save state,

...is still open. We did not find engine source confirming a specific mechanism (e.g. whether
the spawn trigger requires a player to physically cross into its sphere vs. already being
inside it) — that part was inference, not a verified finding.

## Test in progress

On 2026-07-14, wiped all files under
`mpmissions/main.hashima/storage_1/expansion/ai/` and rebooted the server, forcing every roaming
patrol to fresh-spawn with no persisted state. If the "stuck save data" theory is right, all 24
should start cycling normally again after this. If patrols start going stale again over the
following days/weeks (a few dropping out every session, similar to the Jun 20 - Jul 12 pattern
above), that points more strongly at a trigger/spawn-path bug rather than corrupted save data as
the root cause.

**Next step:** after running for a few days, re-run `analyze_ai_lifecycle.py` and re-check the
`storage_1/expansion/ai/` folder mtimes (same method as above) to see whether the full 24-patrol
roster is cycling, and whether new patrols start going stale again over time.
