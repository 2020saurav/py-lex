import sys 
# IMPORT NAME 
import lex 
# IMPORT NAME 
from lex import TOKEN 
# FROM NAME IMPORT NAME 
import tokenize 
# IMPORT NAME 
NO_INDENT = 0 
# NAME EQUAL NUMBER 
MAY_INDENT = 1 
# NAME EQUAL NUMBER 
MUST_INDENT = 2 
# NAME EQUAL NUMBER 
tokens = [ ] 
# NAME EQUAL LSQB RSQB 
keywordlist = [ 
# NAME EQUAL LSQB 
'and' , 'as' , 'assert' , 'break' , 'class' , 'continue' , 'def' , 
# STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA 
'del' , 'elif' , 'else' , 'except' , 'exec' , 'finally' , 'for' , 
# STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA 
'from' , 'global' , 'if' , 'import' , 'in' , 'is' , 'lambda' , 'not' , 
# STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA 
'or' , 'pass' , 'print' , 'raise' , 'return' , 'try' , 'while' , 
# STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA 
'with' , 'yield' 
# STRING COMMA STRING 
] 
# RSQB 
RESERVED = { } 
# NAME EQUAL LBRACE RBRACE 
for keyword in keywordlist : 
# FOR NAME IN NAME COLON 
	name = keyword . upper ( ) 
	# NAME EQUAL NAME DOT NAME LPAREN RPAREN 
	RESERVED [ keyword ] = name 
	# NAME LSQB NAME RSQB EQUAL NAME 
	tokens . append ( name ) 
	# NAME DOT NAME LPAREN NAME RPAREN 
tokens = tuple ( tokens ) + ( 
# NAME EQUAL NAME LPAREN NAME RPAREN PLUS LPAREN 
'ARROW' , 'EQEQUAL' , 'NOTEQUAL' , 'LESSEQUAL' , 'LEFTSHIFT' , 'GREATEREQUAL' , 
# STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA 
'RIGHTSHIFT' , 'PLUSEQUAL' , 'MINEQUAL' , 'STAREQUAL' , 'SLASHEQUAL' , 'PERCENTEQUAL' , 
# STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA 
'COLON' , 'COMMA' , 'SEMI' , 'PLUS' , 'MINUS' , 'STAR' , 'SLASH' , 'VBAR' , 'AMPER' , 'LESS' , 
# STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA 
'GREATER' , 'EQUAL' , 'DOT' , 'PERCENT' , 'BACKQUOTE' , 'CIRCUMFLEX' , 'TILDE' , 'AT' , 
# STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA STRING COMMA 
'LPAREN' , 'RPAREN' , 
# STRING COMMA STRING COMMA 
'LBRACE' , 'RBRACE' , 
# STRING COMMA STRING COMMA 
'LSQB' , 'RSQB' , 
# STRING COMMA STRING COMMA 
'NEWLINE' , 
# STRING COMMA 
'FNUMBER' , 'NUMBER' , 
# STRING COMMA STRING COMMA 
'INDENT' , 'DEDENT' , 
# STRING COMMA STRING COMMA 
'TRIPLESTRING' , 'STRING' , 
# STRING COMMA STRING COMMA 
'RAWSTRING' , 'UNICODESTRING' , 
# STRING COMMA STRING COMMA 
'NAME' , 'WS' 
# STRING COMMA STRING 
) 
# RPAREN 
t_ARROW = '->' 
# NAME EQUAL STRING 
t_EQEQUAL = r'==' 
# NAME EQUAL RAWSTRING 
t_NOTEQUAL = r'!=' 
# NAME EQUAL RAWSTRING 
t_LESSEQUAL = r'<=' 
# NAME EQUAL RAWSTRING 
t_LEFTSHIFT = r'<<' 
# NAME EQUAL RAWSTRING 
t_GREATEREQUAL = r'>=' 
# NAME EQUAL RAWSTRING 
t_RIGHTSHIFT = r'>>' 
# NAME EQUAL RAWSTRING 
t_PLUSEQUAL = r'\+=' 
# NAME EQUAL RAWSTRING 
t_MINEQUAL = r'-=' 
# NAME EQUAL RAWSTRING 
t_STAREQUAL = r'\*=' 
# NAME EQUAL RAWSTRING 
t_SLASHEQUAL = r'/=' 
# NAME EQUAL RAWSTRING 
t_PERCENTEQUAL = r'%=' 
# NAME EQUAL RAWSTRING 
t_COLON = r':' 
# NAME EQUAL RAWSTRING 
t_COMMA = r',' 
# NAME EQUAL RAWSTRING 
t_SEMI = r';' 
# NAME EQUAL RAWSTRING 
t_PLUS = r'\+' 
# NAME EQUAL RAWSTRING 
t_MINUS = r'-' 
# NAME EQUAL RAWSTRING 
t_STAR = r'\*' 
# NAME EQUAL RAWSTRING 
t_SLASH = r'/' 
# NAME EQUAL RAWSTRING 
t_VBAR = r'\|' 
# NAME EQUAL RAWSTRING 
t_AMPER = r'&' 
# NAME EQUAL RAWSTRING 
t_LESS = r'<' 
# NAME EQUAL RAWSTRING 
t_GREATER = r'>' 
# NAME EQUAL RAWSTRING 
t_EQUAL = r'=' 
# NAME EQUAL RAWSTRING 
t_DOT = r'\.' 
# NAME EQUAL RAWSTRING 
t_PERCENT = r'%' 
# NAME EQUAL RAWSTRING 
t_BACKQUOTE = r'`' 
# NAME EQUAL RAWSTRING 
t_CIRCUMFLEX = r'\^' 
# NAME EQUAL RAWSTRING 
t_TILDE = r'~' 
# NAME EQUAL RAWSTRING 
t_AT = r'@' 
# NAME EQUAL RAWSTRING 
def newToken ( newType , lineno ) : 
# DEF NAME LPAREN NAME COMMA NAME RPAREN COLON 
	tok = lex . LexToken ( ) 
	# NAME EQUAL NAME DOT NAME LPAREN RPAREN 
	tok . type = newType 
	# NAME DOT NAME EQUAL NAME 
	tok . value = None 
	# NAME DOT NAME EQUAL NAME 
	tok . lineno = lineno 
	# NAME DOT NAME EQUAL NAME 
	tok . lexpos = - 100 
	# NAME DOT NAME EQUAL MINUS NUMBER 
	return tok 
	# RETURN NAME 
def t_LPAREN ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r"\(" 
	# RAWSTRING 
	t . lexer . parenthesisCount += 1 
	# NAME DOT NAME DOT NAME PLUSEQUAL NUMBER 
	return t 
	# RETURN NAME 
def t_RPAREN ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r"\)" 
	# RAWSTRING 
	t . lexer . parenthesisCount -= 1 
	# NAME DOT NAME DOT NAME MINEQUAL NUMBER 
	return t 
	# RETURN NAME 
def t_LBRACE ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r"\{" 
	# RAWSTRING 
	t . lexer . parenthesisCount += 1 
	# NAME DOT NAME DOT NAME PLUSEQUAL NUMBER 
	return t 
	# RETURN NAME 
def t_RBRACE ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r"\}" 
	# RAWSTRING 
	t . lexer . parenthesisCount -= 1 
	# NAME DOT NAME DOT NAME MINEQUAL NUMBER 
	return t 
	# RETURN NAME 
def t_LSQB ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r"\[" 
	# RAWSTRING 
	t . lexer . parenthesisCount += 1 
	# NAME DOT NAME DOT NAME PLUSEQUAL NUMBER 
	return t 
	# RETURN NAME 
def t_RSQB ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r"\]" 
	# RAWSTRING 
	t . lexer . parenthesisCount -= 1 
	# NAME DOT NAME DOT NAME MINEQUAL NUMBER 
	return t 
	# RETURN NAME 
def t_comment ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r"[ ]*\043[^\n]*" 
	# RAWSTRING 
	pass 
	# PASS 
@ TOKEN ( tokenize . Floatnumber ) 
# AT NAME LPAREN NAME DOT NAME RPAREN 
def t_FNUMBER ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	return t 
	# RETURN NAME 
def t_NUMBER ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r'\d+' 
	# RAWSTRING 
	t . value = int ( t . value ) 
	# NAME DOT NAME EQUAL NAME LPAREN NAME DOT NAME RPAREN 
	return t 
	# RETURN NAME 
def t_TRIPLESTRING ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r'"{3}([\s\S]*?"{3}) | \'{3}([\s\S]*?\'{3})' 
	# RAWSTRING 
	return t 
	# RETURN NAME 
def t_RAWSTRING ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r'[rR](\"(\\.|[^\"])*\") | [rR](\'(\\.|[^\'])*\')' 
	# RAWSTRING 
	return t 
	# RETURN NAME 
def t_UNICODESTRING ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r'[uU](\"(\\.|[^\"])*\") | [uU](\'(\\.|[^\'])*\')' 
	# RAWSTRING 
	return t 
	# RETURN NAME 
def t_STRING ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r'(\"(\\.|[^\"])*\") | (\'(\\.|[^\'])*\')' 
	# RAWSTRING 
	return t 
	# RETURN NAME 
def t_newline ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r'\n+' 
	# RAWSTRING 
	t . lexer . lineno += len ( t . value ) 
	# NAME DOT NAME DOT NAME PLUSEQUAL NAME LPAREN NAME DOT NAME RPAREN 
	t . type = "NEWLINE" 
	# NAME DOT NAME EQUAL STRING 
	if ( t . lexer . parenthesisCount == 0 ) : 
	# IF LPAREN NAME DOT NAME DOT NAME EQEQUAL NUMBER RPAREN COLON 
		return t 
		# RETURN NAME 
def t_NAME ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r"[a-zA-Z_][a-zA-Z0-9_]*" 
	# RAWSTRING 
	t . type = RESERVED . get ( t . value , "NAME" ) 
	# NAME DOT NAME EQUAL NAME DOT NAME LPAREN NAME DOT NAME COMMA STRING RPAREN 
	return t 
	# RETURN NAME 
def t_error ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	print "\nERROR: Illegal character '%s' in %s" % ( t . value [ 0 ] , t . value ) 
	# PRINT STRING PERCENT LPAREN NAME DOT NAME LSQB NUMBER RSQB COMMA NAME DOT NAME RPAREN 
	t . lexer . skip ( 1 ) 
	# NAME DOT NAME DOT NAME LPAREN NUMBER RPAREN 
def t_WS ( t ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	r" [ \t\f]+ " 
	# RAWSTRING 
	value = t . value 
	# NAME EQUAL NAME DOT NAME 
	value = value . rsplit ( "\f" , 1 ) [ - 1 ] 
	# NAME EQUAL NAME DOT NAME LPAREN STRING COMMA NUMBER RPAREN LSQB MINUS NUMBER RSQB 
	pos = 0 
	# NAME EQUAL NUMBER 
	while True : 
	# WHILE NAME COLON 
		pos = value . find ( "\t" ) 
		# NAME EQUAL NAME DOT NAME LPAREN STRING RPAREN 
		if pos == - 1 : 
		# IF NAME EQEQUAL MINUS NUMBER COLON 
			break 
			# BREAK 
		n = 8 - ( pos % 8 ) 
		# NAME EQUAL NUMBER MINUS LPAREN NAME PERCENT NUMBER RPAREN 
		value = value [ : pos ] + " " * n + value [ pos + 1 : ] 
		# NAME EQUAL NAME LSQB COLON NAME RSQB PLUS STRING STAR NAME PLUS NAME LSQB NAME PLUS NUMBER COLON RSQB 
	t . value = value 
	# NAME DOT NAME EQUAL NAME 
	if t . lexer . at_line_start and t . lexer . parenthesisCount == 0 : 
	# IF NAME DOT NAME DOT NAME AND NAME DOT NAME DOT NAME EQEQUAL NUMBER COLON 
		return t 
		# RETURN NAME 
def INDENT ( lineno ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	return newToken ( "INDENT" , lineno ) 
	# RETURN NAME LPAREN STRING COMMA NAME RPAREN 
def DEDENT ( lineno ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	return newToken ( "DEDENT" , lineno ) 
	# RETURN NAME LPAREN STRING COMMA NAME RPAREN 
def annotate_indentation_state ( lexer , token_stream ) : 
# DEF NAME LPAREN NAME COMMA NAME RPAREN COLON 
	lexer . at_line_start = at_line_start = True 
	# NAME DOT NAME EQUAL NAME EQUAL NAME 
	indent = NO_INDENT 
	# NAME EQUAL NAME 
	saw_colon = False 
	# NAME EQUAL NAME 
	for token in token_stream : 
	# FOR NAME IN NAME COLON 
		token . at_line_start = at_line_start 
		# NAME DOT NAME EQUAL NAME 
		if token . type == "ARROW" : 
		# IF NAME DOT NAME EQEQUAL STRING COLON 
			at_line_start = False 
			# NAME EQUAL NAME 
			indent = MAY_INDENT 
			# NAME EQUAL NAME 
			token . must_indent = False 
			# NAME DOT NAME EQUAL NAME 
		elif token . type == "COLON" : 
		# ELIF NAME DOT NAME EQEQUAL STRING COLON 
			at_line_start = False 
			# NAME EQUAL NAME 
			indent = MAY_INDENT 
			# NAME EQUAL NAME 
			token . must_indent = False 
			# NAME DOT NAME EQUAL NAME 
		elif token . type == "NEWLINE" : 
		# ELIF NAME DOT NAME EQEQUAL STRING COLON 
			at_line_start = True 
			# NAME EQUAL NAME 
			if indent == MAY_INDENT : 
			# IF NAME EQEQUAL NAME COLON 
				indent = MUST_INDENT 
				# NAME EQUAL NAME 
			token . must_indent = False 
			# NAME DOT NAME EQUAL NAME 
		elif token . type == "WS" : 
		# ELIF NAME DOT NAME EQEQUAL STRING COLON 
			assert token . at_line_start == True 
			# ASSERT NAME DOT NAME EQEQUAL NAME 
			at_line_start = True 
			# NAME EQUAL NAME 
			token . must_indent = False 
			# NAME DOT NAME EQUAL NAME 
		else : 
		# ELSE COLON 
			if indent == MUST_INDENT : 
			# IF NAME EQEQUAL NAME COLON 
				token . must_indent = True 
				# NAME DOT NAME EQUAL NAME 
			else : 
			# ELSE COLON 
				token . must_indent = False 
				# NAME DOT NAME EQUAL NAME 
			at_line_start = False 
			# NAME EQUAL NAME 
			indent = NO_INDENT 
			# NAME EQUAL NAME 
		yield token 
		# YIELD NAME 
		lexer . at_line_start = at_line_start 
		# NAME DOT NAME EQUAL NAME 
def synthesize_indentation_tokens ( token_stream ) : 
# DEF NAME LPAREN NAME RPAREN COLON 
	levels = [ 0 ] 
	# NAME EQUAL LSQB NUMBER RSQB 
	token = None 
	# NAME EQUAL NAME 
	depth = 0 
	# NAME EQUAL NUMBER 
	prev_was_ws = False 
	# NAME EQUAL NAME 
	for token in token_stream : 
	# FOR NAME IN NAME COLON 
		if token . type == "WS" : 
		# IF NAME DOT NAME EQEQUAL STRING COLON 
			assert depth == 0 
			# ASSERT NAME EQEQUAL NUMBER 
			depth = len ( token . value ) 
			# NAME EQUAL NAME LPAREN NAME DOT NAME RPAREN 
			prev_was_ws = True 
			# NAME EQUAL NAME 
			continue 
			# CONTINUE 
		if token . type == "NEWLINE" : 
		# IF NAME DOT NAME EQEQUAL STRING COLON 
			depth = 0 
			# NAME EQUAL NUMBER 
			if prev_was_ws or token . at_line_start : 
			# IF NAME OR NAME DOT NAME COLON 
				continue 
				# CONTINUE 
			yield token 
			# YIELD NAME 
			continue 
			# CONTINUE 
		prev_was_ws = False 
		# NAME EQUAL NAME 
		if token . must_indent : 
		# IF NAME DOT NAME COLON 
			if not ( depth > levels [ - 1 ] ) : 
			# IF NOT LPAREN NAME GREATER NAME LSQB MINUS NUMBER RSQB RPAREN COLON 
				print "Expected an indented block" , token 
				# PRINT STRING COMMA NAME 
			levels . append ( depth ) 
			# NAME DOT NAME LPAREN NAME RPAREN 
			yield INDENT ( token . lineno ) 
			# YIELD NAME LPAREN NAME DOT NAME RPAREN 
		elif token . at_line_start : 
		# ELIF NAME DOT NAME COLON 
			if depth == levels [ - 1 ] : 
			# IF NAME EQEQUAL NAME LSQB MINUS NUMBER RSQB COLON 
				pass 
				# PASS 
			elif depth > levels [ - 1 ] : 
			# ELIF NAME GREATER NAME LSQB MINUS NUMBER RSQB COLON 
				print "Unexpected indent" , token 
				# PRINT STRING COMMA NAME 
			else : 
			# ELSE COLON 
				try : 
				# TRY COLON 
					i = levels . index ( depth ) 
					# NAME EQUAL NAME DOT NAME LPAREN NAME RPAREN 
				except ValueError : 
				# EXCEPT NAME COLON 
					print "Unindent does not match" , token 
					# PRINT STRING COMMA NAME 
				for z in range ( i + 1 , len ( levels ) ) : 
				# FOR NAME IN NAME LPAREN NAME PLUS NUMBER COMMA NAME LPAREN NAME RPAREN RPAREN COLON 
					yield DEDENT ( token . lineno ) 
					# YIELD NAME LPAREN NAME DOT NAME RPAREN 
					levels . pop ( ) 
					# NAME DOT NAME LPAREN RPAREN 
		yield token 
		# YIELD NAME 
	if len ( levels ) > 1 : 
	# IF NAME LPAREN NAME RPAREN GREATER NUMBER COLON 
		assert token is not None 
		# ASSERT NAME IS NOT NAME 
		for z in range ( 1 , len ( levels ) ) : 
		# FOR NAME IN NAME LPAREN NUMBER COMMA NAME LPAREN NAME RPAREN RPAREN COLON 
			yield DEDENT ( token . lineno ) 
			# YIELD NAME LPAREN NAME DOT NAME RPAREN 
def printTokenized ( filename , tok ) : 
# DEF NAME LPAREN NAME COMMA NAME RPAREN COLON 
	sourcefile = open ( filename ) 
	# NAME EQUAL NAME LPAREN NAME RPAREN 
	printableToken = [ ] 
	# NAME EQUAL LSQB RSQB 
	indentlevel = 0 
	# NAME EQUAL NUMBER 
	while True : 
	# WHILE NAME COLON 
		if ( not tok ) : 
		# IF LPAREN NOT NAME RPAREN COLON 
			break 
			# BREAK 
		if ( tok . type == "INDENT" ) : 
		# IF LPAREN NAME DOT NAME EQEQUAL STRING RPAREN COLON 
			indentlevel += 1 
			# NAME PLUSEQUAL NUMBER 
			tok = token_stream . next ( ) 
			# NAME EQUAL NAME DOT NAME LPAREN RPAREN 
			continue 
			# CONTINUE 
		elif ( tok . type == "DEDENT" ) : 
		# ELIF LPAREN NAME DOT NAME EQEQUAL STRING RPAREN COLON 
			indentlevel -= 1 
			# NAME MINEQUAL NUMBER 
			tok = token_stream . next ( ) 
			# NAME EQUAL NAME DOT NAME LPAREN RPAREN 
			continue 
			# CONTINUE 
		if ( indentlevel > 0 ) : 
		# IF LPAREN NAME GREATER NUMBER RPAREN COLON 
			print "\t" * indentlevel , 
			# PRINT STRING STAR NAME COMMA 
		lineNo = tok . lineno 
		# NAME EQUAL NAME DOT NAME 
		printableToken [ : ] = [ ] 
		# NAME LSQB COLON RSQB EQUAL LSQB RSQB 
		while ( lineNo == tok . lineno ) : 
		# WHILE LPAREN NAME EQEQUAL NAME DOT NAME RPAREN COLON 
			if ( tok . type != "INDENT" and tok . type != "DEDENT" and tok . type != "NEWLINE" ) : 
			# IF LPAREN NAME DOT NAME NOTEQUAL STRING AND NAME DOT NAME NOTEQUAL STRING AND NAME DOT NAME NOTEQUAL STRING RPAREN COLON 
				printableToken . append ( tok . type ) 
				# NAME DOT NAME LPAREN NAME DOT NAME RPAREN 
				print tok . value , 
				# PRINT NAME DOT NAME COMMA 
			try : 
			# TRY COLON 
				tok = token_stream . next ( ) 
				# NAME EQUAL NAME DOT NAME LPAREN RPAREN 
			except : 
			# EXCEPT COLON 
				tok = 0 
				# NAME EQUAL NUMBER 
			if ( not tok ) : 
			# IF LPAREN NOT NAME RPAREN COLON 
				break 
				# BREAK 
		print "" 
		# PRINT STRING 
		if ( indentlevel > 0 ) : 
		# IF LPAREN NAME GREATER NUMBER RPAREN COLON 
			print "\t" * indentlevel , 
			# PRINT STRING STAR NAME COMMA 
		print "#" , 
		# PRINT STRING COMMA 
		for t in printableToken : 
		# FOR NAME IN NAME COLON 
			print t , 
			# PRINT NAME COMMA 
		print "" 
		# PRINT STRING 
lexer = lex . lex ( ) 
# NAME EQUAL NAME DOT NAME LPAREN RPAREN 
lexer . parenthesisCount = 0 
# NAME DOT NAME EQUAL NUMBER 
filename = 'saurav.py' 
# NAME EQUAL STRING 
sourcefile = open ( filename ) 
# NAME EQUAL NAME LPAREN NAME RPAREN 
data = sourcefile . read ( ) 
# NAME EQUAL NAME DOT NAME LPAREN RPAREN 
lexer . input ( data ) 
# NAME DOT NAME LPAREN NAME RPAREN 
token_stream = iter ( lexer . token , None ) 
# NAME EQUAL NAME LPAREN NAME DOT NAME COMMA NAME RPAREN 
token_stream = annotate_indentation_state ( lexer , token_stream ) 
# NAME EQUAL NAME LPAREN NAME COMMA NAME RPAREN 
token_stream = synthesize_indentation_tokens ( token_stream ) 
# NAME EQUAL NAME LPAREN NAME RPAREN 
tok = token_stream . next ( ) 
# NAME EQUAL NAME DOT NAME LPAREN RPAREN 
printTokenized ( filename , tok ) 
# NAME LPAREN NAME COMMA NAME RPAREN 
