import lex
#List of token names

tokens = (
	'NUMBER',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'LPAREN',
	'RPAREN',
	'FUNCTIONSTART',
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
t_FUNCTIONSTART = r'def'
#similarly we need to add other keywords and way to handle variable names. (Presently showing Illegal)

# A regular expression rule with some action code
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

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#Data
# data = '''
# 3 + 4 * 10
#   + -20 *2
# '''
data = open('../test/test1.py')
data = data.read()
lexer.input(data)

#Tokenize
while True:
	tok = lexer.token()
	if (not tok):
		break # no more input
	print tok.type, tok.value, tok.lineno, tok.lexpos," \t\t" ,tok
