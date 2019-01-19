# Code translates each field into its corresponding binary value

destTable = {
	'M':'001',
	'D':'010',
	'MD':'011',
	'A':'100',
	'AM':'101',
	'AD':'110',
	'AMD':'111',
	'null':'000'
}

compTable = {
	'A':'0110000',
	'D+A':'0000010',
	'D':'0001100',
	'D-M':'1010011',
	'0':'0101010',
	'M':'1110000',
	'1':'0111111',
	'-1':'0111010',
	'!D':'0001101',
	'!A':'0110001',
	'-D':'0001111',
	'-A':'0110011',
	'D+1':'0011111',
	'A+1':'0110111',
	'D-1':'0001110',
	'A-1':'0110010',
	'D-A':'0010011',
	'A-D':'0000111',
	'D&A':'0000000',
	'D|A':'0010101',
	'!M':'1110001',
	'-M':'1110011',
	'M+1':'1110111',
	'M-1':'1110010',
	'D+M':'1000010',
	'M-D':'1000111',
	'D&M':'1000000',
	'D|M':'1010101'
}

jumpTable = {
	'JGT':'001',
	'JMP':'111',
	'JEQ':'010',
	'JGE':'011',
	'JLT':'100',
	'JNE':'101',
	'JLE':'110',
	'null':'000'
}

# Translates comp field
def comp(compName):
	return compTable[compName]

# Translates dest field
def dest(destName):
	return destTable[destName]

# Translates jump field
def jump(jumpName):
	return jumpTable[jumpName]