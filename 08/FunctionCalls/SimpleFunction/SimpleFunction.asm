// function SimpleFunction.test 2
(SimpleFunction.test)
D=0
@SP
A=M
M=D
@SP
M=M+1
D=0
@SP
A=M
M=D
@SP
M=M+1
// push local 0
@0
D=A
@LCL
D=M+D
@R13
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 1
@1
D=A
@LCL
D=M+D
@R13
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
// not
@SP
A=M-1
M=!M
// push argument 0
@0
D=A
@ARG
D=M+D
@R13
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
// push argument 1
@1
D=A
@ARG
D=M+D
@R13
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
AM=M-1
D=M
@SP
A=M-1
M=M-D
// return
@LCL
D=M
@FRAME
M=D
@FRAME
D=M
@5
D=D-A
A=D
D=M
@retAddr
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@1
D=D+A
@SP
M=D
@FRAME
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@FRAME
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@FRAME
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@FRAME
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@retAddr
A=M
0;JMP
