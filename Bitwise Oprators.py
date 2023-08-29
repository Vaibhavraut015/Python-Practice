# bitwise opratoract as an oprands as if they were ataring of binary digits they operats bit by bit
#it includes &, OR |, ~ not, ^ Xor, >> right shift, << left shift.

a = 5
b = 22
result = a & b
print(result)

#bitwise OR |
a = 5
b = 22
result = a | b
print(result)

#bitwise NOT ~
a = 5
result = ~a
print(result)

#bitwise XOR ^
a = 5
b = 22
result = a ^ b
print(result)


#Practical example
my_list = [5, 3, 6, 8]
for i in range(len(my_list)):
    my_list[i] = my_list[i] & 3
print(my_list)
