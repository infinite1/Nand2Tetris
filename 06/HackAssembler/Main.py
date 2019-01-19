# Main intializes I/O files and drive the assembling process

import Parser
import Code
import SymbolTable


# Load file
contents = Parser.load(filePath)

# Pass labeles and variables into symbol table
pass1 = SymbolTable.firstPass(contents)
table = SymbolTable.secondPass(contents, pass1)

# Remove labels in contents
contents = [x for x in contents if not x.startswith('(')]

# Parsing, Translating and then writing the instructions in binary
f = open(fileName,"w+")
for i in contents:
    b = 0
    if Parser.isA(i):
        i = i[1:]
        if i.isdigit():
            value = int(i)
            b = '{0:016b}'.format(value)
        else:
            b = '{0:016b}'.format(table[i])
    else:
        [c, d, j] = Parser.fields(i)
        cc = Code.comp(c)
        dd = Code.dest(d)
        jj = Code.jump(j)
        b = '111' + cc + dd + jj
    f.write(b + '\n')
