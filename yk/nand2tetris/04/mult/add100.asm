// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
    // p. 68
    
    // var i := 1
    @i      // A := 16
    M= 1    // M[i] := 1
    
    // var sum := 0
    @sum
    M= 0    // M[sum] := 0
    
(LOOP)
    
    // if i > 100 then goto END
    @i
    D= M    // D := M[i]
    @100
    D= D-A  // D := D - 100; because D > 100 iff D - 100 > 0.
    @END
    D ;JGT  // if D > 0 then goto END
    
    // sum := sum + i
    @i
    D= M    // D := M[i]
    @sum
    M= D+M  // M[sum] := D + M[sum]
    
    // i := i + 1
    @i
    M= M+1  // M[i] := M[i] + 1;
    
    // goto LOOP
    @LOOP
    0 ;JMP  // goto LOOP
    
(END)
    
    // goto END
    @END
    0 ;JMP  // goto END
