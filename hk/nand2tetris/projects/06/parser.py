#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Parser:
    index = -1
    num_command = 0
    command_line = []

    def __init__(self, input_file):
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # 空白を消す
                line = line.replace(' ', '')

                if line[0] != '/' and line != '\n' and line != '\r':
                    # 改行を消す
                    text = line.replace('\n', '')
                    text = text.replace('\r', '')
                    if text.find('/') != -1:
                        text = text[:text.find('/')]
                    self.command_line.append(text)
                    self.num_command += 1

    def reset(self):
        self.index = -1

    def command(self):
        if self.index == -1:
            return ''
        else:
            return self.command_line[self.index]
    def hasMoreCommands(self):
        return (self.index + 1) < self.num_command

    def advance(self):
        self.index += 1

    def commandType(self):
        if self.index == -1:
            return ''
        elif self.a_command():
            return 'A_COMMAND'
        elif self.l_command():
            return 'L_COMMAND'
        elif self.c_command():
            return 'C_COMMAND'

    def a_command(self):
        if self.index == -1:
            return False
        command = self.command()
        return (command[0] == '@')

    def l_command(self):
        if self.index == -1:
            return False
        command = self.command()
        return (command[0] == '(') and (command[-1] == ')')

    def c_command(self):
        if self.index == -1:
            return False
        return (self.a_command() == False) and (self.l_command() == False)


    def symbol(self):
        if self.index == -1:
            return ''
        if self.a_command():
            command = self.command()
            return command[1:]
        elif self.l_command():
            command = self.command()
            return command[1:-1]
        else:
            return ''

    def dest(self):
        if self.c_command():
            command = self.command()
            index = command.find('=')
            if index == -1:
                return 'null'
            else:
                return command[:index]

    def comp(self):
        if self.c_command():
            command = self.command()
            head_comp = command.find('=') + 1
            if command.find(';') == -1:
                return command[head_comp:]
            else:
                tail_comp = command.find(';')
                return command[head_comp:tail_comp]

    def jump(self):
        if self.c_command():
            command = self.command()
            index_semi = command.find(';')
            if index_semi == -1: # null
                return 'null'
            else:
                return command[index_semi+1:]
