import re

s = "Afganistan,America,Bangladesh,Canada,Denmark,England,Greenland,Iceland,Netherlands,New Zealand,Sweden,Switzerland"
countries = s.split(",")

#li = [item for item in countries if item.endswith("land") or item.endswith("lands")]


li = re.findall(r'(\w+lands*)',s)
print(li)

match = re.search('Bangla','Bangladesh')
match.group()
print(match.group())
match = re.search('desh','Bangladesh')
print(match.group())
match = re.search('des','Bangladesh')
match.group()
print(match.group())

print(type(match))

s = "Bangladesh"
match = re.search('.',s)
print(match.group())
match = re.search('B.n',s)
print(match.group())
match = re.search('B.n...',s)
print(match.group())

s = "Bangladesh is our homeland"
match = re.search('............',s)
print(match.group())
match = re.search("o\w\w",s)
print(match.group())
# match = re.search("o\w\w",s)
# print(match.group())

match = re.search('B\w+h',s)
print(match.group())
match = re.search('B.+h',s)
print(match.group())
match = re.search('B.+?h',s)
print(match.group())



text = "phone number: 01938387917."
match = re.search('\d+',text)
print(match.group())


text = "house number : 5 , phone number : 019 38387917"
match = re.search('\d{3}\s?\d{8}',text) # \s \s+ \s* \s?
print(match.group())


text = " Multiple phone number , 01711111111,01811111111,019191919191,00000000000 123-123 "
result = re.findall(r'01[56789]\s*\d{8}',text)
print(result)


#s = "bangla english bangla"
print(re.findall(r'english',s))
print(re.findall(r'^english',s))
print(re.findall(r'english$',s))
print(re.findall(r'^bangla',s))
print(re.findall(r'bangla$',s))

s = "Bangla english Bangla"
print(re.findall(r'bangla$',s))
print(re.findall(r'bangla$',s,re.IGNORECASE)) # or use re.I
print(re.findall(r'bangla$',s,re.I)) # use re.I same as re.INGORECASE




with open("file.txt","r") as f:
    text = f.read()
    print(text)
print(re.findall(r'^.*?$',text))
print(re.findall(r'^.*?$',text,re.MULTILINE))
print(re.findall(r'^.+?$',text,re.MULTILINE))




s = "<li>Tamim</li><li>Shakib</li><li>Mahmudullah</li><li>Mominul</li>"
result = re.findall(r'<li>(.*?)</li>',s)
print(result)


