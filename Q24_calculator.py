#to create a simple calculator

while True:
    print("\n\tCALCULATOR")
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    op=str(input("Enter operator: "))

    if(op=="+"):
        print(num1,op,num2,":",num1+num2)
    elif(op=="-"):
        print(num1,op,num2,":",num1-num2)
    elif(op=="*"):
        print(num1,op,num2,":",num1*num2)
    elif(op=="/"):
        try:
            print(num1,op,num2,":",num1/num2)
        except:
            print("Can't divide by 0")
    else:
        print("Invalid choice")

    choice=str(input("Continue (Y/N): "))
    if(choice.upper()=="N"):
        print("Thank you")
        break

    