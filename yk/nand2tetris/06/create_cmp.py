#!/usr/bin/env python3
# Usage:
#       export tools=path/to/tools
#       python3 create_cmp.py
import os

# Deletes all existing .hack files.
print("rm *.hack")
os.system("rm *.hack")

ss = (
    "add/Add max/Max max/MaxL pong/Pong pong/PongL "
    "rect/Rect rect/RectL").split()

for s in ss:
    dirname, filename = s.split("/")

    # Assembles a .asm file.
    command = "$tools/Assembler.sh {}/{}.asm".format(dirname, filename)
    print(command)
    os.system(command)

    # Moves and renames the file. (e.g. foo/Bar.hack -> Bar_cmp.hack)
    command = "mv {0}/{1}.hack {1}_cmp.hack".format(dirname, filename)
    print(command)
    os.system(command)
