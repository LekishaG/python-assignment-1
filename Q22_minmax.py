#to find the minimum and maximum values in a list
li=eval(input("Enter list of numbers: "))
print(li)

"""
print("Maximum element in list: ",max(li))
print("Minimum element in list: ",min(li))
"""

minel=li[0]
maxel=li[0]
for i in li:
    if(i<minel):
        minel=i
    if(i>maxel):
        maxel=i
print("Maximum element in list: ",maxel)
print("Minimum element in list: ",minel)
