#checking if 2 strings are anagrams of each other
s1=str(input("Enter the string 1: "))
s2=str(input("Enter the string 2: "))

x1=sorted(s1)
x2=sorted(s2)

if(x1==x2):
    print("The 2 strings are anagrams of each other")
else:
    print("The 2 strings are not anagrams of each other")

'''
dict1={}
for c in s1:
    if(c in dict1):
        dict1[c]+=1
    else:
        dict1[c]=1

dict2={}
for c in s2:
    if(c in dict2):
        dict2[c]+=1
    else:
        dict2[c]=1

if(dict1==dict2):
    print("The 2 strings are anagrams of each other")
else:
    print("The 2 strings are not anagrams of each other")
'''


