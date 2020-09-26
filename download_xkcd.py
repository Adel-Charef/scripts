import os
import requests
from bs4 import BeautifulSoup

url = "http://xkcd.com"
os.makedirs("xkcd", exist_ok=True)

while not url.endswith("#"):
    # Download the page
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    # Find the URL of the comic image
    comicElem = soup.select("#comic img")
    if not comicElem:
        print("Could not find comic image 👇👇 ")
    else:
        comicUrl = comicElem[0].get("src")
        # Download the image
        print("Downloading image %s" % (url + comicUrl[1:]))
        response = requests.get(url + comicUrl)
        response.raise_for_status()
        # Save the image in ./xkcd
        imgFile = open(os.path.join("xkcd/", os.path.basename(comicUrl)), "wb")
        for chunk in response.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()
    # Get the prev button url
    prevLink = soup.select("a[rel='prev']")[0]
    url = "http://xkcd.com" + prevLink.get("href")

print("Done...")
