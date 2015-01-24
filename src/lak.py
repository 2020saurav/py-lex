import lex
from lex import TOKEN

tokens=[]
keywordlist = ['and', 'break', 'class', 'continue', 
              'elif', 'else', 'for',
              'if', 'import', 'in', 
              'not', 'or', 'print', 'return', 
              'while','def']
RESERVED = {}
for keyword in keywordlist:
	name = keyword.upper()
	RESERVED[keyword] = name
	tokens.append(name)

tokens = tuple(tokens) + (	'ARROW','EQEQUAL','NOTEQUAL','LESSEQUAL','LEFTSHIFT',
							'GREATEREQUAL','RIGHTSHIFT','PLUSEQUAL', 'MINEQUAL',
							'STAREQUAL','SLASHEQUAL','PERCENTEQUAL','COLON','COMMA',
							'SEMI','PLUS','MINUS','STAR','SLASH','VBAR','AMPER',
							'LESS','GREATER','EQUAL','DOT','PERCENT','BACKQUOTE',
							'CIRCUMFLEX','TILDE','AT','LPAR','RPAR','LBRACE',
							'RBRACE','LSQB','RSQB')

tokens = tuple(tokens) +('NEWLINE','NUMBER','NAME','INDENT', 'SQUOTE','DQUOTE')

# All tokens defined by functions are added in the same order as they appear in the lexer file.
# Tokens defined by strings are added next by sorting them in order of decreasing 
#regular expression length (longer expressions are added first).
# Order important. Match '==' before '=', so put '==' before
# Regular expression rules for simple tokens
# These are sorted with 3-character tokens first, then 2-character then 1.
t_ARROW          = '->'

t_EQEQUAL = r'=='
t_NOTEQUAL =  r'!='
t_LESSEQUAL = r'<='
t_LEFTSHIFT = r'<<'
t_GREATEREQUAL = r'>='
t_RIGHTSHIFT  = r'>>'
t_PLUSEQUAL = r'\+='
t_MINEQUAL = r'-='
t_STAREQUAL = r'\*='
t_SLASHEQUAL = r'/='
t_PERCENTEQUAL = r'%='

t_COLON = r':'
t_COMMA = r','
t_SEMI  = r';'
t_PLUS  = r'\+'
t_MINUS = r'-'
t_STAR  = r'\*'
t_SLASH = r'/'
t_VBAR  = r'\|'
t_AMPER = r'&'
t_LESS  = r'<'
t_GREATER = r'>'
t_EQUAL = r'='
t_DOT  = r'\.'
t_PERCENT = r'%'
t_BACKQUOTE  = r'`'
t_CIRCUMFLEX = r'\^'
t_TILDE = r'~'
t_AT = r'@'
#similarly we need to add other keywords and way to handle variable names. (Presently showing Illegal)

# A regular expression rule with some action code

#ignore comments in source code
def t_comment(t):
	r"[ ]*\043[^\n]*"
	pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

#brackets and quotes
#'LPAR','RPAR','LBRACE','RBRACE','LSQB','RSQB'
#'COLON', 'SQUOTE','DQUOTE',
t_SQUOTE  = r"'"
t_DQUOTE  = r'"'

Bracketing_flag = 0
def t_LPAR(t):
	r'\('
	global Bracketing_flag
	Bracketing_flag+=1
	return t
def t_RPAR(t):
	r'\)'
	global Bracketing_flag
	Bracketing_flag-=1
	return t
def t_LBRACE(t):
	r'\{'
	global Bracketing_flag
	Bracketing_flag+=1
	return t
def t_RBRACE(t):
	r'\}'
	global Bracketing_flag
	Bracketing_flag-=1
	return t
def t_LSQB(t):
	r'\['
	global Bracketing_flag
	Bracketing_flag+=1
	return t
def t_RSQB(t):
	r'\]'
	global Bracketing_flag
	Bracketing_flag-=1
	return t


# Indent
Indent_flag = True
def t_INDENT(t):
	r'[ \t]+'
	#have to assign value, depending upon number spaces and tabs
	#remove cases for balnk line
	global Indent_flag
	if  Indent_flag == True :
		Indent_flag = False
		return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    #next white sapces will be indentation
    #have to check if this new line is between ' or " or ( or {  or [
    # then ignore is 
    if Bracketing_flag > 0:
    	return
    global Indent_flag
    Indent_flag = True
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces)
def t_NAME(t):
	r"[a-zA-Z_][a-zA-Z0-9_]*"
	t.type = RESERVED.get(t.value, "NAME")
	return t


# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
# get from command line arg
data = open('../test/test2.py')
data = data.read()
lexer.input(data)
printableToken =[]
#Tokenize
tok = lexer.token()
while True:
	if(not tok):
		break
	lineNo = tok.lineno
	#indatation
	global Indent_flag
	Indent_flag =  False
	startToken = tok.value
	printableToken[:] = []
	while(lineNo==tok.lineno):
		printableToken.append(tok.type)
		print tok.value,
		tok = lexer.token()
		if(not tok):
			break
	print "\n#", # improve this
	for t in printableToken:
		print t,
	print ""