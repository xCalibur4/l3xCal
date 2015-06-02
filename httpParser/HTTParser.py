# HTTP log file parser

import re   # module for regular expression matching operations 


#class for parsing HTTP log file
class HTTParser:

    def __init__(self):					# default constructor
        self.fp = open("weblog.txt")	# open http log file
        self.count = 1					# will be used as counter when required

    def __del__(self):
    	self.fp.close()

    def parseme(self):		# function to parse log file line by line
        for x in self.fp:
		   regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+ *\d+)* "(.*?)" "(.*?)"'		# regular expression for patterns without - after status code
		   x = str(x)
		   p = re.match(regex,x)	# match function matches string with the regular expression
		   if p == None:
		      regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+ *\d+)* - "(.*?)" "(.*?)"'	# regular expression for patterns with - after status code
		      p = re.match(regex,x)

		   self.count += 1

		   print "\n\n"
		   print "Request Number \t:" + str(self.count)
		   print "Client IP \t: " + p.group(1)
		   print "Timestamp \t: " + p.group(2)

		   l=[]
		   k = p.group(3)
		   l = k.split()	

		   print "Method   \t: " + l[0]
		   print "URL      \t: " + l[1]
		   print "Version  \t: " + l[2]

		   l = []
		   k = p.group(4)
		   l = k.split()

		   if len(l) == 2:
		      print "Status Code\t: " + l[0]
		      print "Object size\t: " + l[1]
		   else:
		      print "Status Code\t: " + l[0]

		   print "Referer  \t: " + p.group(5)
		   print "User-agent \t: " + p.group(6)

if __name__ == '__main__':

	myparser = HTTParser()
	myparser.parseme()