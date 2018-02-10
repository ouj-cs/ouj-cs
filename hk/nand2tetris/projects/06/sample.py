#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from assembler import Assembler

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    if (argc != 3):
        quit()

    input_file = argv[1]
    output_file = argv[2]

    assembler = Assembler(input_file)
    assembler.assemble(output_file)
