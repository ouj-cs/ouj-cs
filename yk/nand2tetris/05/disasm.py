#!/usr/bin/env python3
import collections
import sys

filename = sys.argv[1]

with open(filename, "r") as f:
    lines = f.read().splitlines()

cx = "101010 111111 111010 001100 110000 001101 110001 001111 110011 011111 110111 001110 110010 000010 010011 000111 000000 010101".split()
mnemonic_a0 = "0 1 -1 D A !D !A -D -A D+1 A+1 D-1 A-1 D+A D-A A-D D&A D|A".split()
mnemonic_a1 = "_ _ _ _ M _ !M _ -M _ M+1 _ M-1 D+M D-M M-D D&M D|M".split()
a0 = collections.OrderedDict(zip(cx, mnemonic_a0))
a1 = collections.OrderedDict(zip(cx, mnemonic_a1))
del cx; del mnemonic_a0; del mnemonic_a1;

dx = "000 001 010 011 100 101 110 111".split()
mnemonic_d = "null M D MD A AM AD AMD".split()
d = collections.OrderedDict(zip(dx, mnemonic_d))
del dx; del mnemonic_d;

jx = "000 001 010 011 100 101 110 111".split()
mnemonic_j = "null JGT JEQ JGE JLT JNE JLE JMP".split()
j = collections.OrderedDict(zip(jx, mnemonic_j))
del jx; del mnemonic_j;

for line in lines:
    bin_i = line[0]
    bin_x = line[1:3]
    bin_a = line[3]
    bin_comp = line[4:10]
    bin_dest = line[10:13]
    bin_jump = line[13:16]
    s = ""
    
    if bin_i == "0":
        s += "@"
        s += str(int(line[1:16], 2))
    else:
        if d[bin_dest] != "null":
            s += d[bin_dest] + "="
        
        if bin_a == "0":
            s += a0[bin_comp]
        else:
            s += a1[bin_comp]
        
        if j[bin_jump] != "null":
            s += ";" + j[bin_jump]
    
    print(s)
