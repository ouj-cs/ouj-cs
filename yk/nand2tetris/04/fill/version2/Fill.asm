// Project 04 - Fill.asm
(CHECK_KEYBOARD)
    @SCREEN     // pen := SCREEN
    D=A
    @pen
    M=D
    @KBD        // if KBD != 0 then goto FILL_BLACK
    D=M
    @FILL_BLACK
    D;JNE
(FILL_WHITE)
    @pen        // Memory[pen] := 0
    A=M
    M=0
    @pen        // pen := pen + 1
    M=M+1
    @KBD        // if pen = KBD goto CHECK_KEYBOARD
    D=A
    @pen
    D=M-D
    @CHECK_KEYBOARD
    D;JEQ
    @FILL_WHITE // goto FILL_WHITE
    0;JMP
(FILL_BLACK)
    @pen        // Memory[pen] := -1
    A=M
    M=-1
    @pen        // pen := pen + 1
    M=M+1
    @KBD        // if pen = KBD goto CHECK_KEYBOARD
    D=A
    @pen
    D=M-D
    @CHECK_KEYBOARD
    D;JEQ
    @FILL_BLACK // goto FILL_BLACK
    0;JMP
