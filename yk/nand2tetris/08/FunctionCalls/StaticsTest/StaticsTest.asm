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

// function Class1.set 0
(Class1.set)

// C_PUSH argument 0
@ARG
A=M     // A := M[A]
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP static 0
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@Class1.0
M=D     // M[A] := D

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

// C_POP static 1
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@Class1.1
M=D     // M[A] := D

// C_PUSH constant 0
@0
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

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

// function Class1.get 0
(Class1.get)

// C_PUSH static 0
@Class1.0
D=M     // D:= M[A]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH static 1
@Class1.1
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

// function Sys.init 0
(Sys.init)

// C_PUSH constant 6
@6
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 8
@8
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// call Class1.set 2
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
A=A-1   // A := A - 1
A=A-1   // A := A - 1
D=A     // D := A
@ARG    // A := ARG
M=D     // M[ARG] := D
@SP     // A := SP
D=M     // D := M[SP]
@LCL    // A := LCL
M=D     // M[LCL] := D
@Class1.set
0;JMP   // goto f
(LABEL1)

// C_POP temp 0
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@R5
M=D     // M[M[A] + index] := D

// C_PUSH constant 23
@23
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 15
@15
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// call Class2.set 2
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
A=A-1   // A := A - 1
D=A     // D := A
@ARG    // A := ARG
M=D     // M[ARG] := D
@SP     // A := SP
D=M     // D := M[SP]
@LCL    // A := LCL
M=D     // M[LCL] := D
@Class2.set
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

// call Class1.get 0
@LABEL3
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
@Class1.get
0;JMP   // goto f
(LABEL3)

// call Class2.get 0
@LABEL4
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
@Class2.get
0;JMP   // goto f
(LABEL4)

// label WHILE
(WHILE)

@WHILE
0;JMP

// function Class2.set 0
(Class2.set)

// C_PUSH argument 0
@ARG
A=M     // A := M[A]
D=M     // D := M[M[A] + index]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_POP static 0
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@Class2.0
M=D     // M[A] := D

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

// C_POP static 1
@SP     // A := SP
A=M-1   // A := M[SP] - 1
D=M     // D := M[M[SP] - 1]
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1
@Class2.1
M=D     // M[A] := D

// C_PUSH constant 0
@0
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

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

// function Class2.get 0
(Class2.get)

// C_PUSH static 0
@Class2.0
D=M     // D:= M[A]
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH static 1
@Class2.1
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

