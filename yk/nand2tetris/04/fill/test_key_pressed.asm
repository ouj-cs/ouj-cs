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
(START)
    @KBD    // A := KBD
    D= M    // D := M[KBD]
    
    @PRESSED_NOT
    D ;JEQ
    @PRESSED
    0 ;JMP
    
(PRESSED_NOT)
    @111
    D= A
    @R0
    M= D
    
    @PRESSED_END
    0 ;JMP
    
(PRESSED)
    @222
    D= A
    @R0
    M= D
    
    @PRESSED_END
    0 ;JMP
    
(PRESSED_END)
    // goto START
    @START
    0 ;JMP
