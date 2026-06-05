import re
n = input("Enter a list of products:")
clean_list = n.strip().lower()
words_list = clean_list.split(", ")
no_duplicates = list(set(words_list))
no_duplicates.sort(key=str.lower)

print(", ".join(no_duplicates))
