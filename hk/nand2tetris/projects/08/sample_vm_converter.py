#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from vm_converter import VMConverter

if __name__ == '__main__':
    argv = sys.argv
    input_file = argv[1]
    vm_converter = VMConverter()
    vm_converter.convert(input_file)
