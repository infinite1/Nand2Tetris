import sys
import Parser
import CodeWriter

# Load file
file = sys.argv[1]
contents = Parser.get_contents(file)

# Create asm file
temp = str(file).index('.vm')
fileName = str(file)[:temp]
f = open(fileName+'.asm', 'w+')

# Set the initial index of eq, gt and lt labels
eq_index = 1
gt_index = 1
lt_index = 1

# Write corresponding codes into asm file
for i in contents:
    w = ''
    if Parser.is_push_pop(i):
        w = CodeWriter.write_push_pop(i)
    elif Parser.is_arithmetic(i):
        w = CodeWriter.write_arithmetic(i)
    elif Parser.is_logical(i):
        w = CodeWriter.write_logical(i)
        if 'eq' in i:
            w = w.replace('EQUAL', 'EQUAL'+str(eq_index))
            eq_index += 1
        elif 'gt' in i:
            w = w.replace('GREAT', 'GREAT' + str(gt_index))
            gt_index += 1
        elif 'lt' in i:
            w = w.replace('LESS', 'LESS' + str(lt_index))
            lt_index += 1
    f.write(w)

# Terminate the asm program
end = '(END)\n@END\n0;JMP\n'
f.write(end)