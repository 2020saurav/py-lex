def foo(a):
	print   a
	print "fo \n o bar" #dude escape sequences
	s = ["this",
		"is",
		"not",
	        	"new",
		"line"]

def main():		
	a = 42
	foo(a) #indented by
	if a > 3:
		print "indented" 
		print "by tabs"
	#comment to be ignored by the lexer

if __name__=='__main__':
	main()
