#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CodeWriter:
    def __init__(self, output_file):
        self.f = open(output_file, "w")
        self.count = 0
        self.index = 0
        self.filename = ""
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
            self.f.write("@SP //lt\n")
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
            self.f.write("D=M\n")       # Dにpopする値が入っている
            self.f.write("@data_pop\n") # data_popに格納
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
                    self.f.write("D=M\n") # baseのアドレスをDに格納
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

    def writeInit(self):
        self.f.write("@256\n")
        self.f.write("D=A\n")
        self.f.write("@SP\n")
        self.f.write("M=D\n")
        # LC, ARG, THIS, THATの初期値は何でも良いと思われる

        self.writeCall("Sys.init", 0)
        # self.f.write("@Sys.init\n")
        # self.f.write("0;JMP\n")
        return

    def writeLabel(self, label):
        self.f.write("(%s) //writeLabel\n" % label)
        return

    def writeGoto(self, label):
        self.f.write("@%s //writeGoto\n" % label)
        self.f.write("0;JMP\n")
        return

    def writeIf(self, label):
        self.f.write("@SP //writeIf\n")
        self.f.write("M=M-1\n")
        self.f.write("A=M\n")
        self.f.write("D=M\n")
        self.f.write("@%s\n" % label)
        self.f.write("D;JNE\n")
        return

    def writeFunction(self, functionName, numLocals):
        label_function = functionName
        self.f.write("(%s) //writeFunction\n" % label_function)
        for _ in range(numLocals):
            self.f.write("@SP\n")
            self.f.write("A=M\n")
            self.f.write("M=0\n")
            self.f.write("@SP\n")
            self.f.write("M=M+1\n")
        return

    def writeCall(self, functionName, numArgs):
        label_function = functionName

        return_address = "%s.%s.%d.return_address" % (self.filename, label_function, self.index)
        self.index += 1
        # push return_address
        self.f.write("@%s // push %s\n" % (return_address, return_address))
        self.f.write("D=A\n")
        self.f.write("@SP\n")
        self.f.write("A=M\n")
        self.f.write("M=D\n")
        self.f.write("@SP\n")
        self.f.write("M=M+1\n")
        # push LCL
        self._pushForWriteCall("LCL")
        # push ARG
        self._pushForWriteCall("ARG")
        # push THIS
        self._pushForWriteCall("THIS")
        # push THAT
        self._pushForWriteCall("THAT")
        # ARG = SP - n - 5
        self.f.write("@SP\n")
        self.f.write("A=M\n")
        for _ in range(numArgs):
            self.f.write("A=A-1\n")

        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("D=A\n")
        self.f.write("@ARG\n")
        self.f.write("M=D\n")
        # LCL = SP
        self.f.write("@SP\n")
        self.f.write("D=M\n")
        self.f.write("@LCL\n")
        self.f.write("M=D\n")
        self.f.write("@%s\n" % label_function)
        self.f.write("0;JMP\n")
        self.f.write("(%s)\n" % return_address)
        return

    # internal use
    def _pushForWriteCall(self, label):
        self.f.write("@%s // push %s\n" % (label, label))
        self.f.write("D=M\n")
        self.f.write("@SP\n")
        self.f.write("A=M\n")
        self.f.write("M=D\n")
        self.f.write("@SP\n")
        self.f.write("M=M+1\n")
        return

    def writeReturn(self):
        self.f.write("@LCL //writeReturn\n")
        self.f.write("D=M\n")   # value of LCL
        # frame(temp var)
        self.f.write("@R13\n")
        self.f.write("M=D\n")   # frame = LCL
        self.f.write("A=M\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("D=M\n")   # *(frame - 5)
        self.f.write("@R14\n")
        self.f.write("M=D\n")   # ret = *(frame - 5)
        self.f.write("@SP\n")
        self.f.write("M=M-1\n")
        self.f.write("A=M\n")
        self.f.write("D=M\n")   # return value
        self.f.write("@ARG\n")
        self.f.write("A=M\n")   # A=ARG
        self.f.write("M=D\n")   # *ARG = pop()
        self.f.write("D=A+1\n")
        self.f.write("@SP\n")
        self.f.write("M=D\n")
        self.f.write("@R13\n")
        self.f.write("A=M\n")
        self.f.write("A=A-1\n")
        self.f.write("D=M\n")
        self.f.write("@THAT\n")
        self.f.write("M=D //THAT = *(frame - 1)\n")
        # THIS = *(frame - 2)
        self.f.write("@R13\n")
        self.f.write("A=M\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("D=M\n")
        self.f.write("@THIS\n")
        self.f.write("M=D //THIS = *(frame - 2)\n")
        # ARG = *(frame - 3)
        self.f.write("@R13\n")
        self.f.write("A=M\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("D=M\n")   # *(frame - 3)
        self.f.write("@ARG\n")
        self.f.write("M=D //ARG = *(frame - 3)\n")
        # LCL = *(frame - 4)
        self.f.write("@R13\n")
        self.f.write("A=M\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("A=A-1\n")
        self.f.write("D=M\n")   # *(frame - 4)
        self.f.write("@LCL\n")
        self.f.write("M=D //LCL = *(frame - 4)\n")
        self.f.write("@R14\n")
        self.f.write("A=M\n")
        self.f.write("0;JMP\n")
        return

    def close(self):
        self.f.close()
        return
