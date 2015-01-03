import lex

tokens=[]
keywordlist = ['and', 'break', 'class', 'continue', 
              'elif', 'else', 'for',
              'if', 'import', 'in', 
              'not', 'or', 'print', 'return', 
              'while',]
RESERVED = {}
for keyword in keywordlist:
	name = keyword.upper()
	RESERVED[keyword] = name
	tokens.append(name)

tokens = tuple(tokens) + (
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
	'LPAREN', 'RPAREN',
	'EQEQUAL','EQUAL',
	'COLON', 'SQUOTE','DQUOTE',
	'NEWLINE','NUMBER','NAME')

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

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
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

#Tokenize
while True:
	tok = lexer.token()
	if (not tok):
		break # no more input
	print tok.value,"\t\t\t", tok.type,  tok.lineno, tok.lexpos
