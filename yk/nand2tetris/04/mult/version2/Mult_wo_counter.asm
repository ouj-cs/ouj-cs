// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// where R0 >= 0 and R1 >= 0 and R0 * R1 < 32768.
    @R2     // R2 := 0
    M=0
    @mask   // mask := 1
    M=1
(LOOP)
    @mask   // if mask & R0 = 0 then goto IGNORE
    D=M
    @R0
    D=D&M
    @IGNORE
    D;JEQ
    @R1     // R2 += R1
    D=M
    @R2
    M=D+M
(IGNORE)
    @mask   // mask = 2 * mask
    D=M
    M=D+M
    @R1     // R1 = 2 * R1
    D=M
    M=D+M
    @mask   // if mask != 0 then goto LOOP
    D=M
    @LOOP
    D;JNE
(END)
    @END    // goto END
    0;JMP
