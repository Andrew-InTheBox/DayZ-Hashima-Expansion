# Configuration Guide: Bubak Trigger System

In the configuration, you can define **trigger areas**. When a player
enters one, it triggers an action that **spawns infected entities** in
defined areas.

> 💡 *Note:* "**Bubak**" is a Czech word meaning *ghost* or *scary
> creature*.

------------------------------------------------------------------------

## Logging

-   **loglevel** *(0--100)* -- Higher numbers produce more verbose
    logging.

------------------------------------------------------------------------

## Bubak Locations

-   **BubakLocations** -- List of locations.

### Location Parameters

-   **name** -- Name of the location.\
-   **workinghours** -- Defines when this trigger should work (in game
    time).\
-   **triggerdependency** -- List of trigger names this trigger depends
    on (can be empty).

------------------------------------------------------------------------

## Trigger Configuration

-   **triggerpos** -- Position of the trigger.\
-   **triggermins**, **triggermaxs** -- Two points that define a
    **box-shaped** trigger (relative to trigger position).\
-   **triggerradius** -- When non-zero, selects a **sphere-shaped**
    trigger; center is `triggerpos`.\
-   **triggercylradius**, **triggercylheight** -- When non-zero (and
    others are zero), selects a **cylinder-shaped** trigger defined by
    radius and height.\
-   **notification** -- When not empty, shows a notification when the
    trigger is activated (useful for debugging).\
-   **notificationtime** -- Time in seconds that the notification
    remains visible.\
-   **triggerdelay** -- Cooldown time (in seconds) before the trigger
    can activate again.

------------------------------------------------------------------------

## Spawning Configuration

-   **spawnerpos** -- List of positions where spawns occur.\
-   **spawnradius** -- Defines the radius around spawn points to
    slightly randomize positions.\
-   **bubaknum** -- Number of AI or items to be spawned.\
-   **onlyfilltobubaknum** -- For AI only; once this limit is reached,
    no more will spawn.\
-   **itemrandomdmg** -- For items only; spawns items with random damage
    rather than pristine condition.\
-   **bubaci** -- List of AI/items to be spawned.\
-   **bubakinventory** -- List of random loot for spawned creatures.

------------------------------------------------------------------------

### Example Summary

This configuration allows flexible setup of in-game trigger zones that
dynamically spawn entities or items based on location, time, and
conditions. Perfect for custom survival or horror game scenarios.


# Bunker Zed Spawn Points

## Group 1

**Trigger:**\
`730.564, 531.423, 1233.14`

**Spawn Positions:** - `703.695, 531.414, 1226.37` -
`702.152, 531.432, 1185.75` - `648.909, 531.427, 1143.26` -
`603.274, 531.412, 1134.13` - `628.447, 531.408, 1153.23`

------------------------------------------------------------------------

## Group 2

**Trigger:**\
`618.273, 486.339, 1152.61`

**Spawns:** - `626.857, 501.259, 1124.26` -
`627.382, 501.263, 1143.14` - `645.048, 501.252, 1140.23` -
`642.496, 501.252, 1146.27`

------------------------------------------------------------------------

## Group 3

**Trigger:**\
`640.312, 496.413, 1153.69`

**Spawns:** - `640.617, 486.398, 1147.53` -
`650.102, 486.362, 1144.51` - `646.174, 486.362, 1149.12` -
`638.832, 486.39, 1134.88`
