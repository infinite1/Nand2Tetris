# Parses each VM command into its lexical elements


# Clean and load file contents
def get_contents(file):
    contents = []
    with open(file) as f:
        raw = f.readlines()
        temp = [i.strip() for i in raw if not i.startswith(('/', '\n'))]
        for i in temp:
            if '//' in i:
                i = i[:i.index('//')]
            contents.append(i.strip())
        return contents


# Decide if push or pop commands
def is_push_pop(c):
    return ('push' in c) or ('pop' in c)


# Decide if arithmetic commands
def is_arithmetic(c):
    c = c.split()
    if len(c) == 1:
        return ('add' in c) or ('sub' in c) or ('neg' in c)
    return False


# Decide if logical commands
def is_logical(c):
    return ('eq' in c) or ('lt' in c) or ('gt' in c) or\
           ('or' in c) or ('and' in c) or ('not' in c)


# Decide if branching commands
def is_branch(c):
    return ('label' in c) or ('goto' in c) or ('if-goto' in c)


# Decide if function commands
def is_function(c):
    return ('function' in c) or ('return' in c) or ('call' in c)
