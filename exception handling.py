# for error handling in our website and application and not app dead
try:
 a=int(input("enter your number:"))
 print(a+3)
except:
 print("some error is occured")