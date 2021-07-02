import re


File = open("google news 2.html",'r')

notice = re.findall("^ *?<a .*articles.*?(?=\n)|(?<=\">)[A-Z][a-z ]* [a-zA-Z ]{26,100}[0-9]*(?=</)",File.read())
File.close()
Filenew = open("Temp.txt",'w')
for note in notice:
	if(note != ""):
		Filenew.write(note+"\n")

Filenew.close()


# This is the final RegEx that i followed to get the required answer. In order to remove small unwanted words 
#i considered that the news should atleast have one word starting with the capital letter and there must 
# atleast have 26 more characters in order to make a statement (Which will make the news headings)