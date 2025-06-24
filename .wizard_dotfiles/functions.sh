function winpopup() {
  /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('$1', 'WSL')"
}

pif() {
  local filetype="${1:-py}"            # default to .py
  shift
  local excludes=("$@")                # all remaining args are excluded paths

  local find_cmd=(find . -type f -name "*.${filetype}")

  for ex in "${excludes[@]}"; do
    find_cmd+=(-not -path "./$ex/*")
  done

  "${find_cmd[@]}" -exec sh -c 'for f; do echo "=== $f ==="; cat "$f"; echo ""; done' _ {} +
}

addssh() {
  eval "$(ssh-agent -s)"
  ssh-add /home/developer/.ssh/id_work
}

