#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Parser:
    # index = -1
    # num_command = 0
    def __init__(self, input_file):
        self.command_line = []
        self.index = -1
        self.num_command = 0
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if line[0] != '/' and line != '\n' and line != '\r':
                    # 改行を消す
                    text = line.replace('\n', '')
                    text = text.replace('\r', '')
                    # 後ろにコメント
                    if text.find('/') != -1:
                        text = text[:text.find('/')]
                    # 先頭及び末尾から空白と改行を削除
                    text = text.strip()
                    self.command_line.append(text)
                    self.num_command += 1

    def hasMoreCommands(self):
        return (self.index + 1) < self.num_command

    def advance(self):
        self.index += 1

    def commandType(self):
        if self.index < 0 or self.index >= self.num_command:
            return ''
        else:
            command = self.command_line[self.index]
            word_list = command.split(' ')
            instruction = word_list[0]
            if instruction == 'add' or \
               instruction == 'sub' or \
               instruction == 'neg' or \
               instruction == 'eq' or \
               instruction == 'gt' or \
               instruction == 'lt' or \
               instruction == 'and' or \
               instruction == 'or' or \
               instruction == 'not':
                return "C_ARITHMETIC"
            elif instruction == 'push':
                return "C_PUSH"
            elif instruction == 'pop':
                return "C_POP"
            elif instruction == 'label':
                return "C_LABEL"
            elif instruction == 'goto':
                return "C_GOTO"
            elif instruction == 'if-goto':
                return "C_IF"
            elif instruction == 'function':
                return "C_FUNCTION"
            elif instruction == 'call':
                return "C_CALL"
            elif instruction == 'return':
                return "C_RETURN"

    # the type of arg1 is string
    def arg1(self):
        if self.index < 0 or self.index >= self.num_command:
            return ''
        else:
            command = self.command_line[self.index]
            word_list = command.split(' ')
            if len(word_list) == 1:
                return word_list[0]
            else:
                return word_list[1]

    # the type of arg2 is int
    def arg2(self):
        if self.index < 0 or self.index >= self.num_command:
            return -1           #エラーを示す
        else:
            command = self.command_line[self.index]
            word_list = command.split(' ')
            return int(word_list[2])
