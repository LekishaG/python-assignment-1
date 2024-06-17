#return sum of list

try:
	li = []

	while True:
		li.append(int(input("Enter no: ")))

except:
	print(li)
	
sum=0
for i in li:
	sum+=i
print("Sum of numbers in list:",sum)

