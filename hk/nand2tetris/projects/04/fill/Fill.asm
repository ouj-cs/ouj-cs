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


	// i = 0;
	// j = 8192
	// while ( 8192 - i >= 0 ) {
	//	SCREEN[i] = 0;
	//	i++;
	// }
	// c = 0
	// while ( true ) {
	// 	n = ~0
	//	if ( KBD[0] == 0 ) {
	//		n = 0;
	//	}
	//	if ( c != n ) {
	//		i = 0;
	//		while ( i < j ) {
	//			SCREEN[i] = !SCREEN[i];
	//			i++;
	//		}
	//		c = n;
	//	}
	// }
// Put your code here.
	@i
	M = 0
	@8192
	D = A
	@j
	M = D
	//(INIT)
	//@j
	//D = M
	//@i
	//D = D - M
	//@ENDINIT
	//D;JLE
	//@i
	//D = M
	//@SCREEN
	//A = A + D
	//M = 0
	//@i
	//M = M + 1
	//@INIT
	//0;JMP
	//(ENDINIT)
	@c
	M = 0
	(LOOP)
	@n
	M = 0
	M = !M
	@KBD
	D = M
	@NOTZERO
	D;JNE
	@n
	M = 0
	(NOTZERO)
	@n
	D = M
	@c
	D = D - M
	@EQUAL
	D;JEQ
	@i
	M = 0
	(DRAW)
	@j
	D = M
	@i
	D = D - M
	@ENDDRAW
	D;JLE
	@i
	D = M
	@SCREEN
	A = A + D
	M = !M
	@i
	M = M + 1
	@DRAW
	0;JMP
	(ENDDRAW)
	@n
	D = M
	@c
	M = D
	(EQUAL)
	@LOOP
	0;JMP
