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

(LOOP)
	// if (KBD > 0), blacken the screen 
	@KBD
	D=M
	@ON
	D;JGT

	// if (KBD = 0), clear the screen
	@OFF
	0;JMP

(ON)
	// SET Color = black
	@COLOR
	M=-1

	// Blacken the screen
	@FILL
	0;JMP

(OFF)
	// Set Color = white
	@COLOR
	M=0

	// Clear the screen
	@FILL
	0;JMP

(FILL)
	// Total number of pixels
	@8192
	D=A
	@n
	M=D

	// Screen's base address
	@SCREEN
	D=A
	@addr
	M=D

	@NEXT
	0;JMP

(NEXT)
	@n
	D=M
	@LOOP
	D;JEQ

	// Fill color in pixels
	@COLOR
	D=M
	@addr
	A=M
	M=D
	@addr
	M=M+1
	@n
	M=M-1

	@NEXT
	0;JMP













