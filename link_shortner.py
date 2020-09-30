import pyshorteners

link = input("Enter the link: ")  # link
shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short(link)  # shorting the link
print(x)
