import re

htmlfile = open("r+" , "polubienia.txt")

Filestring = htmlfile.read()

regfile = open("w","list.txt")

pattern = "name lastname<//a> lubi: <a class=\"profileLink\" href=\"*data-hovercard-prefer-more-content-show=\"1\">*</a>"
sztrink = re.finditer(pattern,Filestring)

for i in sztrink.lengh():

	UEREL = re.search("https://facebook.com*\"",sztrink[i])

	NAZWA = re.search("-show=\"1\">*<//a>",sztrink[i])

	NAZWA = re.sub("-show=\"1\">",'',NAZWA)

	NAZWA = re.sub("<//a>",'',NAZWA)

	refile.write("\n " + NAZWA + "  " + UEREL)
	
regfile.close()
htmlfile.close()
	
