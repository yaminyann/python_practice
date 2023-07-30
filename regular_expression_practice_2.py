import re

text = "2020-20-02 this is line 1 . date is 2017/06/01. and there is another date : 2017-07-01. and the third and final date is 2017/08/30."
pat = re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')
print(pat)
print(type(pat))
result = pat.findall(text)
print(result)


s = "Abcd 1234 - 33"
result = re.sub(r'\d','0',s)
print(result)



s = "22/07/2017, 20/01/2017, 01/01/2018"
news_s = re.sub(r'(\d{2})/(\d{2})/{\d{4}','\3-\2-\1',s)
print(news_s)





import re

with open("index.html","r") as h:
    li = h.read()


name = re.findall(r'<li>(.*?)</li>',li)
print(name)

text = "Email your feedback here : book@subeen.com book@subeen thank you "
result = re.findall(r'\w+@\w+\.\w+', text)
print(result)

text = "Email your feedback here : book@subeen.com book@subeen thank you "
result = re.findall(r'\w+@\w+[.]\w+', text)
print(result)

text = "Email your feedback here : book@subeen.com book@subeen thank you py.book@subeen.com "
result = re.findall(r'[.\w]+@\w+[.]\w+', text)
print(result)

text = "Book at subeen.com, book at subeen.com, book(at) subeen dot com, book [at] subeen [dot] com "
result = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+', '@', text, flags=re.I)
print(result)




