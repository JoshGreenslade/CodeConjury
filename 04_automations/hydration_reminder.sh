#!/bin/bash
source /home/developer/code-conjuring/.wizard_dotfiles/aliases.sh
source /home/developer/code-conjuring/.wizard_dotfiles/functions.sh

LOCKFILE=/tmp/hydration_reminder.lock

flock -n "$LOCKFILE" winpopup "Take a stretch! Grab a drink! Ponder your life choices up till now!"