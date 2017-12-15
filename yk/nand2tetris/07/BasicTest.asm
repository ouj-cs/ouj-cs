// C_PUSH constant 10
@10
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP local 0
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@LCL
A=M     // A := M[A]
M=D     // M[M[A] + index] := D

// C_PUSH constant 21
@21
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 22
@22
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP argument 2
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@ARG
A=M     // A := M[A]
A=A+1
A=A+1
M=D     // M[M[A] + index] := D

// C_POP argument 1
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@ARG
A=M     // A := M[A]
A=A+1
M=D     // M[M[A] + index] := D

// C_PUSH constant 36
@36
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP this 6
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@THIS
A=M     // A := M[A]
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D     // M[M[A] + index] := D

// C_PUSH constant 42
@42
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 45
@45
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP that 5
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@THAT
A=M     // A := M[A]
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D     // M[M[A] + index] := D

// C_POP that 2
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@THAT
A=M     // A := M[A]
A=A+1
A=A+1
M=D     // M[M[A] + index] := D

// C_PUSH constant 510
@510
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP temp 6
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@R5
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D     // M[M[A] + index] := D

// C_PUSH local 0
@LCL
A=M     // A := M[A]
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH that 5
@THAT
A=M     // A := M[A]
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
D=M     // D := M[M[A] + index]
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

// C_PUSH argument 1
@ARG
A=M     // A := M[A]
A=A+1
D=M     // D := M[M[A] + index]
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

// C_PUSH this 6
@THIS
A=M     // A := M[A]
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH this 6
@THIS
A=M     // A := M[A]
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
D=M     // D := M[M[A] + index]
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

// C_PUSH temp 6
@R5
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
D=M     // D := M[M[A] + index]
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

