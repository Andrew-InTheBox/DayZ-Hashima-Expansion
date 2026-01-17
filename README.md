# DayZ Hashima Islands with Expansion

This repository contains configuration files located in `./config` and `./mpmissions/Expansion.chernarusplus` directories for setting up a DayZ server on the Hashima Islands map with the Expansion mod suite.

## Note on Server-Side Mods

The startup batch file `start_automods.bat` automatically loads any directory starting with "@" as a mod. Therefore, server-side mods must be named differently to avoid being loaded in this manner. In this setup, server-side mods are prefixed with "_@". Add your server-side mods manually to the startup batch file following this convention.

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



