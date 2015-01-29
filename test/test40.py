import urllib
lines=[line.strip() for line in open('links')]
i=1
for line in lines:
	urllib.urlretrieve(line,filename=str(i)+".jpg")
	i+=1
