import sys
import Parser
import CodeWriter
import os


# Load file
file = sys.argv[1]

vm_files = []
if os.path.isdir(file):
    files = os.listdir(file)
    for i in files:
        if '.vm' in i:
            vm_files.append(i)

    # Create asm file and add bootstrap code
    temp_file = open(file + '/' + file + '.asm', 'w+')
    if len(vm_files) > 1:
        temp_file.write('@256\nD=A\n@SP\nM=D\n')
        boot_code = CodeWriter.write_function('call Sys.init 0')
        temp_file.write(boot_code)

else:
    vm_files.append(file)
    # Create asm file
    temp = str(file).index('.vm')
    fileName = str(file)[:temp]
    temp_file = open(fileName+'.asm', 'w+')

f = temp_file
# Write corresponding codes into asm file

# Set the initial index of eq, gt and lt labels
eq_index = 1
gt_index = 1
lt_index = 1
call_count = 1

for v in vm_files:
    # check if vm_files are from a directory
    if os.path.isdir(file):
        path = file + '/' + v
        contents = Parser.get_contents(path)
    else:
        contents = Parser.get_contents(v)

    # Get each file name in vm_files
    vm_index = str(v).index('.vm')
    vm_name = str(v)[:vm_index]

    for i in contents:
        w = ''
        if Parser.is_push_pop(i):
            w = CodeWriter.write_push_pop(i)
            # Make unique name for static command
            if 'static' in i:
                w = w.replace('Foo', vm_name)
        elif Parser.is_arithmetic(i):
            w = CodeWriter.write_arithmetic(i)
        elif Parser.is_logical(i):
            w = CodeWriter.write_logical(i)
            # Make unique name for eq command
            if 'eq' in i:
                w = w.replace('EQUAL', 'EQUAL'+str(eq_index))
                eq_index += 1
            # Make unique name for gt command
            elif 'gt' in i:
                w = w.replace('GREAT', 'GREAT' + str(gt_index))
                gt_index += 1
            # Make unique name for lt command
            elif 'lt' in i:
                w = w.replace('LESS', 'LESS' + str(lt_index))
                lt_index += 1
        elif Parser.is_branch(i):
            w = CodeWriter.write_branch(i)
        elif Parser.is_function(i):
            w = CodeWriter.write_function(i)
            if 'call' in i:
                w = w.replace('RET', 'RET' + str(call_count))
                call_count += 1
        f.write(w)

