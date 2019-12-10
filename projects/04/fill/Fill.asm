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

(LOOP)

// addr = SCREEN
@SCREEN
D=A
@addr
M=D

// i = 0
@0
D=A
@i
M=D

// n = 8192
@8192
D=A
@n
M=D

// check k value
@KBD
D=M

// if k isn't 0, turn black
@BLACK
D;JNE

// if k is 0, turn white
@WHITE
0;JMP

(BLACK)
// if i >= n, jump to LOOP
@i
D=M
@n
D=D-M
@LOOP
D;JGE

// RAM[addr+i] = -1
@i
D=M
@addr
A=D+M
M=-1

// i+=1
@i
M=M+1

// continue to next 16bit word
@BLACK
0;JMP


(WHITE)
// if i >= n, jump to LOOP
@i
D=M
@n
D=D-M
@LOOP
D;JGE

// RAM[addr+i] = 0
@i
D=M
@addr
A=D+M
M=0

// i+=1
@i
M=M+1

// continue to next 16bit word
@WHITE
0;JMP