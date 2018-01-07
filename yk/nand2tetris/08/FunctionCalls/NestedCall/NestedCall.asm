// bootstrap
@256
D=A
@SP
M=D     // M[SP] := 256
@333
D=A
@LCL
M=D     // M[LCL] := 333
@444
D=A
@ARG
M=D     // M[ARG] := 444
@555
D=A
@THIS
M=D     // M[THIS] := 555
@666
D=A
@THAT
M=D     // M[THAT] := 666

// call Sys.init 0
@LABEL0
D=A     // D := return-address
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (return-address)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@LCL    // A := LCL
D=M     // D := M[LCL]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (LCL of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@ARG    // A := ARG
D=M     // D := M[ARG]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (ARG of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@THIS   // A := THIS
D=M     // D := M[THIS]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (THIS of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@THAT   // A := THAT
D=M     // D := M[THAT]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (THAT of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
D=A     // D := A
@ARG    // A := ARG
M=D     // M[ARG] := D
@SP     // A := SP
D=M     // D := M[SP]
@LCL    // A := LCL
M=D     // M[LCL] := D
@Sys.init
0;JMP   // goto f
(LABEL0)

// function Sys.init 0
(Sys.init)

// C_PUSH constant 4000
@4000
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP pointer 0
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@THIS
M=D     // M[M[A] + index] := D

// C_PUSH constant 5000
@5000
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP pointer 1
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@THIS
A=A+1
M=D     // M[M[A] + index] := D

// call Sys.main 0
@LABEL1
D=A     // D := return-address
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (return-address)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@LCL    // A := LCL
D=M     // D := M[LCL]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (LCL of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@ARG    // A := ARG
D=M     // D := M[ARG]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (ARG of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@THIS   // A := THIS
D=M     // D := M[THIS]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (THIS of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@THAT   // A := THAT
D=M     // D := M[THAT]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (THAT of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
D=A     // D := A
@ARG    // A := ARG
M=D     // M[ARG] := D
@SP     // A := SP
D=M     // D := M[SP]
@LCL    // A := LCL
M=D     // M[LCL] := D
@Sys.main
0;JMP   // goto f
(LABEL1)

// C_POP temp 1
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@R5
A=A+1
M=D     // M[M[A] + index] := D

// label LOOP
(LOOP)

@LOOP
0;JMP

// function Sys.main 5
(Sys.main)
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
@SP     // A := SP
A=M     // A := M[SP]
M=0     // M[M[SP]] := 0
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1

// C_PUSH constant 4001
@4001
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP pointer 0
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@THIS
M=D     // M[M[A] + index] := D

// C_PUSH constant 5001
@5001
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP pointer 1
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@THIS
A=A+1
M=D     // M[M[A] + index] := D

// C_PUSH constant 200
@200
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP local 1
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@LCL
A=M     // A := M[A]
A=A+1
M=D     // M[M[A] + index] := D

// C_PUSH constant 40
@40
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP local 2
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@LCL
A=M     // A := M[A]
A=A+1
A=A+1
M=D     // M[M[A] + index] := D

// C_PUSH constant 6
@6
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP local 3
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@LCL
A=M     // A := M[A]
A=A+1
A=A+1
A=A+1
M=D     // M[M[A] + index] := D

// C_PUSH constant 123
@123
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// call Sys.add12 1
@LABEL2
D=A     // D := return-address
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (return-address)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@LCL    // A := LCL
D=M     // D := M[LCL]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (LCL of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@ARG    // A := ARG
D=M     // D := M[ARG]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (ARG of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@THIS   // A := THIS
D=M     // D := M[THIS]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (THIS of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@THAT   // A := THAT
D=M     // D := M[THAT]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D (THAT of the calling function)
@SP     // A := SP
M=M+1   // M[SP] := M[SP] + 1
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
A=A-1   // A := A - 1
D=A     // D := A
@ARG    // A := ARG
M=D     // M[ARG] := D
@SP     // A := SP
D=M     // D := M[SP]
@LCL    // A := LCL
M=D     // M[LCL] := D
@Sys.add12
0;JMP   // goto f
(LABEL2)

// C_POP temp 0
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@R5
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

// C_PUSH local 2
@LCL
A=M     // A := M[A]
A=A+1
A=A+1
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH local 3
@LCL
A=M     // A := M[A]
A=A+1
A=A+1
A=A+1
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH local 4
@LCL
A=M     // A := M[A]
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

// function Sys.add12 0
(Sys.add12)

// C_PUSH constant 4002
@4002
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP pointer 0
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@THIS
M=D     // M[M[A] + index] := D

// C_PUSH constant 5002
@5002
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP pointer 1
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@THIS
A=A+1
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

// C_PUSH constant 12
@12
D=A     // D := A
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

