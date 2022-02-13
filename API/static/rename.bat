# for filename in *; do echo mv \"$filename\" \"${filename//-animal/}\"; done > result.txt # | /bin/bash
for filename in *; do echo mv \"$filename\" \"${filename//-animal/}\"; done | /bin/bash

# for filename in *; do echo mv \"$filename\" \"${filename//-100/}\"; done | /bin/bash
