#count the occurences of a specific element in a list

try:
	li = []

	while True:
		li.append(int(input("Enter no: ")))

except:
	print(li)
	
ele=int(input("Enter element to search: "))
#print("Number of occurences of",ele,":",li.count(ele))
cnt=0
for i in li:
	if(i==ele):
		cnt+=1
print("Number of occurences of",ele,":",cnt)