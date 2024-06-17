#read multiple lines of input from user unil empty line

lines=[]
while True:
    l=str(input())
    if not l:
        break
    lines.append(l)
    
for i in lines:
    print(i)