#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from parser import Parser
from code_writer import CodeWriter

class VMConverter:
    def __init__(self):
        return
    def convert(self, input_file):
        filename = input_file[:input_file.find('.')]
        output_file = filename + '.asm'
        parser = Parser(input_file)
        code_writer = CodeWriter(output_file)
        code_writer.setFileName(os.path.basename(filename))
        parser.reset()
        while parser.hasMoreCommands():
            parser.advance()
            command_type = parser.commandType()
            if command_type == 'C_ARITHMETIC':
                command = parser.arg1()
                code_writer.writeArithmetic(command)
            elif command_type == 'C_PUSH' or\
                 command_type == 'C_POP':
                arg1 = parser.arg1()
                arg2 = parser.arg2()
                if command_type == 'C_PUSH':
                    command = 'push'
                else:
                    command = 'pop'
                code_writer.writePushPop(command, arg1, arg2)

        code_writer.close()
