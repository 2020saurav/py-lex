import lex
from lex import TOKEN
import tokenize

NO_INDENT = 0
MAY_INDENT = 1
MUST_INDENT = 2

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

tokens = tuple(tokens) + (
				'ARROW','EQEQUAL','NOTEQUAL','LESSEQUAL','LEFTSHIFT','GREATEREQUAL',
				'RIGHTSHIFT','PLUSEQUAL','MINEQUAL','STAREQUAL','SLASHEQUAL','PERCENTEQUAL',
				'COLON','COMMA','SEMI','PLUS','MINUS','STAR','SLASH','VBAR','AMPER','LESS',
				'GREATER','EQUAL','DOT','PERCENT','BACKQUOTE','CIRCUMFLEX','TILDE',	'AT',

			    'LPAREN', 'RPAREN',
			    'LBRACE', 'RBRACE',
			    'LSQB', 'RSQB',
				'NEWLINE',
				'FNUMBER', 'NUMBER',
				'NAME',
				'INDENT', 'DEDENT',
				'STRING', 'TRIPLESTRING',
				"WS"
	)

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

@TOKEN(tokenize.Floatnumber)
def t_FLOAT_NUMBER(t):
    t.type = "FNUMBER"
    # t.value = (float(t.value), t.value)
    return t
# FP number above integers    
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

# def t_INDENT(t):
# 	r'\t'
# 	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = "NEWLINE"
    if(t.lexer.parenthesisCount == 0):
    	return t

# A string containing ignored characters (spaces)
# t_ignore  = ' '
def t_NAME(t):
	r"[a-zA-Z_][a-zA-Z0-9_]*"
	t.type = RESERVED.get(t.value, "NAME")
	return t


# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# WHITESPACE

def t_WS(t):
	r" [ \t\f]+ "
	value = t.value
	value = value.rsplit("\f", 1)[-1]
	pos = 0
	while True:
		pos = value.find("\t")
		if pos == -1:
			break
		n = 8 - (pos % 8)
		value = value[:pos] + " "*n + value[pos+1:]
	t.value = value
	if t.lexer.parenthesisCount == 0:
		return t
def annotate_indentation_state(lexer, token_stream):
	lexer.at_line_start = at_line_start = True
	indent = NO_INDENT
	saw_colon = False
	for token in token_stream:
		token.at_line_start = at_line_start
		if token.type == "ARROW":
			at_line_start = False
			indent = MAY_INDENT
			token.must_indent = False
		elif token.type == "COLON":
			at_line_start = False
			indent = MAY_INDENT
			token.must_indent = False
		elif token.type == "NEWLINE":
			at_line_start = True
			if indent == MAY_INDENT:
				indent = MUST_INDENT
			token.must_indent = False
		elif token.type == "WS":
			assert token.at_line_start == True
			at_line_start = True
			token.must_indent = False
		else:
			if indent == MUST_INDENT:
				token.must_indent = True
			else:
				token.must_indent = False
			at_line_start = False
			indent = NO_INDENT

		yield token
		lexer.at_line_start = at_line_start

def synthesize_indentation_tokens(token_stream):
	levels = [0]
	token = None
	depth = 0
	prev_was_ws = False
	for token in token_stream:
		if token.type == "WS":
			assert depth == 0
			depth = len(token.value)
			prev_was_ws = True
			continue
		if token.type == "NEWLINE":
			depth = 0
			if prev_was_ws or token.at_line_start:
				continue
			yield token
			continue
		prev_was_ws = False
		if token.must_indent:
			if not (depth > levels[-1]):
				print "Expected an indented block", token
			levels.append(depth)
			yield INDENT(token.lineno)
		elif token.at_line_start:
			if depth == levels[-1]:
				pass
			elif depth > levels[-1]:
				print "Unexpected indent", token
			else:
				try:
					i = levels.index(depth)
				except ValueError:
					print "Unindent does not match", token
				for z in range(i+1, len(levels)):
					yield DEDENT(token.lineno)
					levels.pop()
		yield token
	if len(levels) > 1:
		assert token is not None
		for z in range(1, len(levels)):
			yield DEDENT(token.lineno)


# Build the lexer
lexer = lex.lex()
lexer.parenthesisCount = 0
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
		print "#", # improve this
		for t in printableToken:
			print t,
	print ""


# Tabs : replace by 8 spaces and then compute Indentations
# Handle all types of comments
# Handle \ on line continutation, no comment continutation using \ (implicit and explicit line join using \)
# Implit line join, immaterial whit spaces in between 2.1.6
# 2.1.8 about indentations



# HANDLE   5. indent dedent  
# 6. string with rRuU prefix!https://docs.python.org/2.0/ref/strings.html

#  complex numbers
#error reporting