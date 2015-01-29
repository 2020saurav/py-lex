a = """ Testing a 3 \
			quote string with tabs preserved ' test " some test "" three test \"\"\" ''' tt """
b = '''multiline with """ test "" t \'\' \'\'\' test :D '' pp

			tabs preserved'''
c = """ xyz \t \ '''''' " " '' ''   ff """
d = "hel\
lo"
# e = "hel PREVENT THIS FROM PASSING
# o"
print a
print b
print c
