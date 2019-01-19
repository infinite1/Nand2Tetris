# Parser unpacks each instruction into its underlying fields

# Load the file from the path
def load(filePath):
	content = []
	with open(filePath) as f:
		raw = f.readlines()
		temp = [i.strip() for i in raw if not i.startswith(('/', '\n'))]
		for i in temp:
			if '//' in i:
				i = i[:i.index('//')]
			content.append(i.strip())
	return content

# Check the instruction types
def isA(i):
	return i.startswith('@')


# Unpacks C-instruction into comp, dest and jump fields	
def fields(i):
	if ';' in i and '=' in i:
		i1 = i.index(';')
		i2 = i.index('=')
		c = i[i2+1:i1]
		d = i[:i2]
		j = i[i1+1:]
	elif ';' in i:
		i1 = i.index(';')
		c = i[:i1]
		d = 'null'
		j = i[i1+1:]
	elif '=' in i:
		i2 = i.index('=')
		c = i[i2+1:]
		d = i[:i2]
		j = 'null'
	return [c, d, j]