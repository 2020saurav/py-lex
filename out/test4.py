a = """ Testing a 3 \
			quote string with tabs preserved""" 
# NAME EQUAL TRIPLESTRING NEWLINE 
b = '''multiline with 

			tabs preserved''' 
# NAME EQUAL TRIPLESTRING NEWLINE 
c = "Testing single \
			quote string with tabs preserved" 
# NAME EQUAL STRING NEWLINE 
d = 'Testing single \
			quote string with tabs preserved'
# e = 'Testing single quote
# in multiline' 
# NAME EQUAL STRING NEWLINE 

# NEWLINE 
print a 
# PRINT NAME NEWLINE 
print b 
# PRINT NAME NEWLINE 
print c 
# PRINT NAME NEWLINE 
print d 

