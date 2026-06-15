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
2. Update mods via SteamCMD (if enabled)
3. Start the DayZ server
4. Automatically restart when the server exits

### Configuration

Edit the variables at the top of the script:

| Variable | Default | Description |
|----------|---------|-------------|
| `serverName` | `Your-Servername` | Window title for the CMD process |
| `serverPort` | `2302` | Server port |
| `serverConfig` | `serverDZ.cfg` | Server configuration file |
| `serverProfile` | `config` | Profile folder for logs and settings |
| `serverCPU` | `4` | CPU cores to allocate |

### SteamCMD Auto-Updating

The script can automatically update mods on each restart using SteamCMD.

| Variable | Default | Description |
|----------|---------|-------------|
| `STEAMCMD` | `C:\steamcmd\steamcmd.exe` | Path to SteamCMD |
| `UPDATE_ON_RESTART` | `1` | Enable/disable auto-updates (1/0) |
| `USE_STEAMCMD` | `1` | Use SteamCMD (1) or existing workshop cache (0) |
| `WORKSHOP_PATH` | `E:\SteamLibrary\...` | Fallback workshop path when not using SteamCMD |

### Steam Authentication

For authenticated downloads, credentials can be provided via a `.env` file:

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



