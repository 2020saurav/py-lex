import lex
from lex import TOKEN

tokens=[]
keywordlist = [
				'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 
				'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 
				'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 
				'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 
				'with', 'yield'
				]
RESERVED = {}
for keyword in keywordlist:
	name = keyword.upper()
	RESERVED[keyword] = name
	tokens.append(name)

# TODO : ADD MORE TOKENS
tokens = tuple(tokens) + (
				'ARROW','EQEQUAL','NOTEQUAL','LESSEQUAL','LEFTSHIFT','GREATEREQUAL',
				'RIGHTSHIFT','PLUSEQUAL','MINEQUAL','STAREQUAL','SLASHEQUAL','PERCENTEQUAL',
				'COLON','COMMA','SEMI','PLUS','MINUS','STAR','SLASH','VBAR','AMPER','LESS',
				'GREATER','EQUAL','DOT','PERCENT','BACKQUOTE','CIRCUMFLEX','TILDE',	'AT',

			    'LPAREN', 'RPAREN',
			    'LBRACE', 'RBRACE',
			    'LSQB', 'RSQB',
				'NEWLINE','NUMBER','NAME',
				'INDENT',
				'STRING', 'TRIPLESTRING'
	)

# All tokens defined by functions are added in the same order as they appear in the lexer file.
# Tokens defined by strings are added next by sorting them in order of decreasing regular expression length (longer expressions are added first).
# Order important. Match '==' before '=', so put '==' before
# Regular expression rules for simple tokens
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



def t_LPAREN(t):
	r"\("
	t.lexer.parenthesisCount+=1
	return t
def t_RPAREN(t):
	r"\)"
	t.lexer.parenthesisCount-=1
	return t
def t_LBRACE(t):
	r"\{"
	t.lexer.parenthesisCount+=1
	return t
def t_RBRACE(t):
	r"\}"
	t.lexer.parenthesisCount-=1
	return t
def t_LSQB(t):
	r"\["
	t.lexer.parenthesisCount+=1
	return t
def t_RSQB(t):
	r"\]"
	t.lexer.parenthesisCount-=1
	return t

#ignore comments in source code
def t_comment(t):
	r"[ ]*\043[^\n]*"
	pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t
def t_TRIPLESTRING(t):
	r'(\"\"\"(\\.|[^"])*\"\"\") | (\'\'\'(\\.|[^"])*\'\'\')'
	return t
def t_STRING(t):
	r'(\"(\\.|[^"])*\") | (\'(\\.|[^"])*\')'
	return t

# Indent
# CANNOT HANDLE INDENTATIONS THIS WAY
# READ https://docs.python.org/2/reference/lexical_analysis.html FOR DETAILS
# CONVERT TABS TO SPACES AND MAINTAIN STACK OF INDENTATION COUNT AS SUGGESTED!  1 Tab = 8 spaces

def t_INDENT(t):
	r'\t'
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = "NEWLINE"
    if(t.lexer.parenthesisCount == 0):
    	return t

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
lexer.parenthesisCount = 0
# get from command line arg
data = open('../test/test4.py')
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
		print "#", # improve this
		for t in printableToken:
			print t,
	print ""


# Tabs : replace by 8 spaces and then compute Indentations
# Handle all types of comments
# Handle \ on line continutation, no comment continutation using \ (implicit and explicit line join using \)
# Implit line join, immaterial whit spaces in between 2.1.6
# 2.1.8 about indentations



# HANDLE  4. brackets  5. indent dedent  
# 6. string with rRuU prefix!https://docs.python.org/2.0/ref/strings.html
# escaped new line in both single quote, triple quote
# floating, complex numbers
#error reporting