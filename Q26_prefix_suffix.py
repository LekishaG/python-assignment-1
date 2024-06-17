# check if a string starts with given prefix or ends with given suffix

s=str(input("Enter string: "))
ss=str(input("Enter prefix/suffix: "))

if(s.startswith(ss) and s.endswith(ss)):
    print(ss,"is a both prefix and suffix of",s)
elif(s.startswith(ss)):
    print(ss,"is a prefix of",s)
elif(s.endswith(ss)):
    print(ss,"is a suffix of",s)
else:
    print(ss,"is not a prefix or suffix of",s)
