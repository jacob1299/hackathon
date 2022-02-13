for filename in *; do echo mv \"$filename\" \"${filename//icons8-/white_}\"; done | /bin/bash
for filename in *; do echo mv \"$filename\" \"${filename//-100/}\"; done | /bin/bash
