#convert celcius to fahrenheit or fahrenheit to celcius


while True:
    print("\tMenu\n1.Celcius to Fahrenheit\n2.Fahrenheit to Celcius\n3.Exit")
    choice=int(input("Enter your choice: "))
    if(choice==3):
        print("Thank you")
        break
    elif(choice==1):
        cel=eval(input("Enter temperature (in °C): "))
        fah=cel*9/5 +32
        print("Temperature (in °F):",fah)
    elif(choice==2):
        fah=eval(input("Enter temperature (in °F): "))
        cel= (fah-32)*9/5
        print("Temperature (in °C):",cel)
    else:
        print("Invalid choice")