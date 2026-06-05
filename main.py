n=input("Enter a list of products:")
clean_list = n.strip().lower()
no_duplicates =  list(set(clean_list))
words = no_duplicates.sort()
