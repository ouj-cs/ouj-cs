#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parser import Parser
from code import Code
from symbol_table import SymbolTable

class Assembler:
    def __init__(self, input_file):
        self.parser = Parser(input_file)
        self.code = Code()
        # 定義済みシンボルの追加
        self.symbol_table = SymbolTable()
        self.symbol_table.addEntry('SP', 0)
        self.symbol_table.addEntry('LCL', 1)
        self.symbol_table.addEntry('ARG', 2)
        self.symbol_table.addEntry('THIS', 3)
        self.symbol_table.addEntry('THAT', 4)
        for i in range(16):
            symbol = 'R%d' % i
            self.symbol_table.addEntry(symbol, i)

        self.symbol_table.addEntry('SCREEN', 16384)
        self.symbol_table.addEntry('KBD', 24576)

    # 1回目. シンボルをsymbol tableに追加
    def first_path(self):
        address = -1
        self.parser.reset()

        while self.parser.hasMoreCommands():
            self.parser.advance()
            if self.parser.a_command():
                symbol = self.parser.symbol()
                if symbol.isdigit():
                    self.symbol_table.addEntry(symbol, int(symbol))
                address += 1
            elif self.parser.c_command():
                address += 1
            elif self.parser.l_command():
                symbol = self.parser.symbol()
                self.symbol_table.addEntry(symbol, address + 1)

    def assemble(self, output_file):
        self.first_path()
        address_var = 16
        self.parser.reset()
        with open(output_file, "w") as f:
            while self.parser.hasMoreCommands():
                self.parser.advance()
                if self.parser.a_command():
                    symbol = self.parser.symbol()
                    if self.symbol_table.contains(symbol):
                        address = self.symbol_table.getAddress(symbol)
                        command = format(address, 'b').zfill(16)
                    else:
                        self.symbol_table.addEntry(symbol, address_var)
                        command = format(address_var, 'b').zfill(16)
                        address_var += 1
                    f.write(command)
                    f.write('\n')
                elif self.parser.c_command():
                    dest_str = self.parser.dest()
                    comp_str = self.parser.comp()
                    jump_str = self.parser.jump()
                    dest = self.code.dest(dest_str)
                    comp = self.code.comp(comp_str)
                    jump = self.code.jump(jump_str)
                    command_binary = (7 << 13) + (comp << 6) + (dest << 3) + jump
                    command = format(command_binary, 'b').zfill(16)
                    f.write(command)
                    f.write('\n')
