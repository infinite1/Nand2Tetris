# Parses each VM command into its lexical elements


# Clean and load file contents
def get_contents(file):
    with open(file) as f:
        raw = f.readlines()
        contents = [i.strip() for i in raw if not i.startswith(('/', '\n'))]
        return contents


# Determine command types
def is_push_pop(c):
    return ('push' in c) or ('pop' in c)


def is_arithmetic(c):
    return ('add' in c) or ('sub' in c) or ('neg' in c)


def is_logical(c):
    return ('eq' in c) or ('lt' in c) or ('gt' in c) or\
           ('or' in c) or ('and' in c) or ('not' in c)
