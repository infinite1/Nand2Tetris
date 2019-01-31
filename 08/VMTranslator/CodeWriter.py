# Generates assembly code from the parsed VM command


# Generates memory access commands
def write_push_pop(a):
    temp = '// ' + a + '\n'
    a = a.split()

    # Translate push
    if a[0] == 'push':

        # Translate constant
        if a[1] == 'constant':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')

        # Translate local
        elif a[1] == 'local':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@LCL\n' + 'D=M+D\n' +
                     '@R13\n' + 'A=D\n' + 'D=M\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')

        # Translate argument
        elif a[1] == 'argument':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@ARG\n' + 'D=M+D\n' +
                     '@R13\n' + 'A=D\n' + 'D=M\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')

        # Translate this
        elif a[1] == 'this':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@THIS\n' + 'D=M+D\n' +
                     '@R13\n' + 'A=D\n' + 'D=M\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')

        # Translate that
        elif a[1] == 'that':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@THAT\n' + 'D=M+D\n' +
                     '@R13\n' + 'A=D\n' + 'D=M\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')

        # Translate temp
        elif a[1] == 'temp':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@5\n' + 'D=A+D\n' +
                     '@R13\n' + 'A=D\n' + 'D=M\n' + '@SP\n' + 'A=M\n' +
                     'M=D\n' + '@SP\n' + 'M=M+1\n')

        # Translate pointer
        elif a[1] == 'pointer':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@3\n' + 'A=A+D\n' + 'D=M\n' +
                     '@SP\n' + 'A=M\n' + 'M=D\n' + '@SP\n' + 'M=M+1\n')

        # Translate constant
        elif a[1] == 'static':
            temp += ('@Foo.' + a[2] + '\n' + 'D=M\n' + '@SP\n' + 'A=M\n' + 'M=D\n' +
                     '@SP\n' + 'M=M+1\n')

    # Translate pop
    elif a[0] == 'pop':

        # Translate local
        if a[1] == 'local':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@LCL\n' + 'D=M+D\n' +
                     '@R13\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' + 'D=M\n' +
                     '@R13\n' + 'A=M\n' + 'M=D\n')

        # Translate argument
        elif a[1] == 'argument':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@ARG\n' + 'D=M+D\n' +
                     '@R13\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' + 'D=M\n' +
                     '@R13\n' + 'A=M\n' + 'M=D\n')

        # Translate this
        elif a[1] == 'this':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@THIS\n' + 'D=M+D\n' +
                     '@R13\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' + 'D=M\n' +
                     '@R13\n' + 'A=M\n' + 'M=D\n')

        # Translate that
        elif a[1] == 'that':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@THAT\n' + 'D=M+D\n' +
                     '@R13\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' + 'D=M\n' +
                     '@R13\n' + 'A=M\n' + 'M=D\n')

        # Translate temp
        elif a[1] == 'temp':
            temp += ('@' + a[2] + '\n' + 'D=A\n' + '@5\n' + 'D=A+D\n' +
                     '@R13\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' + 'D=M\n' +
                     '@R13\n' + 'A=M\n' + 'M=D\n')

        # Translate pointer
        elif a[1] == 'pointer':
            temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@R13\n' + 'M=D\n' +
                     '@' + a[2] + '\n' + 'D=A\n' + '@3\n' + 'D=A+D\n' +
                     '@R14\n' + 'M=D\n' + '@R13\n' + 'D=M\n' + '@R14\n' + 'A=M\n' + 'M=D\n')

        # Translate static
        elif a[1] == 'static':
            temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@Foo.' + a[2] + '\n' + 'M=D\n')

    return temp


# Generate arithmetic commands
def write_arithmetic(a):
    temp = '// ' + a + '\n'

    # Translate add
    if a == 'add':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'M=M+D\n')

    # Translate sub
    elif a == 'sub':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'M=M-D\n')

    # Translate neg
    elif a == 'neg':
        temp += ('@SP\n' + 'A=M-1\n' + 'M=-M\n')

    return temp


# Generate logical commands
def write_logical(a):
    temp = '// ' + a + '\n'

    # Translate eq
    if a == 'eq':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'D=M-D\n' + 'M=-1\n' + '@EQUAL\n' +
                 'D;JEQ\n' + '@SP\n' + 'A=M-1\n' + 'M=0\n' +
                 '(EQUAL)\n')

    # Translate gt
    elif a == 'gt':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'D=M-D\n' + 'M=-1\n' + '@GREAT\n' +
                 'D;JGT\n' + '@SP\n' + 'A=M-1\n' + 'M=0\n' +
                 '(GREAT)\n')

    # Translate lt
    elif a == 'lt':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'D=M-D\n' + 'M=-1\n' + '@LESS\n' +
                 'D;JLT\n' + '@SP\n' + 'A=M-1\n' + 'M=0\n' +
                 '(LESS)\n')

    # Translate and
    elif a == 'and':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'M=D&M\n')

    # Translate or
    elif a == 'or':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@SP\n' +
                 'A=M-1\n' + 'M=D|M\n')

    # Translate not
    elif a == 'not':
        temp += ('@SP\n' + 'A=M-1\n' + 'M=!M\n')

    return temp


# Generate branching commands
def write_branch(a):
    temp = '// ' + a + '\n'
    a = a.split()

    # Translate label declaring
    if a[0] == 'label':
        temp += ('(' + a[1] + ')\n')

    # Translate conditional branching
    elif a[0] == 'if-goto':
        temp += ('@SP\n' + 'AM=M-1\n' + 'D=M\n' + '@' + a[1] +
                 '\n' + 'D;JNE\n')

    # Translate unconditional branching
    elif a[0] == 'goto':
        temp += ('@' + a[1] + '\n' + '0;JMP\n')

    return temp


# Generate function commands
def write_function(a):
    temp = '// ' + a + '\n'
    a = a.split()

    # Translate function declaring
    if a[0] == 'function':
        temp += ('(' + a[1] + ')\n')
        for i in range(int(a[2])):
            temp += ('D=0\n' + '@SP\n' + 'A=M\n' + 'M=D\n' +
                     '@SP\n' + 'M=M+1\n')

    # Translate return
    elif a[0] == 'return':
        temp += ('@LCL\n' + 'D=M\n' + '@FRAME\n' + 'M=D\n' + '@FRAME\n' + 'D=M\n'
                 '@5\n' + 'D=D-A\n' + 'A=D\n' +
                 'D=M\n' + '@retAddr\n' + 'M=D\n' + '@SP\n' + 'AM=M-1\n' +
                 'D=M\n' + '@ARG\n' + 'A=M\n' + 'M=D\n' + '@ARG\n' +
                 'D=M\n' + '@1\n' + 'D=D+A\n' + '@SP\n' + 'M=D\n' +
                 '@FRAME\n' + 'D=M\n' + '@1\n' + 'D=D-A\n' + 'A=D\n' +
                 'D=M\n' + '@THAT\n' + 'M=D\n' + '@FRAME\n' + 'D=M\n' +
                 '@2\n' + 'D=D-A\n' + 'A=D\n' + 'D=M\n' + '@THIS\n' + 'M=D\n' +
                 '@FRAME\n' + 'D=M\n' + '@3\n' + 'D=D-A\n' + 'A=D\n' +
                 'D=M\n' + '@ARG\n' + 'M=D\n' + '@FRAME\n' + 'D=M\n' +
                 '@4\n' + 'D=D-A\n' + 'A=D\n' + 'D=M\n' + '@LCL\n' + 'M=D\n' +
                 '@retAddr\n' + 'A=M\n' + '0;JMP\n')

    # Translate call
    elif a[0] == 'call':
        temp += ('@RET\n' + 'D=A\n' + '@SP\n' + 'A=M\n' + 'M=D\n' + '@SP\n' + 'M=M+1\n' +
                 '@LCL\n' + 'D=M\n' + '@SP\n' + 'A=M\n' + 'M=D\n' + '@SP\n' + 'M=M+1\n' +
                 '@ARG\n' + 'D=M\n' + '@SP\n' + 'A=M\n' + 'M=D\n' + '@SP\n' + 'M=M+1\n' +
                 '@THIS\n' + 'D=M\n' + '@SP\n' + 'A=M\n' + 'M=D\n' + '@SP\n' + 'M=M+1\n' +
                 '@THAT\n' + 'D=M\n' + '@SP\n' + 'A=M\n' + 'M=D\n' + '@SP\n' + 'M=M+1\n' +
                 '@SP\n' + 'D=M\n' + '@5\n' + 'D=D-A\n' + '@' + a[2] + '\n' + 'D=D-A\n' + '@ARG\n' +
                 'M=D\n' + '@SP\n' + 'D=M\n' + '@LCL\n' + 'M=D\n' + '@' + a[1] + '\n' +
                 '0;JMP\n' + '(RET)\n')
    return temp
