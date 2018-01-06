// function SimpleFunction.test 2
(SimpleFunction.test)
@SP     // A := SP
A=M     // A := M[SP]
M=0     // M[M[SP]] := 0
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@SP     // A := SP
A=M     // A := M[SP]
M=0     // M[M[SP]] := 0
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1

// C_PUSH local 0
@LCL
A=M     // A := M[A]
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH local 1
@LCL
A=M     // A := M[A]
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

// not
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
M=!M    // M[M[SP] - 1] := !M[M[SP] - 1]

// C_PUSH argument 0
@ARG
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

// return
@LCL    // A := LCL
D=M     // D := M[LCL]
@R13    // A := R13
M=D     // M[R13] := D
A=M     // A := M[R13]
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
D=M     // D := M[M[R13] - 5]
@R14    // A := R14
M=D     // M[R14] := D (return address)
@SP     // A := SP
M=M-1   // M[SP] := M[SP] - 1
A=M     // A := M[SP]
D=M     // D := M[M[SP]]
@ARG    // A := ARG
A=M     // A := M[ARG]
M=D     // M[M[ARG]] := D (return value)
D=A+1   // D := M[ARG] + 1
@SP     // A := SP
M=D     // M[SP] := D (stack top)
@R13    // A := R13
A=M     // A := M[R13]
A=A-1   // A := A - 1
D=M     // D := M[M[R13] - 1]
@THAT   // A := THAT
M=D     // M[THAT] := D
@R13    // A := R13
A=M     // A := M[R13]
A=A-1   // A := A - 1
A=A-1   // A := A - 1
D=M     // D := M[M[R13] - 2]
@THIS   // A := THIS
M=D     // M[THIS] := D
@R13    // A := R13
A=M     // A := M[R13]
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
D=M     // D := M[M[R13] - 3]
@ARG    // A := ARG
M=D     // M[ARG] := D
@R13    // A := R13
A=M     // A := M[R13]
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
D=M     // D := M[M[R13] - 4]
@LCL    // A := LCL
M=D     // M[LCL] := D
@R14    // A := R14
A=M     // A := M[R14]
0;JMP   // goto M[R14]

