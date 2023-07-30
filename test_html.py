
import re

with open("index.html","r") as h:
    li = h.read()


name = re.findall(r'<li>(.*?)</li>',li)
print(name)
