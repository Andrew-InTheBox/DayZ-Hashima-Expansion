@echo off
setlocal

::Name for the CMD window
set "serverName=KRONJON-Hashima-PvE"
::Server Port
set "serverPort=2302"
::Server config
set "serverConfig=serverDZ.cfg"
::Server profile folder
set "serverProfile=config"
::Logical CPU cores to use (Equal or less than available)
set "serverCPU=4"

title %serverName% batch

::Build mods list from folders starting with "@"
setlocal enabledelayedexpansion
set "mods="
for /d %%D in (@*) do (
    if not defined mods (
        set "mods=%%~D"
    ) else (
        set "mods=!mods!;%%~D"
    )
)
endlocal & set "mods=%mods%"

echo Server mod list: %mods%

:loop
echo (%time%) Starting %serverName%...

:: /wait = batch pauses until DayZServer_x64.exe exits (graceful shutdown)
start "DayZ Server" /min /wait DayZServer_x64.exe ^
  -config=%serverConfig% ^
  "-mod=%mods%" ^
  "-serverMod=_@Heatmap;_@SpawnerBubaku" ^
  -port=%serverPort% ^
  -profiles=%serverProfile% ^
  -cpuCount=%serverCPU% ^
  -adminlog -netlog -freezecheck

echo (%time%) Server process exited. Restarting in 3 seconds...
timeout /t 3 /nobreak >nul
goto loop
