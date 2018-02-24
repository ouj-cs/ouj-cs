#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CodeWriter:
    def __init__(self, output_file):
        self.f = open(output_file, "w")
        self.count = 0
        return

    def setFileName(self, fileName):
        self.filename = fileName
        return

    # 算術コマンドをアセンブリコードに変換
    def writeArithmetic(self, command):
        if command == 'add':
            self.f.write("@SP\n")
            self.f.write("M=M-1\n")
            self.f.write("A=M\n")
            self.f.write("D=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=M+D\n")
        elif command == 'sub':
            self.f.write("@SP\n")
            self.f.write("M=M-1\n")
            self.f.write("A=M\n")
            self.f.write("D=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=M-D\n")
        elif command == 'neg':
            self.f.write("@SP\n")
            self.f.write("A=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=-M\n")
        elif command == 'eq':
            self.f.write("@SP\n")
            self.f.write("M=M-1\n")
            self.f.write("A=M\n")
            self.f.write("D=M\n")
            self.f.write("A=A-1\n")
            self.f.write("D=M-D\n")
            self.f.write("@%s.%d.EQUAL\n" % (self.filename, self.count))
            self.f.write("D;JEQ\n")
            self.f.write("@SP\n")
            self.f.write("A=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=0\n")
            self.f.write("@%s.%d.END\n" % (self.filename, self.count))
            self.f.write("0;JMP\n")
            self.f.write("(%s.%d.EQUAL)\n" % (self.filename, self.count))
            self.f.write("@SP\n")
            self.f.write("A=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=-1\n")
            self.f.write("(%s.%d.END)\n" % (self.filename, self.count))
        elif command == 'gt':
            self.f.write("@SP\n")
            self.f.write("M=M-1\n")
            self.f.write("A=M\n")
            self.f.write("D=M\n")
            self.f.write("A=A-1\n")
            self.f.write("D=M-D\n")
            self.f.write("@%s.%d.GT\n" % (self.filename, self.count))
            self.f.write("D;JGT\n")
            self.f.write("@SP\n")
            self.f.write("A=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=0\n")
            self.f.write("@%s.%d.END\n" % (self.filename, self.count))
            self.f.write("0;JMP\n")
            self.f.write("(%s.%d.GT)\n" % (self.filename, self.count))
            self.f.write("@SP\n")
            self.f.write("A=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=-1\n")
            self.f.write("(%s.%d.END)\n" % (self.filename, self.count))
        elif command == 'lt':
            self.f.write("@SP\n")
            self.f.write("M=M-1\n")
            self.f.write("A=M\n")
            self.f.write("D=M\n")
            self.f.write("A=A-1\n")
            self.f.write("D=M-D\n")
            self.f.write("@%s.%d.LT\n" % (self.filename, self.count))
            self.f.write("D;JLT\n")
            self.f.write("@SP\n")
            self.f.write("A=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=0\n")
            self.f.write("@%s.%d.END\n" % (self.filename, self.count))
            self.f.write("0;JMP\n")
            self.f.write("(%s.%d.LT)\n" % (self.filename, self.count))
            self.f.write("@SP\n")
            self.f.write("A=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=-1\n")
            self.f.write("(%s.%d.END)\n" % (self.filename, self.count))

        elif command == 'and':
            self.f.write("@SP\n")
            self.f.write("M=M-1\n")
            self.f.write("A=M\n")
            self.f.write("D=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=M&D\n")
        elif command == 'or':
            self.f.write("@SP\n")
            self.f.write("M=M-1\n")
            self.f.write("A=M\n")
            self.f.write("D=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=M|D\n")
        elif command == 'not':
            self.f.write("@SP\n")
            self.f.write("A=M\n")
            self.f.write("A=A-1\n")
            self.f.write("M=!M\n")

        self.count += 1
        return

    def writePushPop(self, command, segment, index):
        if command == 'push':
            if segment == 'constant':
                self.f.write("@%d\n" % index)
                self.f.write("D=A\n")
                self.f.write("@SP\n")
                self.f.write("A=M\n")
                self.f.write("M=D\n")
                self.f.write("@SP\n")
                self.f.write("M=M+1\n")
            else:
                if segment == 'static':
                    self.f.write("@%s.%d\n" % (self.filename, index))
                else:
                    if segment == 'pointer' or\
                       segment == 'temp':
                        if segment == 'pointer':
                            self.f.write("@3\n")
                        elif segment == 'temp':
                            self.f.write("@5\n")
                        self.f.write("D=A\n")
                    else:
                        if segment == 'argument':
                            self.f.write("@ARG\n")
                        elif segment == 'local':
                            self.f.write("@LCL\n")
                        elif segment == 'this':
                            self.f.write("@THIS\n")
                        elif segment == 'that':
                            self.f.write("@THAT\n")
                        self.f.write("D=M\n")
                    self.f.write("@%d\n" % index)
                    self.f.write("A=D+A\n")
                self.f.write("D=M\n")
                self.f.write("@SP\n")
                self.f.write("A=M\n")
                self.f.write("M=D\n")
                self.f.write("@SP\n")
                self.f.write("M=M+1\n")
        elif command == 'pop':
            # commandがpopの場合は, segmentがconstantにならないと想定
            self.f.write("@SP\n")
            self.f.write("M=M-1\n")
            self.f.write("A=M\n")
            self.f.write("D=M\n")
            self.f.write("@data_pop\n")
            self.f.write("M=D\n")
            if segment == 'static':
                self.f.write("@%s.%d\n" % (self.filename, index))
            else:
                if segment == 'pointer' or \
                   segment == 'temp':
                    if segment == 'pointer':
                        self.f.write("@3\n")
                    else:
                        self.f.write("@5\n")
                    self.f.write("D=A\n")
                else:
                    if segment == 'argument':
                        self.f.write("@ARG\n")
                    elif segment == 'local':
                        self.f.write("@LCL\n")
                    elif segment == 'this':
                        self.f.write("@THIS\n")
                    elif segment == 'that':
                        self.f.write("@THAT\n")
                    self.f.write("D=M\n")
                self.f.write("@%d\n" % index)
                self.f.write("D=D+A\n")
                self.f.write("@pointer_pop\n")
                self.f.write("M=D\n")
                self.f.write("@data_pop\n")
                self.f.write("D=M\n")
                self.f.write("@pointer_pop\n")
                self.f.write("A=M\n")
            self.f.write("M=D\n")
        return

    def close(self):
        self.f.close()
        return
