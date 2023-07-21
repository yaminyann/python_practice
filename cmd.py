# import sys
# print(sys.argv)
# print(type(sys.argv))

# argu = sys.argv

# a = int(argu[1])
# b = int(argu[2])
# print(a+b)


import requests
import sys
img_url = sys.argv[1]
file_name = sys.argv[2]
r = requests.get(img_url)

with open (file_name, "wb") as f:
    f.write(r.content)


# output terminal in command __ python cmd.py https://goo.gl/Q7LmXw career.png