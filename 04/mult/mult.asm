// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
	
	// Let n = R1
	@R1
	D=M
	@n
	M=D		

	// Let sum = 0
	@sum
	M=0

(LOOP)
	// if (n = 0) goto STOP
	@n
	D=M

	@STOP
	D;JEQ

	// sum = sum + m
	@R0
	D=M

	@sum
	M=M+D

	// n = n - 1
	@n
	M=M-1

	@LOOP
	0;JMP

(STOP)
	// R2 = sum
	@sum
	D=M
	
	@R2
	M=D

(END)
	@END
	0;JMP