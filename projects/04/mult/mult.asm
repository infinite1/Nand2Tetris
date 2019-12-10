// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// sum = 0
@sum
M=0

(LOOP)
// if R1 = 0, go to stop
@R1
D=M
@STOP
D;JEQ

// sum += RAM[R0]
@R0
D=M
@sum
M=D+M

// RAM[R1] -= 1
@R1
M=M-1

// go to LOOP
@LOOP
0;JMP

(STOP)
// RAM[R1] = sum
@sum
D=M
@R2
M=D

(END)
@END
0;JMP