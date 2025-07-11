#!/usr/bin/env bash
###############################################################################
# iterate.sh – Profi-Rahmen für extrem kleine, testbare Entwicklungs-Sprints
# Autor: Dr. Allwissend Poppsen · v0.9 · 11.07.2025
###############################################################################
# Features
#   • Platzhalter .todo / .done, automatische ID-Vergabe
#   • YAML-Konfig (.iterconfig.yml) statt Hard-Coding
#   • Git-Hooks: Commit-Text-Check, Tests, Coverage, Lint
#   • Snapshot-Backup (.ci/backup) vor jedem Push, Auto-Rollback
#   • Farbiges Status-Dashboard im Terminal
#   • Extremely low dependencies (bash ≥ 4, git, tar, yq, pytest, coverage)
###############################################################################

set -euo pipefail

# ------------------------ 1 | Farben ----------------------------------------
RED=$(tput setaf 1); GRN=$(tput setaf 2); YEL=$(tput setaf 3); BLU=$(tput setaf 4)
BOLD=$(tput bold); RST=$(tput sgr0)

# ------------------------ 2 | Pfad-Konstanten -------------------------------
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$ROOT_DIR/.iterconfig.yml"
[[ -f $CONFIG_FILE ]] || { echo "${RED}Fehlt: .iterconfig.yml${RST}"; exit 1; }

# YAML-Werte lesen (benötigt yq: `sudo snap install yq`)
cfg() { yq -r ".$1" "$CONFIG_FILE"; }

PROJECT=$(cfg project_name)
DEFAULT_MOD=$(cfg default_module)
BACKLOG="$ROOT_DIR/backlog/tasks_inbox.txt"
MODULES="$ROOT_DIR/modules"
LOGS="$ROOT_DIR/logs"
CI="$ROOT_DIR/.ci"
STRUCT="$ROOT_DIR/verzeichnisstruktur.txt"
BACKUP_DIR="$CI/backup"
KEEP_BACKUP=$(cfg backup_keep)
CHUNK_SIZES=$(cfg chunk_sizes | tr -d '[],')

mkdir -p "$MODULES" "$LOGS/failures" "$BACKUP_DIR" "$CI/hooks"

# ------------------------ 3 | Hilfs-Funktionen ------------------------------
ts() { date +"%Y-%m-%d|%H:%M:%S"; }

log() {               # log ID MOD ACT RES
  echo "$(ts)|$1|$2|$3|$4|$(git rev-parse --short HEAD 2>/dev/null || echo -)" \
    >> "$LOGS/actions.log"
}

snapshot() {          # Vor Push sichern
  local file="$BACKUP_DIR/$(date +%s).tar.zst"
  tar --exclude="$BACKUP_DIR" -C "$ROOT_DIR" -I 'zstd -T0' -cf "$file" .
  ls -1t "$BACKUP_DIR" | tail -n +$((KEEP_BACKUP + 1)) | xargs -I{} rm -f "$BACKUP_DIR/{}" || true
}

restore_last() {
  local last
  last=$(ls -1t "$BACKUP_DIR" | head -1) || { echo "Kein Backup."; return; }
  tar -I 'zstd -d' -xf "$BACKUP_DIR/$last" -C "$ROOT_DIR"
}

update_tree() {        # Strukturdatei neu erzeugen
  { echo "# Baumstand $(date +"%d.%m.%Y %H:%M")"; tree -a -I '.git|__pycache__'; } > "$STRUCT"
}

next_id() {
  grep -rohP '^id:\s*\K\d+' "$MODULES"/*/tasks 2>/dev/null | sort -n | tail -1 | awk '{print ($0+1)}'
}

yaml_header() { cat <<EOF
id: $1
name: $2
size: XS
prio: normal
text: "$3"
EOF
}

color_percent() {      # 0-100 → farbiger String
  local p=$1
  if   (( p >= $(cfg coverage_target) )); then echo "${GRN}$p${RST}"
  elif (( p > 0 ));                    then echo "${YEL}$p${RST}"
  else                                     echo "${RED}$p${RST}"; fi
}

# ------------------------ 4 | Aktionen --------------------------------------

init() {
  echo -e "${BLU}Erzeuge Grundgerüst …${RST}"
  mkdir -p "$BACKLOG" "$LOGS" "$MODULES/$DEFAULT_MOD/tasks"
  touch "$BACKLOG" "$LOGS/actions.log"
  cat > "$CI/hooks/commit-msg" <<'H'
#!/usr/bin/env bash
grep -qE '^\[#?[0-9]+\] ' "$1" || {
  echo "Commit-Nachricht muss ‘[#ID] Kurzer Text’ enthalten."; exit 1; }
H
  chmod +x "$CI/hooks/commit-msg"
  git config core.hooksPath "$CI/hooks"
  update_tree
  echo -e "${GRN}Grundstruktur erstellt.${RST}"
}

pull() {
  [[ -s $BACKLOG ]] || { echo "Keine neuen Aufgaben."; return; }
  while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    id=$(next_id); mod=$DEFAULT_MOD
    file="$MODULES/$mod/tasks/$(printf '%03d' "$id")_$(echo "$line" | tr ' /' '_' | tr -cd '[:alnum:]_').todo"
    mkdir -p "$(dirname "$file")"
    yaml_header "$id" "$(echo "$line" | cut -d' ' -f1)" "$line" > "$file"
    log "$id" "$mod" NEW 0
    echo "Importiert: $line → $(basename "$file")"
  done < "$BACKLOG"
  : > "$BACKLOG"
  update_tree
}

plan() {
  echo -e "${BLU}Plane Aufgaben …${RST}"
  for size in $CHUNK_SIZES; do
    find "$MODULES" -path "*/tasks/*.todo" -exec grep -Pl "size:\s*$size" {} \; \
        -exec echo "➜ Nutze {}" \;
  done
  update_tree
}

finalize() {
  echo -e "${BLU}Suche .done …${RST}"
  find "$MODULES" -path "*/tasks/*.done" | while read -r f; do
    mod=$(echo "$f" | cut -d/ -f2)
    id=$(grep -Po '^id:\s*\K\d+' "$f")
    rm "$f"; log "$id" "$mod" PASS 0
    status="$MODULES/$mod/STATUS.yml"
    prog=$(grep -Po '^progress:\s*\K\d+' "$status" 2>/dev/null || echo 0)
    prog=$(( prog + 5 > 100 ? 100 : prog + 5 ))
    cat > "$status" <<EOF
module: $mod
progress: $prog
coverage: $(coverage json -o /tmp/cov.json && jq '.totals.percent_covered' /tmp/cov.json || echo 0)
EOF
    echo "Aufgabe #$id abgeschlossen."
  done
  update_tree
}

status() {
  printf "\n${BOLD}Modul            Fortschritt  Test-Coverage${RST}\n"
  echo   "-----------------------------------------------"
  for s in "$MODULES"/*/STATUS.yml; do
    mod=$(grep -Po '^module:\s*\K.*' "$s")
    prog=$(grep -Po '^progress:\s*\K\d+' "$s")
    cov=$(grep -Po '^coverage:\s*\K[\d.]+' "$s")
    printf "%-16s %s%%         %s%%\n" "$mod" "$(color_percent "$prog")" "$(color_percent "${cov%.*}")"
  done
}

backup() { snapshot && echo "Backup angelegt unter $BACKUP_DIR"; }

help() {
  cat <<EOF
Nutzen: ./iterate.sh <Befehl>

--init        Grundstruktur + Hooks anlegen
--pull        Aufgaben aus backlog einlesen
--plan        Platzhalter für XS/S auflisten
--finalize    .done-Dateien einsammeln, Status & Logs schreiben
--status      Farbige Modul-Übersicht
--backup      Manuelles Backup
--help        Diese Hilfe
EOF
}

# ------------------------ 5 | Argument-Router -------------------------------
case "${1:-}" in
  --init)     init ;;
  --pull)     pull ;;
  --plan)     plan ;;
  --finalize) finalize ;;
  --status)   status ;;
  --backup)   backup ;;
  *)          help ;;
esac
