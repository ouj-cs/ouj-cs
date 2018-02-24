#!/usr/bin/env python3
import collections
import os
import re
import sys


class Parser:
    def __init__(self, path):
        self.__n_current = 0

        with open(path, "r") as f:
            self.__lines = f.read().splitlines()

        for i in range(len(self.__lines)):
            line = self.__lines[i]
            line = re.sub("//.*", "", line)  # removes comments
            line = line.strip()
            self.__lines[i] = line

        # removes empty lines
        self.__lines = [x for x in self.__lines if x != ""]
        print("\n".join(self.__lines))

    def __line(self):
        return self.__lines[self.__n_current]

    def hasMoreCommands(self):
        return self.__n_current < len(self.__lines)

    def advance(self):
        self.__n_current += 1

    def commandType(self):
        arg0 = self.__arg0()

        if arg0 in "add sub neg eq gt lt and or not".split():
            return "C_ARITHMETIC"

        d = collections.OrderedDict(zip(
                "push pop label goto if-goto function call return"
                .split(),
                "C_PUSH C_POP C_LABEL C_GOTO C_IF C_FUNCTION C_RETURN C_CALL"
                .split()))
        return d[arg0]

    def __arg0(self):
        return self.__line().split()[0]

    def arg1(self):
        if self.commandType() == "C_ARITHMETIC":
            return self.__arg0()

        return self.__line().split()[1]

    def arg2(self):
        return int(self.__line().split()[2])


class CodeWriter:
    def __init__(self, path):
        print("path_output = {}".format(path))
        self.__file = open(path, "w")
        self.__n_label = 0

    def __get_label(self):
        s = "LABEL{}".format(self.__n_label)
        self.__n_label += 1
        return s

    def setFileName(self, fileName):
        self.__fileName = fileName

    def writeArithmetic(self, command):
        s = ""
        s += "// {}\n".format(command)

        if command == "add":
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "D=M     // D := M[M[SP] - 2] (D = x)\n"
            s += "A=A+1   // A := M[SP] - 1\n"
            s += "D=D+M   // D := D + M[M[SP] - 1] (D = x + y)\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "M=D     // M[M[SP] - 2] := D\n"
            s += "@SP     // A := SP\n"
            s += "M=M-1   // M[SP] = M[SP] - 1\n"
        elif command == "sub":
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "D=M     // D := M[M[SP] - 2] (D = x)\n"
            s += "A=A+1   // A := M[SP] - 1\n"
            s += "D=D-M   // D := D - M[M[SP] - 1] (D = x - y)\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "M=D     // M[M[SP] - 2] := D\n"
            s += "@SP     // A := SP\n"
            s += "M=M-1   // M[SP] = M[SP] - 1\n"
        elif command == "neg":
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "M=-M    // M[M[SP] - 1] := -M[M[SP] - 1]\n"
        elif command == "eq":
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "D=M     // D := M[M[SP] - 2] (D = x)\n"
            s += "A=A+1   // A := M[SP] - 1\n"
            s += "D=D-M   // D := D - M[M[SP] - 1] (D = x - y)\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "M=-1    // M[M[SP] - 2] := -1 (true)\n"
            label = self.__get_label()
            s += "@{}\n".format(label)
            s += "D;JEQ   // If x == y then goto A.\n"
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "M=0     // M[M[SP] - 2] := 0 (false)\n"
            s += "({})\n".format(label)
            s += "@SP     // A := SP\n"
            s += "M=M-1   // M[SP] = M[SP] - 1\n"
        elif command == "gt":
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "D=M     // D := M[M[SP] - 2] (D = x)\n"
            s += "A=A+1   // A := M[SP] - 1\n"
            s += "D=D-M   // D := D - M[M[SP] - 1] (D = x - y)\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "M=-1    // M[M[SP] - 2] := -1 (true)\n"
            label = self.__get_label()
            s += "@{}\n".format(label)
            s += "D;JGT   // If x > y then goto A.\n"
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "M=0     // M[M[SP] - 2] := 0 (false)\n"
            s += "({})\n".format(label)
            s += "@SP     // A := SP\n"
            s += "M=M-1   // M[SP] = M[SP] - 1\n"
        elif command == "lt":
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "D=M     // D := M[M[SP] - 2] (D = x)\n"
            s += "A=A+1   // A := M[SP] - 1\n"
            s += "D=D-M   // D := D - M[M[SP] - 1] (D = x - y)\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "M=-1    // M[M[SP] - 2] := -1 (true)\n"
            label = self.__get_label()
            s += "@{}\n".format(label)
            s += "D;JLT   // If x < y then goto A.\n"
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "M=0     // M[M[SP] - 2] := 0 (false)\n"
            s += "({})\n".format(label)
            s += "@SP     // A := SP\n"
            s += "M=M-1   // M[SP] = M[SP] - 1\n"
        elif command == "and":
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "D=M     // D := M[M[SP] - 2] (D = x)\n"
            s += "A=A+1   // A := M[SP] - 1\n"
            s += "D=D&M   // D := D & M[M[SP] - 1] (D = x & y)\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "M=D     // M[M[SP] - 2] := D\n"
            s += "@SP     // A := SP\n"
            s += "M=M-1   // M[SP] = M[SP] - 1\n"
        elif command == "or":
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "D=M     // D := M[M[SP] - 2] (D = x)\n"
            s += "A=A+1   // A := M[SP] - 1\n"
            s += "D=D|M   // D := D | M[M[SP] - 1] (D = x | y)\n"
            s += "A=A-1   // A := M[SP] - 2\n"
            s += "M=D     // M[M[SP] - 2] := D\n"
            s += "@SP     // A := SP\n"
            s += "M=M-1   // M[SP] = M[SP] - 1\n"
        elif command == "not":
            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "A=A-1   // A := M[SP] - 1\n"
            s += "M=!M    // M[M[SP] - 1] := !M[M[SP] - 1]\n"

        self.__file.write(s + "\n")

    def writePushPop(self, command, segment, index):
        s = ""
        s += "// {} {} {}\n".format(command, segment, index)

        if command == "C_PUSH":
            if segment == "constant":
                s += "@{}\n".format(index)
                s += "D=A     // D := A\n"
            elif segment in "local argument this that pointer temp".split():
                d = collections.OrderedDict(zip(
                        "local argument this that pointer temp".split(),
                        "LCL ARG THIS THAT THIS R5".split()))
                s += "@{}\n".format(d[segment])
                if segment not in "pointer temp":
                    s += "A=M     // A := M[A]\n"
                for _ in range(index):
                    s += "A=A+1\n"
                s += "D=M     // D := M[M[A] + index]\n"
            elif segment == "static":
                s += "@{}.{}\n".format(self.__fileName, index)
                s += "D=M     // D:= M[A]\n"

            s += "@SP     // A := SP\n"
            s += "A=M     // A := M[SP]\n"
            s += "M=D     // M[M[SP]] := D\n"
            s += "@SP     // A := SP\n"
            s += "M=M+1   // M[SP] = M[SP] + 1\n"
        elif command == "C_POP":
            s += "@SP     // A := SP\n"
            s += "A=M-1   // A := M[SP] - 1\n"
            s += "D=M     // D := M[M[SP] - 1]\n"
            s += "@SP     // A := SP\n"
            s += "M=M-1   // M[SP] = M[SP] - 1\n"

            if segment in "local argument this that pointer temp".split():
                d = collections.OrderedDict(zip(
                        "local argument this that pointer temp".split(),
                        "LCL ARG THIS THAT THIS R5".split()))
                s += "@{}\n".format(d[segment])
                if segment not in "pointer temp":
                    s += "A=M     // A := M[A]\n"
                for _ in range(index):
                    s += "A=A+1\n"
                s += "M=D     // M[M[A] + index] := D\n"
            elif segment == "static":
                s += "@{}.{}\n".format(self.__fileName, index)
                s += "M=D     // M[A] := D\n"

        self.__file.write(s + "\n")

    def close(self):
        self.__file.close()


def get_paths():
    argv_1 = sys.argv[1]
#    print("argv_1 = {}".format(argv_1))
    is_exists = os.path.exists(argv_1)
#    print("exists = {}".format(is_exists))
    if not is_exists:
        raise Exception('File "{}" not exists.'.format(argv_1))
    path_abs = os.path.abspath(argv_1)
#    print("path_abs = {}".format(path_abs))
    is_dir = os.path.isdir(path_abs)
#    print("is_dir = {}".format(is_dir))
    if not is_dir:
        return [path_abs]


def get_path_output():
    argv_1 = sys.argv[1]
    basename = os.path.basename(argv_1)
    name = os.path.splitext(basename)[0]
    path_abs = os.path.abspath(argv_1)
    dirname = os.path.dirname(path_abs)
    return "{}/{}.asm".format(dirname, name)


def main():
    paths = get_paths()
#    print("paths = {}".format(paths))
    path_output = get_path_output()
    writer = CodeWriter(path_output)

    for path in paths:
        parser = Parser(path)
        writer.setFileName(os.path.splitext(os.path.basename(path))[0])

        while parser.hasMoreCommands():
            type = parser.commandType()

            if type == "C_ARITHMETIC":
                writer.writeArithmetic(parser.arg1())
            elif type in "C_PUSH C_POP".split():
                writer.writePushPop(type, parser.arg1(), parser.arg2())

            parser.advance()


if __name__ == "__main__":
    main()
