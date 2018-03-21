#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from parser import Parser
from code_writer import CodeWriter

class VMConverter:
    def __init__(self):
        return

    def _convert_file(self, input_file):
        print(input_file)
        filename = os.path.basename(input_file[:input_file.find('.')])
        parser = Parser(input_file)
        self.code_writer.setFileName(filename)

        while parser.hasMoreCommands():
            parser.advance()
            command_type = parser.commandType()
            if command_type == 'C_ARITHMETIC':
                command = parser.arg1()
                self.code_writer.writeArithmetic(command)
            elif command_type == 'C_PUSH' or\
                 command_type == 'C_POP':
                arg1 = parser.arg1()
                arg2 = parser.arg2()
                if command_type == 'C_PUSH':
                    command = 'push'
                else:
                    command = 'pop'
                self.code_writer.writePushPop(command, arg1, arg2)
            elif command_type == 'C_LABEL':
                label= parser.arg1()
                self.code_writer.writeLabel(label)
            elif command_type == 'C_GOTO':
                label= parser.arg1()
                self.code_writer.writeGoto(label)
            elif command_type == 'C_IF':
                label= parser.arg1()
                self.code_writer.writeIf(label)
            elif command_type == 'C_FUNCTION':
                 functionName = parser.arg1()
                 numLocals = parser.arg2()
                 self.code_writer.writeFunction(functionName, numLocals)
            elif command_type == 'C_CALL':
                 functionName = parser.arg1()
                 numLocals = parser.arg2()
                 self.code_writer.writeCall(functionName, numLocals)
            elif command_type == 'C_RETURN':
                 self.code_writer.writeReturn()

    def convert(self, input_path):
        output_file = ''
        if os.path.isdir(input_path): # directory
            output_file = input_path + os.sep + os.path.basename(input_path) + '.asm'
        else:                   # file
            output_file = input_path[:input_path.find('.')] + '.asm'

        self.code_writer = CodeWriter(output_file)

        if os.path.isdir(input_path): # directory
            print("directory")
            input_files = []
            files = os.listdir(input_path)

            # write bootstrap code
            self.code_writer.writeInit()

            # find vm files
            for f in files:
                path, ext = os.path.splitext(f)
                if ext == '.vm':
                    input_files.append(input_path + os.sep + f)

            # convert vm files
            for input_file in input_files:
                self._convert_file(input_file)
        else:                   # file
            print("file")
            self._convert_file(input_path)

        self.code_writer.close()

        return
