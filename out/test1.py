def foo ( a ) : 		# DEF NAME LPAREN NAME RPAREN COLON 
	print a 		# INDENT PRINT NAME 
def main ( ) : 		# DEF NAME LPAREN RPAREN COLON 
	a = 42 		# INDENT NAME EQUAL NUMBER 
	foo (a) 		# INDENT NAME LPAREN NAME RPAREN 
			# INDENT 
if __name__ == '__main__' : 		# IF NAME EQEQUAL SQUOTE NAME SQUOTE COLON 
	main () 
