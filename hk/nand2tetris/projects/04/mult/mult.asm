// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
	@0
	D = M
	@r0
	M = D
	@1
	D = M
	@r1
	M = D
	@i
	M = 1
	@j
	M = 1
	@2
	M = 0
(LOOP)
	@i
	D = M
	@15
	D = D - A
	@END
	D;JGT
	@j
	D = M
	@r0
	D = D & M
	@ENDIF
	D;JEQ
	@r1
	D = M
	@2
	M = D + M
(ENDIF)
	@j
	D = M
	M = D + M
	@r1
	D = M
	M = D + M
	@i
	M = M + 1
	@LOOP
	0;JMP
(END)
	@END
	0;JMP
