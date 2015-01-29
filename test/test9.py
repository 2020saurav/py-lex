#!/usr/bin/python
# first 2 lines may have encoding info

#explicit line joins 2.1.5
year = 99999
if year > 1000 or \
	    some_arbit_thing: #no comment can be after \. \ in comment is ignored.
	print 42 #no comment betwwn some arbit and \ either

#implicit
a = [
	'me', 'her', # comment can be here
	   
	   'anything' # The indentation of the continuation lines is not important
]
print a