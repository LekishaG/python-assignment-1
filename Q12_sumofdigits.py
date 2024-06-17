#sum ofdigits of given number
num=int(input("Enter the number: "))
sum=0
while(num>0):
    sum+= num%10
    num=num//10
print("Sum of digits:",sum)