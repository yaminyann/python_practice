import requests
import sys


base_url = "http://subeen.com/download/"

info_dt = {"name": "yamin","email": "book@subeen.com","country": "bangladesh"}

url = base_url + "process.php"

response = requests.post(url, data=info_dt)
if response.ok is False:
    sys.exit("error downloading the file")
with open("cpbook.pdf", "wb") as fp:
    fp.write(response.content)
print("book downloading completed")

