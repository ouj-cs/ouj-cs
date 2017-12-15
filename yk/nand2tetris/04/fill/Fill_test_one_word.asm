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
    
    // pen = SCREEN
    @SCREEN
    D= A
    @pen
    M= D
    
(LOOP_MAIN)
    // color = 0
    @color  // A := color
    M= 0    // M[color] = 0
    
// begin if
    // if keys are not pressed then goto PRESSED_NOT
    @KBD    // A := KBD
    D= M    // D := M[KBD]
    @PRESSED_NOT
    D ;JEQ
    
    // if key is pressed then color = 0xffff
    @1  // A := 1
    D= -A   // D := -A
    @color  // A := color
    M= D    // M[color] := D
(PRESSED_NOT)
// end if
    
    // M[pen] = color
    @color  // A := color
    D= M    // D := M[color]
    @pen    // A := pen
    A= M    // A := M[pen]
    M= D    // M[M[pen]] := D
    
    
    // goto LOOP_MAIN
    @LOOP_MAIN
    0 ;JMP
