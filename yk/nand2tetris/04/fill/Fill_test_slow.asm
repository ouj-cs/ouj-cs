// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
    // var white := 0x0000
    @white  // A := white
    M= 0    // M[white] := 0
    
    // var black := 0xffff
    @1      // A := 1
    D= -A   // D := -A
    @black  // A := black
    M= D    // M[black] := D
    
    // var color := black
    @black
    D= M    // D := M[black]
    @color  // A := color
    M= D    // M[color] := D
    
    // pen := SCREEN
    @SCREEN // A := SCREEN
    D= A    // D := A
    @pen    // A := pen
    M= D    // M[pen] := D
    
(LOOP_DRAW)
    // call FUNCTION_DRAW16
    @FUNCTION_DRAW16
    0 ;JMP
(DRAW16_RETURN)
    
    // pen := pen + 1
    @pen    // A := pen
    M= M+1  // M[pen] := M[pen] + 1
    
    @LOOP_DRAW
    0 ;JMP
// end LOOP_DRAW
    
(FUNCTION_DRAW16)
    // M[pen] := color
    @color  // A := color
    D= M    // D := M[color]
    @pen    // A := pen
    A= M    // A := M[pen]
    M= D    // M[A] := D
    
    // return
    @DRAW16_RETURN
    0 ;JMP
// end FUNCTION_DRAW16
