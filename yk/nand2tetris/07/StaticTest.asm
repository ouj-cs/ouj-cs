// C_PUSH constant 111
@111
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 333
@333
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 888
@888
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP static 8
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@StaticTest.8
M=D     // M[A] := D

// C_POP static 3
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@StaticTest.3
M=D     // M[A] := D

// C_POP static 1
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@StaticTest.1
M=D     // M[A] := D

// C_PUSH static 3
@StaticTest.3
D=M     // D:= M[A]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH static 1
@StaticTest.1
D=M     // D:= M[A]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// sub
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D-M   // D := D - M[M[SP] - 1] (D = x - y)
A=A-1   // A := M[SP] - 2
M=D     // M[M[SP] - 2] := D
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH static 8
@StaticTest.8
D=M     // D:= M[A]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// add
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D+M   // D := D + M[M[SP] - 1] (D = x + y)
A=A-1   // A := M[SP] - 2
M=D     // M[M[SP] - 2] := D
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

