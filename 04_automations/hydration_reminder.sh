#!/bin/bash
LOCKFILE=/tmp/hydration_reminder.lock
flock -n "$LOCKFILE" /home/developer/code-conjuring/04_automations/hydration_popup.sh 
