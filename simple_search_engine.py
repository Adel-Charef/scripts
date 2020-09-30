#! usr/bin/python3
# Open several google search results in new tabs

import sys
import requests
import webbrowser
from bs4 import BeautifulSoup

query = sys.argv[1:]
URL = f"https://google.com/search?q={query}"

user_agent = "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"

headers = {"user-agent": user_agent}

print("""
	 *****************************************
         |            My Search Engine           |
         *****************************************
         """)

response = requests.get(URL, headers=headers)
print("Googling.....\n")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
else:
    print("The Status Code is:", response.status_code)

results = []

for g in soup.find_all("div", class_="r"):
    anchors = g.find_all("a")
    if anchors:
        links = anchors[0]["href"]
        results.append(links)

print("*****************************************")
print("              Results........            ")
print("*****************************************\n")
for i in range(min(8, len(results))):
    print(f"{i}-- {results[i]}\n")
selected_result = int(input(">> -Select a Result: "))
webbrowser.open(results[selected_result])
