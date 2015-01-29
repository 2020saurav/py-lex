def foo ( a ) : # DEF NAME LPAREN NAME RPAREN COLON 
	print a # PRINT NAME 
	print "fo \n o bar" # PRINT STRING 
	s = [ "this" , # NAME EQUAL LSQB STRING COMMA 
	"is" , # STRING COMMA 
	"not" , # STRING COMMA 
	"new" , # STRING COMMA 
	"line" ] # STRING RSQB 
def main ( ) : # DEF NAME LPAREN RPAREN COLON 
	a = - 420.03 # NAME EQUAL MINUS FNUMBER 
	b = 43 # NAME EQUAL NUMBER 
	foo ( a ) # NAME LPAREN NAME RPAREN 
	if a < 3 : # IF NAME LESS NUMBER COLON 
		print "indented ' test ' anything ' \" some random" # PRINT STRING 
		print 'by tabs" test " anything \' some fer r r " " " " th' # PRINT STRING 
if __name__ == '__main__' : # IF NAME EQEQUAL STRING COLON 
	main ( ) # NAME LPAREN RPAREN 
