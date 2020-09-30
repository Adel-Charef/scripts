from itertools import product
import string

min_len = int(input("Enter minimum length of password: "))
max_len = int(input("Enter maximum length of password: "))
counter = 0
character = string.ascii_lowercase + \
    string.ascii_uppercase + string.digits + string.punctuation

wordlist_file = open("wordlist.txt", "w")

for i in range(min_len, max_len + 1):
    for j in product(character, repeat=i):
        word = "".join(j)
        wordlist_file.write(word)
        wordlist_file.write("\n")
        counter += 1
print("Wordlist of {} passwords created successfully".format(counter))