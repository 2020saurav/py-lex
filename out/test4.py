a = """ Testing a 3 \
			quote string with tabs preserved ' test " some test "" three test \"\"\" ''' tt """ # NAME EQUAL TRIPLESTRING 
b = '''multiline with """ test "" t \'\' \'\'\' test :D '' pp

			tabs preserved''' # NAME EQUAL TRIPLESTRING 
c = """ xyz \t \ '''''' " " '' ''   ff """ # NAME EQUAL TRIPLESTRING 
d = "hel\
lo" # NAME EQUAL STRING 
print a # PRINT NAME 
print b # PRINT NAME 
print c # PRINT NAME 
