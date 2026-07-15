# DayZ Hashima Islands with Expansion

This repository contains configuration files located in `./config` and `./mpmissions/Expansion.chernarusplus` directories for setting up a DayZ server on the Hashima Islands map with the Expansion mod suite.

## Server Startup Script (start_autoMods.bat)

The `start_autoMods.bat` script handles server startup, automatic mod updates, and restart loops.

### Basic Usage

```batch
.\start_autoMods.bat
```

The script will:
1. Build a mod list from all `@*` directories
2. Optionally update the DayZ Server game files themselves (off by default, see below)
3. Update mods via SteamCMD by default, or sync from a local workshop cache when configured
4. Start the DayZ server
5. Automatically restart when the server exits

### Configuration

Edit the variables at the top of the script:

| Variable | Default | Description |
|----------|---------|-------------|
| `serverName` | `Your-Servername` | Window title for the CMD process |
| `serverPort` | `2302` | Server port |
| `serverConfig` | `serverDZ.cfg` | Server configuration file |
| `serverProfile` | `config` | Profile folder for logs and settings |
| `serverCPU` | `2` | CPU cores to allocate |

### SteamCMD Auto-Updating

The script can automatically update mods on each restart using SteamCMD. Set `USE_STEAMCMD=0` in `.env` to sync from an existing Steam workshop cache instead.

| Variable | Default | Description |
|----------|---------|-------------|
| `STEAMCMD` | `C:\steamcmd\steamcmd.exe` | Path to SteamCMD |
| `UPDATE_ON_RESTART` | `1` | Enable/disable auto-updates (1/0) |
| `USE_STEAMCMD` | `1` | Use SteamCMD (1) or existing workshop cache (0) |
| `WORKSHOP_PATH` | `E:\SteamLibrary\steamapps\workshop\content\221100` | Workshop cache path used when `USE_STEAMCMD=0` |

### DayZ Server Game File Updates

The script can also keep the DayZ Server game files themselves (this folder) up to date, separately from mod updates. Off by default - opt in once you've confirmed it behaves as expected on your machine.

| Variable | Default | Description |
|----------|---------|--------------|
| `ENABLE_SERVER_UPDATE` | `0` | Enable/disable auto-updating the server game files (1/0) |
| `SERVER_APPID` | `223350` | DayZ Server SteamCMD AppID. Anonymous login can return `No subscription` depending on the account - uses the same authenticated `STEAM_LOGIN`/`STEAM_PASS` as mod updates (see Steam Authentication below) |
| `VALIDATE_SERVER_FILES` | `0` | Force SteamCMD to re-hash every server file (slow, ~15GB). Leave off for routine restarts; enable occasionally to repair corruption |
| `SERVER_SOURCE_PATH` | `C:\Program Files (x86)\Steam\steamapps\common\DayZServer` | Local vanilla DayZ Server install to copy from when `USE_STEAMCMD=0` |
| `SERVER_UPDATE_DIRS` | `dta addons battleye keys sakhal` | Folders synced in local-copy mode |
| `SERVER_UPDATE_FILES` | `DayZServer_x64.exe *.dll` | Root files synced in local-copy mode |

How it updates depends on `USE_STEAMCMD`, same as mod updates:

- **`USE_STEAMCMD=1` (default):** runs `steamcmd +force_install_dir <this folder> +login <STEAM_LOGIN> +app_update 223350` (login args must precede `+app_update` but come after `+force_install_dir` - SteamCMD requires that order). Note `force_install_dir` fetches the entire server tool depot, which brings along some SteamCMD/Valve-owned artifacts alongside your files on first run - `steamapps/` (SteamCMD's own install manifests), `_CommonRedist/` (bundled .NET/VC++ redistributable installers), `server_manager/` (Bohemia's companion GUI tool), `steam_appid.txt`, and stock `mpmissions/dayzOffline.*` mission templates (unused - this server loads `main.hashima`). All of these are already covered by `.gitignore`, so they won't show up in `git status`.
- **`USE_STEAMCMD=0`:** useful on a dev machine where a second SteamCMD login would conflict with an active Steam client login. Instead, robocopies only the known vendor game paths (`SERVER_UPDATE_DIRS`/`SERVER_UPDATE_FILES`) from a local vanilla `DayZServer` install that the Steam client keeps updated. This never touches `config/`, `mpmissions/`, mod folders, or `serverDZ.cfg` - only those explicitly whitelisted paths are copied, and nothing is ever deleted from this folder (no mirroring).

### Steam Authentication

Steam credentials are needed whenever `USE_STEAMCMD=1`, for **both** mod updates and server file updates (`ENABLE_SERVER_UPDATE=1`) - anonymous login works for mods but can fail with `No subscription` for the server tool appid depending on the account, so both update paths log in with the same credentials. Provide them via a `.env` file in the project root:

```
USERNAME=your_steam_username
PASSWORD=your_password
```

**Credential Caching:** After the first successful login with Steam Guard, SteamCMD stores a token in `config\config.vdf`. Subsequent logins only need the username - the script detects this automatically and skips the password.

### Skipping Mods from Updates

To exclude specific mods from auto-updating:

| Variable | Example | Description |
|----------|---------|-------------|
| `SKIP_MODS` | `_@Heatmap` | Skip by folder name |
| `SKIP_MOD_IDS` | `2854246756` | Skip by workshop ID |

### Server-Side Mods

Mods prefixed with `_@` are server-side only and not sent to clients. They must be added manually to the `-serverMod=` parameter in the script. Currently configured:

```batch
-serverMod=_@Heatmap;_@SpawnerBubaku
```

## Required Mods

The following mods are required for this project. These are located in directories at the top level of the project and start with the "@" symbol:

- **@Admirals-Parachute-Mod**
- **@Airborne-AI**
- **@CF**
- **@Community-Online-Tools**
- **@DabsFramework**
- **@DayZ-Expansion**
- **@DayZ-Expansion-AI**
- **@DayZ-Expansion-Animations**
- **@DayZ-Expansion-Core**
- **@DayZ-Expansion-Licensed**
- **@DayZ-Expansion-Navigation**
- **@DayZ-Expansion-Vehicles**
- **@DayZ-Expansion-Weapons**
- **@Expansion_Brake_Fix**
- **@HashimaIslands**
- **@HashimaIslandsAssets**
- **@MMG-MightysMilitaryGear**
- **@NoForceWeaponRaise**

## Server-Side Mods

The following are server-side only mods (prefixed with "_@"):

- **_@Heatmap**
- **_@SpawnerBubaku**

Make sure you have these mods installed to ensure full functionality of the server.

## Project Structure

### Custom Scripts

#### `custom_scripts/analyze_quests.py`

This script is used to generate reports for quests defined in the configuration. It processes the quests and outputs details about each quest, including quest ID, title, objectives, quest giver, and rewards.

Several other useful scripts are in that directory, use at your own risk and make sure you understand what they do.  Some will absolutely trash your files if you aren't careful.

### Docs files

The `docs/dayz-expansion` folder contains documentation from the Expansion Wiki. You can reference these docs using your agentic code editor to help speed building out Expansion features.
