// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
//    // R0 := 5
//    @5
//    D= A
//    @R0
//    M= D
//    
//    // R1 := 5
//    @3
//    D= A
//    @R1
//    M= D
    
    // var n_loop := R1
    @R1
    D= M
    @n_loop
    M= D
    
    // var i := 1
    @i
    M= 1    // M[i] := 1
    
    // var sum := 0
    @sum
    M= 0    // M[sum] := 0
    
(LOOP)
    
    // if i > n_loop then goto END
    @i
    D= M    // D := M[i]
    @n_loop
    D= D-M
    @END
    D ;JGT  // if D > 0 then goto END
    
    // sum := sum + R0
    @R0
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
    
    // R2 := sum
    @sum
    D= M    // D := M[sum]
    @R2
    M= D    // M[R2] := D
    
(END2)
    
    // goto END2
    @END2
    0 ;JMP  // goto END2
