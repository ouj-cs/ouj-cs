@0
D=M     // D := M[0]
@1
D=D-M   // D := D - M[1]
@10
D;JGT   // if D > 0 then goto 10
@1
D=M     // D := M[1]
@12
0;JMP   // goto 12
@0
D=M     // D := M[0]
@2
M=D     // M[2] = D
@14
0;JMP   // goto 14
