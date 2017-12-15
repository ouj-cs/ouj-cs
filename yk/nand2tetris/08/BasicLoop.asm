// C_PUSH constant 0
@0
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

// label LOOP_START
(LOOP_START)

// C_PUSH argument 0
@ARG
A=M     // A := M[A]
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH local 0
@LCL
A=M     // A := M[A]
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

// C_POP local 0
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@LCL
A=M     // A := M[A]
M=D     // M[M[A] + index] := D

// C_PUSH argument 0
@ARG
A=M     // A := M[A]
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 1
@1
D=A     // D := A
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

// C_POP argument 0
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@ARG
A=M     // A := M[A]
M=D     // M[M[A] + index] := D

// C_PUSH argument 0
@ARG
A=M     // A := M[A]
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// if-goto LOOP_START
@SP
M=M-1   // M[SP] := M[SP] - 1
A=M     // A := M[SP]
D=M     // D := M[M[SP]]
@LOOP_START
D;JNE

// C_PUSH local 0
@LCL
A=M     // A := M[A]
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

