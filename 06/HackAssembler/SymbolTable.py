# Manages the symbol Table

table = {
    'R0':0,
    'R1':1,
    'R2':2,
    'R3':3,
    'R4':4,
    'R5':5,
    'R6':6,
    'R7':7,
    'R8':8,
    'R9':9,
    'R10':10,
    'R11':11,
    'R12':12,
    'R13':13,
    'R14':14,
    'R15':15,
    'SCREEN':16384,
    'KBD':24576,
    'SP':0,
    'LCL':1,
    'ARG':2,
    'THIS':3,
    'THAT':4
}

# Read all labels
def firstPass(contents):
	count = 1
	for i in range(len(contents)):
		content = contents[i]
		if content.startswith('('):
			table[content[1:-1]] = (i+1-count)
			count += 1
	return table

# Read all variables
def secondPass(contents, pass1):
	n = 16
	for i in contents:
		if i.startswith('@'):
			key = i[1:]
			if key not in pass1:
				if not key.isdigit():
					pass1.update({key:n})
					n += 1
	return pass1

