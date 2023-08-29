#Logical oprators are includes and oprators, OR oprator and NOT oprator

number1= int(input("enter first number:"))
number2= int(input("enter second number"))

add= number1+number2
sub= number1-number2

if add and sub > 50:
    print("You are on right track")
else:
    print("you are making somthing wrong")

if add or sub > 50:
    print("You are on right track")
else:
    print("you are making somthing wrong")

if not sub > 50:
    print("You are on right track")
else:
    print("you are making somthing wrong")


