import requests
from bs4 import BeautifulSoup


url_example = "https://en.wikipedia.org/wiki/Snake"
url = input("Enter URL: ")

response = requests.get(url)
response.raise_for_status()

if response is not None:
    page = BeautifulSoup(response.content, "html.parser")
    title = page.select("#firstHeading")[0].text
    paragraphs = page.select("p")
    print(title)
    intro = "\n".join([para.text for para in paragraphs[0:5]])
    print(intro)
