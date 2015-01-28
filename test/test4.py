a = """ Testing a 3 \
			quote string with tabs preserved ' test " some test "" three test \"\"\" ''' tt """
b = '''multiline with """ test "" t \'\' \'\'\' test :D '' pp

			tabs preserved'''
c =  "Testing single \
			quote string with tabs preserved"
d =  'Testing single \
			quote string with tabs preserved'
# e = 'Testing single quote
# in multiline'
# THIS IS ^ NOT ALLOWED!
print a
print b
print c
print d
