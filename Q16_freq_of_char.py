#count frequency of each character in a string
s=str(input("Enter the string: "))
dict={}
for c in s:
    if(c in dict):
        dict[c]+=1
    else:
        dict[c]=1
print(dict)
