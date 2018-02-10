#!/usr/bin/env python3
import collections
import re
import sys


class Parser:
    def __init__(self):
        self._n_current = 0

        # コマンドライン引数をファイルパスと見なして読み込む。
        with open(sys.argv[1], "r") as f:
            # 行を要素とするリストとして保持する。
            self._lines = f.read().splitlines()

        for i in range(len(self._lines)):  # 各行について。
            line = self._lines[i]
            line = re.sub("//.*", "", line)  # コメントを削除する。
            line = line.strip()  # 左右の空白を削除する。
            self._lines[i] = line

        self._lines = [x for x in self._lines if x != ""]  # 空行を削除する。

    def _line(self):
        """現在の行の文字列を返す。"""
        return self._lines[self._n_current]

    def _split(self):
        line = self._line()
        dest = "null"
        jump = "null"
        ss = line.split("=")  # 「=」で分割したリストを得る。

        # 文字列に「=」が含まれるならば、左側を dest、右側を line とする。
        # （そうでなければ、dest は null、line は文字列全体である。）
        if len(ss) == 2:  # リストの要素数が 2 である。
            dest = ss[0]
            line = ss[1]

        ss = line.split(";")

        # line に「;」が含まれるならば、左側を line、右側を jump とする。
        # （そうでなければ、line はそのまま、jump は null である。）
        if len(ss) == 2:
            line = ss[0]
            jump = ss[1]

        comp = line  # line には今や comp ニーモニックだけが残っているはずである。
        return dest, comp, jump

    def hasMoreCommands(self):
        return self._n_current < len(self._lines)

    def advance(self):
        self._n_current += 1

    def commandType(self):
        line = self._line()

        if re.search("@.*", line):  # 「@」で始まる。
            return "A_COMMAND"

        if re.search("\(.*\)", line):  # 丸括弧で囲まれている。
            return "L_COMMAND"

        return "C_COMMAND"

    def symbol(self):
        line = self._line()
        type = self.commandType()

        if type == "A_COMMAND":
            return line[1:]  # 最初の文字「@」を除いて返す。

        if type == "L_COMMAND":
            return line[1:-1]  # 左右の丸括弧を除いて返す。

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
        # リストの要素数が一致することを確認しておく。
        assert len(mnemonic_dest) == len(binary_dest)
        # ニーモニック -> バイナリコード、な連想配列を定義する。
        self._dict_dest = collections.OrderedDict(
            zip(mnemonic_dest, binary_dest))

        # compニーモニックについて、同様に連想配列を定める。
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

        # jumpニーモニックについて、同様に連想配列を定める。
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


class SymbolTable:
    def __init__(self):
        # 連想配列を用意する。シンボル -> アドレス、として用いる。
        self._dict = collections.OrderedDict()

        # 定義済みシンボルを登録していく。
        self.addEntry("SP", 0)
        self.addEntry("LCL", 1)
        self.addEntry("ARG", 2)
        self.addEntry("THIS", 3)
        self.addEntry("THAT", 4)

        for i in range(0, 16):  # R0〜R15 を登録する。
            self.addEntry("R{}".format(i), i)

        self.addEntry("SCREEN", 16384)
        self.addEntry("KBD", 24576)

    def __str__(self):
        return str(self._dict)

    def addEntry(self, symbol, address):
        self._dict[symbol] = address

    def contains(self, symbol):
        return symbol in self._dict

    def getAddress(self, symbol):
        return self._dict[symbol]


def main():
    code = Code()
    table = SymbolTable()
    parser = Parser()
    address = 0

    # 最初のパスを行う。
    while parser.hasMoreCommands():
        type = parser.commandType()

        # ラベルシンボル (Xxx) をシンボルテーブルに登録する。
        if type == "L_COMMAND":
            symbol = parser.symbol()
            table.addEntry(symbol, address)

        # ROMアドレスを動かす。
        if type == "A_COMMAND" or type == "C_COMMAND":
            address += 1

        parser.advance()

    parser = Parser()
    address = 16  # 変数シンボル @Xxx のアドレスは 16 からである。

    # 2 回目のパスを行う。
    while parser.hasMoreCommands():
        type = parser.commandType()

        if type == "A_COMMAND":
            symbol = parser.symbol()

            if re.search("[^0-9]+", symbol):  # @Xxx が数字でない。
                if not table.contains(symbol):  # 未登録である。
                    # 変数シンボル @Xxx と登録する。
                    table.addEntry(symbol, address)
                    address += 1

                integer = table.getAddress(symbol)
            else:  # @Xxx が数字である。
                integer = int(symbol)  # "123" -> 123 などと型変換する。

            # 「0」でパディングしつつ二進数文字列を出力する。
            print("0{:015b}".format(integer))
        elif type == "C_COMMAND":
            # dest、comp、jump の各部分を二進数に変換して出力する。
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
