import pyshorteners

link = input("Enter the link: ")


def makeItShort(url):

    shortener = pyshorteners.Shortener()
    x = shortener.tinyurl.short(link)
    print(x)


makeItShort(link)
