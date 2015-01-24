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

# TODO : ADD MORE TOKENS
tokens = tuple(tokens) + (
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
	'LPAREN', 'RPAREN',
	'EQEQUAL','EQUAL',
	'COLON', 'SQUOTE','DQUOTE',
	'NEWLINE','NUMBER','NAME',
	'INDENT',
	)

# All tokens defined by functions are added in the same order as they appear in the lexer file.
# Tokens defined by strings are added next by sorting them in order of decreasing regular expression length (longer expressions are added first).
# Order important. Match '==' before '=', so put '==' before
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQEQUAL = r'=='
t_EQUAL   = r'='
t_COLON   = r'\:'
t_SQUOTE  = r"'"
t_DQUOTE  = r'"'
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
# Indent
# CANNOT HANDLE INDENTATIONS THIS WAY
# READ https://docs.python.org/2/reference/lexical_analysis.html FOR DETAILS
# CONVERT TABS TO SPACES AND MAINTAIN STACK OF INDENTATION COUNT AS SUGGESTED!

def t_INDENT(t):
	r'\t'
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces)
t_ignore  = ' '
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
data = open('../test/test1.py')
data = data.read()
lexer.input(data)
printableToken =[]
#Tokenize
tok = lexer.token()
while True:
	if(not tok):
		break
	lineNo = tok.lineno
	startToken = tok.value
	printableToken[:] = []
	while(lineNo==tok.lineno):
		printableToken.append(tok.type)
		print tok.value,
		tok = lexer.token()
		if(not tok):
			break
	if(tok):
		print "\n#", # improve this
		for t in printableToken:
			print t,
	print "\n"


# Tabs : replace by 8 spaces and then compute Indentations
# Handle all types of comments
# Handle \ on line continutation, no comment continutation using \ (implicit and explicit line join using \)
# Implit line join, immaterial whit spaces in between 2.1.6
# 2.1.8 about indentations
