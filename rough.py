n=input("Enter a word: ")

if n.lower()==n[::-1].lower():
    print("pal")
else:
    print("no pal")