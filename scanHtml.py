import requests
import sys


web = sys.argv[1]

html = requests.get(web)

print(html.text)
