#!/usr/bin/env bash
# build_appimage.sh - erstellt ein AppImage
# benoetigt: appimagetool, python3
set -e
APPDIR=AppDir
APP=experimental-agent

# Verzeichnis neu anlegen
rm -rf "$APPDIR" "$APP".AppImage
mkdir -p "$APPDIR/usr/bin"

# Python-Dateien kopieren
cp -r src "$APPDIR/usr/"

# Startskript anlegen
cat > "$APPDIR/AppRun" <<'H'
#!/bin/bash
HERE="$(dirname "$(readlink -f "$0")")"
exec python3 "$HERE/usr/src/main.py"
H
chmod +x "$APPDIR/AppRun"

# Desktop-Datei anlegen
cat > "$APPDIR/$APP.desktop" <<H
[Desktop Entry]
Name=Experimental Agent
Exec=AppRun
Icon=utilities-terminal
Type=Application
Categories=Utility;
H

# AppImage erstellen
appimagetool "$APPDIR" "$APP.AppImage"

printf '\nFertig: %s.AppImage\n' "$APP"

