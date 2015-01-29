def foo ( a ) : # DEF NAME LPAREN NAME RPAREN COLON 
	print a # PRINT NAME 
	print a + 1 # PRINT NAME PLUS NUMBER 
def main ( ) : # DEF NAME LPAREN RPAREN COLON 
	a = 42 # NAME EQUAL NUMBER 
	arr = [ 43 , 34 , # NAME EQUAL LSQB NUMBER COMMA NUMBER COMMA 
	85 , # NUMBER COMMA 
	89 , # NUMBER COMMA 
	77 # NUMBER 
	] # RSQB 
	foo ( a ) # NAME LPAREN NAME RPAREN 
	b = "my name is\np ksaurav" # NAME EQUAL STRING 
	print b # PRINT NAME 
if __name__ == '__main__' : # IF NAME EQEQUAL STRING COLON 
	main ( ) # NAME LPAREN RPAREN 
