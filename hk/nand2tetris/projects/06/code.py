#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Code:
    def __init__(self):
        return

    def dest(self, mnemonic):
        if mnemonic == 'null':
            return 0
        else:
            ret = 0
            # 順不同にした
            for c in mnemonic:
                if c == 'A':
                    ret = ret + (1 << 2)
                elif c == 'D':
                    ret = ret + (1 << 1)
                elif c == 'M':
                    ret = ret + (1 << 0)
            return ret

    def comp(self, mnemonic):
            if mnemonic == '0':
                return 0b0101010
            if mnemonic == '1':
                return 0b0111111
            if mnemonic == '-1':
                return 0b0111010
            if mnemonic == 'D':
                return 0b0001100
            if mnemonic == 'A':
                return 0b0110000
            if mnemonic == 'M':
                return 0b1110000
            if mnemonic == '!D':
                return 0b0001101
            if mnemonic == '!A':
                return 0b0110001
            if mnemonic == '!M':
                return 0b1110001
            if mnemonic == '-D':
                return 0b0001111
            if mnemonic == '-A':
                return 0b0110011
            if mnemonic == '-M':
                return 0b1110011
            if mnemonic == 'D+1':
                return 0b0011111
            if mnemonic == 'A+1':
                return 0b0110111
            if mnemonic == 'M+1':
                return 0b1110111
            if mnemonic == 'D-1':
                return 0b0001110
            if mnemonic == 'A-1':
                return 0b0110010
            if mnemonic == 'M-1':
                return 0b1110010
            if mnemonic == 'D+A':
                return 0b0000010
            if mnemonic == 'D+M':
                return 0b1000010
            if mnemonic == 'D-A':
                return 0b0010011
            if mnemonic == 'D-M':
                return 0b1010011
            if mnemonic == 'A-D':
                return 0b0000111
            if mnemonic == 'M-D':
                return 0b1000111
            if mnemonic == 'D&A':
                return 0b0000000
            if mnemonic == 'D&M':
                return 0b1000000
            if mnemonic == 'D|A':
                return 0b0010101
            if mnemonic == 'D|M':
                return 0b1010101
            # if comp.find('M') != -1:
            #     ret_list[0] = '1' # a
            # if comp.find('D') == -1:
            #     ret_list[1] = '1' # c1
            # if comp.find('A') == -1 and comp.find('M') == -1:
            #     ret_list[3] = '1' # c3

    def jump(self, mnemonic):
        if mnemonic == 'null':
            return 0b000
        if mnemonic == 'JGT':
            return 0b001
        if mnemonic == 'JEQ':
            return 0b010
        if mnemonic == 'JGE':
            return 0b011
        if mnemonic == 'JLT':
            return 0b100
        if mnemonic == 'JNE':
            return 0b101
        if mnemonic == 'JLE':
            return 0b110
        if mnemonic == 'JMP':
            return 0b111
