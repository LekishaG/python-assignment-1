#remove punctuation from a string

s=str(input("Enter a string: "))
newstr=""
for c in s:
    if(c.isalnum() or c==" "):
        newstr+=c

print("String after removing punctuation:",newstr)