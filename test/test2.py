def foo(a):
	print   a
	print "fo \n o bar" #dude escape sequences
	s = ["this",
		"is",
		"not",
	        	"new",
		"line"]

def main():		
	a = -420.03
	b = 43
	foo(a) #indented by
	if a < 3:
		print "indented ' test ' anything ' \" some random" 
		print 'by tabs" test " anything \' some fer r r " " " " th'
	#comment to be ignored by the lexer

if __name__=='__main__':
	main()
