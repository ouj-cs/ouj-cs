#!/usr/bin/env python3
import os
ss = "Add MaxL Max RectL Rect PongL Pong".split()
for s in ss:
    os.system("./asm.py {0}.asm > {0}.hack".format(s))
