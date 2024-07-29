# calculator

print("Enter The Numbers For Calculation")
num1=float(input("Enter The First number : "))
num2=float(input("Enter The Second number : "))


choice=input("Enter Operation ('+' '-' '*' '/') : ")
if(choice=='+'):
    print("Addition is : ",num1+num2)
elif(choice=='-'):
    print("Subtraction is : ",num1-num2)
elif(choice=='*'):
    print("Multiplication is : ",num1*num2)
elif(choice=='/'):
    print("Division is : ",num1/num2)
else:
    print("Wrong Operation")