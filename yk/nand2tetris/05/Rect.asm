@0
D=M     // D := M[0] // rectangle height
@23
D;JLE   // if D <= 0 then goto 23
@16
M=D     // M[16] := D // height to draw
@16384
D=A     // D := @SCREEN
@17
M=D     // M[17] := D // pen location
@17
A=M     // A := M[17]
M=-1    // M[A] = -1 // fills 16 horizontal pixels with black color
@17
D=M     // D := M[17]
@32
D=D+A   // D := D + 32 // go down 1 pixel
@17
M=D     // M[17] = D // updates pen location
@16
MD=M-1  // M[16], D = M[16] - 1
@10
D;JGT   // if D > 0 then goto 10 // height to draw remains
@23
0;JMP   // goto 23
