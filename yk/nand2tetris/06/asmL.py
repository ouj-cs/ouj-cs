#!/usr/bin/env python3
import collections
import re
import sys


class Parser:
    def __init__(self):
        self._n_current = 0

        with open(sys.argv[1], "r") as f:
            self._lines = f.read().splitlines()

        for i in range(len(self._lines)):
            line = self._lines[i]
            line = re.sub("//.*", "", line)  # コメントを削除する。
            line = line.strip()
            self._lines[i] = line

        self._lines = [x for x in self._lines if x != ""]  # 空行を削除する。

    def _line(self):
        return self._lines[self._n_current]

    def _split(self):
        line = self._line()
        dest = "null"
        jump = "null"
        ss = line.split("=")

        if len(ss) == 2:
            dest = ss[0]
            line = ss[1]

        ss = line.split(";")

        if len(ss) == 2:
            line = ss[0]
            jump = ss[1]

        comp = line
        return dest, comp, jump

    def hasMoreCommands(self):
        return self._n_current < len(self._lines)

    def advance(self):
        self._n_current += 1

    def commandType(self):
        line = self._line()

        if re.search("@.*", line):
            return "A_COMMAND"

        if re.search("\(.*\)", line):
            return "L_COMMAND"

        return "C_COMMAND"

    def symbol(self):
        line = self._line()
        type = self.commandType()

        if type == "A_COMMAND":
            return line[1:]

        if type == "L_COMMAND":
            return line[1:-1]

    def dest(self):
        dest, _, _ = self._split()
        return dest

    def comp(self):
        _, comp, _ = self._split()
        return comp

    def jump(self):
        _, _, jump = self._split()
        return jump


class Code:
    def __init__(self):
        mnemonic_dest = "null M D MD A AM AD AMD".split()
        binary_dest = "000 001 010 011 100 101 110 111".split()
        assert len(mnemonic_dest) == len(binary_dest)
        self._dict_dest = collections.OrderedDict(
            zip(mnemonic_dest, binary_dest))

        mnemonic_comp = (
            "0 1 -1 D A !D !A -D -A D+1 A+1 D-1 A-1 D+A D-A A-D D&A D|A "
            "_ _ _ _ M _ !M _ -M  _ M+1 _ M-1 D+M D-M M-D D&M D|M").split()
        binary_comp = (
            "0101010 0111111 0111010 0001100 0110000 0001101 0110001 0001111 "
            "0110011 0011111 0110111 0001110 0110010 0000010 0010011 0000111 "
            "0000000 0010101 1101010 1111111 1111010 1001100 1110000 1001101 "
            "1110001 1001111 1110011 1011111 1110111 1001110 1110010 1000010 "
            "1010011 1000111 1000000 1010101").split()
        assert len(mnemonic_comp) == len(binary_comp)
        self._dict_comp = collections.OrderedDict(
            zip(mnemonic_comp, binary_comp))

        mnemonic_jump = "null JGT JEQ JGE JLT JNE JLE JMP".split()
        binary_jump = "000 001 010 011 100 101 110 111".split()
        assert len(mnemonic_jump) == len(binary_jump)
        self._dict_jump = collections.OrderedDict(
            zip(mnemonic_jump, binary_jump))

    def dest(self, mnemonic):
        return self._dict_dest[mnemonic]

    def comp(self, mnemonic):
        return self._dict_comp[mnemonic]

    def jump(self, mnemonic):
        return self._dict_jump[mnemonic]


def main():
    parser = Parser()
    code = Code()

    while parser.hasMoreCommands():
        type = parser.commandType()

        if type == "A_COMMAND":
            symbol = parser.symbol()
            print("0{:015b}".format(int(symbol)))
        elif type == "C_COMMAND":
            mnemonic_dest = parser.dest()
            binary_dest = code.dest(mnemonic_dest)
            mnemonic_comp = parser.comp()
            binary_comp = code.comp(mnemonic_comp)
            mnemonic_jump = parser.jump()
            binary_jump = code.jump(mnemonic_jump)
            print("111{}{}{}".format(binary_comp, binary_dest, binary_jump))

        parser.advance()


if __name__ == "__main__":
    main()
