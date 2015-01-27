def   foo ( a ) : 
# DEF WS NAME LPAREN NAME RPAREN COLON NEWLINE 
         print   a 

# WS PRINT WS NAME NEWLINE 
def   main ( ) : 
# DEF WS NAME LPAREN RPAREN COLON NEWLINE 
         a   =   42 
# WS NAME WS EQUAL WS NUMBER NEWLINE 
         arr   =   [ 43 , 34 , # WS NAME WS EQUAL WS LSQB NUMBER COMMA NUMBER COMMA 
85 , # NUMBER COMMA 
89 , # NUMBER COMMA 
77 # NUMBER 
] 
# RSQB NEWLINE 
         foo ( a ) 
# WS NAME LPAREN NAME RPAREN NEWLINE 
         b   =   "my name is\np ksaurav" 
# WS NAME WS EQUAL WS STRING NEWLINE 
         print   b 
# WS PRINT WS NAME NEWLINE 
         

# WS NEWLINE 
if   __name__ == '__main__' : 
# IF WS NAME EQEQUAL STRING COLON NEWLINE 
         main ( ) 
