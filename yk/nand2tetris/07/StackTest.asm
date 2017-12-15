// C_PUSH constant 17
@17
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 17
@17
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// eq
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D-M   // D := D - M[M[SP] - 1] (D = x - y)
A=A-1   // A := M[SP] - 2
M=-1    // M[M[SP] - 2] := -1 (true)
@LABEL0
D;JEQ   // If x == y then goto A.
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
M=0     // M[M[SP] - 2] := 0 (false)
(LABEL0)
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH constant 17
@17
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 16
@16
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// eq
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D-M   // D := D - M[M[SP] - 1] (D = x - y)
A=A-1   // A := M[SP] - 2
M=-1    // M[M[SP] - 2] := -1 (true)
@LABEL1
D;JEQ   // If x == y then goto A.
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
M=0     // M[M[SP] - 2] := 0 (false)
(LABEL1)
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH constant 16
@16
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 17
@17
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// eq
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D-M   // D := D - M[M[SP] - 1] (D = x - y)
A=A-1   // A := M[SP] - 2
M=-1    // M[M[SP] - 2] := -1 (true)
@LABEL2
D;JEQ   // If x == y then goto A.
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
M=0     // M[M[SP] - 2] := 0 (false)
(LABEL2)
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH constant 892
@892
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 891
@891
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// lt
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D-M   // D := D - M[M[SP] - 1] (D = x - y)
A=A-1   // A := M[SP] - 2
M=-1    // M[M[SP] - 2] := -1 (true)
@LABEL3
D;JLT   // If x < y then goto A.
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
M=0     // M[M[SP] - 2] := 0 (false)
(LABEL3)
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH constant 891
@891
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 892
@892
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// lt
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D-M   // D := D - M[M[SP] - 1] (D = x - y)
A=A-1   // A := M[SP] - 2
M=-1    // M[M[SP] - 2] := -1 (true)
@LABEL4
D;JLT   // If x < y then goto A.
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
M=0     // M[M[SP] - 2] := 0 (false)
(LABEL4)
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH constant 891
@891
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 891
@891
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// lt
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D-M   // D := D - M[M[SP] - 1] (D = x - y)
A=A-1   // A := M[SP] - 2
M=-1    // M[M[SP] - 2] := -1 (true)
@LABEL5
D;JLT   // If x < y then goto A.
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
M=0     // M[M[SP] - 2] := 0 (false)
(LABEL5)
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH constant 32767
@32767
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 32766
@32766
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// gt
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D-M   // D := D - M[M[SP] - 1] (D = x - y)
A=A-1   // A := M[SP] - 2
M=-1    // M[M[SP] - 2] := -1 (true)
@LABEL6
D;JGT   // If x > y then goto A.
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
M=0     // M[M[SP] - 2] := 0 (false)
(LABEL6)
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH constant 32766
@32766
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 32767
@32767
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// gt
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D-M   // D := D - M[M[SP] - 1] (D = x - y)
A=A-1   // A := M[SP] - 2
M=-1    // M[M[SP] - 2] := -1 (true)
@LABEL7
D;JGT   // If x > y then goto A.
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
M=0     // M[M[SP] - 2] := 0 (false)
(LABEL7)
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH constant 32766
@32766
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 32766
@32766
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// gt
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D-M   // D := D - M[M[SP] - 1] (D = x - y)
A=A-1   // A := M[SP] - 2
M=-1    // M[M[SP] - 2] := -1 (true)
@LABEL8
D;JGT   // If x > y then goto A.
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
M=0     // M[M[SP] - 2] := 0 (false)
(LABEL8)
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH constant 57
@57
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 31
@31
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// C_PUSH constant 53
@53
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

// C_PUSH constant 112
@112
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

// neg
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
M=-M    // M[M[SP] - 1] := -M[M[SP] - 1]

// and
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D&M   // D := D & M[M[SP] - 1] (D = x & y)
A=A-1   // A := M[SP] - 2
M=D     // M[M[SP] - 2] := D
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// C_PUSH constant 82
@82
D=A     // D := A
@SP     // A := SP
A=M     // A := M[SP]
M=D     // M[M[SP]] := D
@SP     // A := SP
M=M+1   // M[SP] = M[SP] + 1

// or
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
A=A-1   // A := M[SP] - 2
D=M     // D := M[M[SP] - 2] (D = x)
A=A+1   // A := M[SP] - 1
D=D|M   // D := D | M[M[SP] - 1] (D = x | y)
A=A-1   // A := M[SP] - 2
M=D     // M[M[SP] - 2] := D
@SP     // A := SP
M=M-1   // M[SP] = M[SP] - 1

// not
@SP     // A := SP
A=M     // A := M[SP]
A=A-1   // A := M[SP] - 1
M=!M    // M[M[SP] - 1] := !M[M[SP] - 1]

