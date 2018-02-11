#!/usr/bin/env python3
# Usage:
#       export tools=path/to/tools
#       python3 diff.py
import os

# Compiles.
command = "g++ asm.cpp"
print(command)
os.system(command)

ss = (
    "add/Add max/Max max/MaxL pong/Pong pong/PongL "
    "rect/Rect rect/RectL").split()
ss = ["../{}".format(x) for x in ss]
ss = [os.path.abspath(x) for x in ss]

for s in ss:
    basename = os.path.basename(s)
    dirname = os.path.dirname(s)

    # Assembles a .asm file.
    command = "$tools/Assembler.sh {}/{}.asm".format(dirname, basename)
    print(command)
    os.system(command)

    # Moves and renames the file. (e.g. foo/Bar.hack -> Bar_cmp.hack)
    command = "mv {0}/{1}.hack {1}_cmp.hack".format(dirname, basename)
    print(command)
    os.system(command)

for s in ss:
    basename = os.path.basename(s)
    dirname = os.path.dirname(s)

    # Assembles a .asm file.
    command = "./a.out {0}/{1}.asm > {1}.hack".format(dirname, basename)
    print(command)
    os.system(command)

for s in ss:
    basename = os.path.basename(s)
    command = "diff -w {0}.hack {0}_cmp.hack".format(basename)
    print(command)
    os.system(command)

# Deletes files.
command = "rm *.hack"
print(command)
os.system(command)

command = "rm a.out"
print(command)
os.system(command)
