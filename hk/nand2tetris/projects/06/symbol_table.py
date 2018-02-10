#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SymbolTable:
    def __init__(self):
        self.table = {}
        return

    def addEntry(self, symbol, address):
        self.table[symbol] = address
        return

    def contains(self, symbol):
        return symbol in self.table.keys()

    def getAddress(self, symbol):
        return self.table[symbol]
