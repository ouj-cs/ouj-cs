#!/usr/bin/env python3
import os

os.system("python3 create_cmp.py")

ss = "Add MaxL RectL PongL".split()

for s in ss:
    command = "./asmL.py {0}.asm > {0}.hack".format(s)
    print(command)
    os.system(command)

for s in ss:
    command = "diff -w {0}.hack {0}_cmp.hack".format(s)
    print(command)
    os.system(command)
