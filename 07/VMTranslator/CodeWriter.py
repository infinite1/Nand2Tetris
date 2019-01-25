# Generates assembly code from the parsed VM command


# Generates memory access commands
def write_push_pop(a):
    temp = '// ' + a + '\n'
    a = a.split()
    if a[0] == 'push':
        if a[1] == 'constant':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')
        elif a[1] == 'local':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@LCL\n' + 'D=M+D\n' +
                     '@R13\n' + 'A=D\n' + 'D=M\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')
        elif a[1] == 'argument':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@ARG\n' + 'D=M+D\n' +
                     '@R13\n' + 'A=D\n' + 'D=M\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')
        elif a[1] == 'this':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@THIS\n' + 'D=M+D\n' +
                     '@R13\n' + 'A=D\n' + 'D=M\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')
        elif a[1] == 'that':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@THAT\n' + 'D=M+D\n' +
                     '@R13\n' + 'A=D\n' + 'D=M\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')
        elif a[1] == 'temp':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@5\n' + 'D=A+D\n' +
                     '@R13\n' + 'A=D\n' + 'D=M\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')
        elif a[1] == 'pointer':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@3\n' + 'A=A+D\n' + 'D=M\n' +
                     '@SP\n' + 'A=M\n' + 'M=D\n' + '@SP\n' + 'M=M+1\n')
        elif a[1] == 'static':
            temp += ('@Foo.' + a[2] + '\n' + 'D=M\n' + '@SP\n' + 'A=M\n' + 'M=D\n' +
                     '@SP\n' + 'M=M+1\n')
    elif a[0] == 'pop':
        if a[1] == 'local':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@LCL\n' + 'D=M+D\n' +
                     '@R13\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' + 'D=M\n' +
                     '@R13\n' + 'A=M\n' + 'M=D\n')
        elif a[1] == 'argument':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@ARG\n' + 'D=M+D\n' +
                     '@R13\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' + 'D=M\n' +
                     '@R13\n' + 'A=M\n' + 'M=D\n')
        elif a[1] == 'this':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@THIS\n' + 'D=M+D\n' +
                     '@R13\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' + 'D=M\n' +
                     '@R13\n' + 'A=M\n' + 'M=D\n')
        elif a[1] == 'that':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@THAT\n' + 'D=M+D\n' +
                     '@R13\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' + 'D=M\n' +
                     '@R13\n' + 'A=M\n' + 'M=D\n')
        elif a[1] == 'temp':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@5\n' + 'D=A+D\n' +
                     '@R13\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' + 'D=M\n' +
                     '@R13\n' + 'A=M\n' + 'M=D\n')
        elif a[1] == 'pointer':
            temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@R13\n' + 'M=D\n' +
                     '@' + a[2] + '\n' + 'D=A\n' + '@3\n' + 'D=A+D\n' +
                     '@R14\n' + 'M=D\n' + '@R13\n' + 'D=M\n' + '@R14\n' + 'A=M\n' + 'M=D\n')
        elif a[1] == 'static':
            temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@Foo.' + a[2] + '\n' + 'M=D\n')
    return temp


# Generate arithmetic commands
def write_arithmetic(a):
    temp = '// ' + a + '\n'
    if a == 'add':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'M=M+D\n')
    elif a == 'sub':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'M=M-D\n')
    elif a == 'neg':
        temp += ('@SP\n' + 'A=M-1\n' + 'M=-M\n')
    return temp


# Generate logical commands
def write_logical(a):
    temp = '// ' + a + '\n'
    if a == 'eq':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'D=M-D\n' + 'M=-1\n' + '@EQUAL\n' +
                 'D;JEQ\n' + '@SP\n' + 'A=M-1\n' + 'M=0\n' +
                 '(EQUAL)\n')
    elif a == 'gt':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'D=M-D\n' + 'M=-1\n' + '@GREAT\n' +
                 'D;JGT\n' + '@SP\n' + 'A=M-1\n' + 'M=0\n' +
                 '(GREAT)\n')
    elif a == 'lt':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'D=M-D\n' + 'M=-1\n' + '@LESS\n' +
                 'D;JLT\n' + '@SP\n' + 'A=M-1\n' + 'M=0\n' +
                 '(LESS)\n')
    elif a == 'and':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'M=D&M\n')
    elif a == 'or':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'M=D|M\n')
    elif a == 'not':
        temp += ('@SP\n' + 'A=M-1\n' + 'M=!M\n')
    return temp


