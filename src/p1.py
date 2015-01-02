def hello():
	print "Hello World!"

class Test:
	num=42 # public
	__pvt=43 # private
	def printnum(self): # this -> self
		print self.num
	def printpvt(self): # to access private variables
		print self.__pvt
