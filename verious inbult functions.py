# built-in zip function in python practice
num =[1,2,3]
str =["a","b","ag""af"]
set =['A1','B2','C4']
outputA= zip(num,str,set)
print(list(outputA))

# for loop in python practice
for i in range(12):
    print(i*i*i)
for x in [1,2,3,4]:
    print(x)
names=["vaibhav","rahul","ram"]
values=[12,125,45]

# Combine for and zip function
for names,values in zip(names,values):
    print(names,values)

# append function
a=[1,2,3,4,5]
a.append(10)
print(a)

# built-in function Sum
a=sum([1,2,3,4,5,6])
print(a)

# List reversed built-in function
a=([1, 2, 3, 4])
output=reversed(a)
print(list(output))

# cumulative sum function
def cumulative_sum():
    for i in range(12):
      print(i*(i-1))
cumulative_sum()
a=([1,2,3,4,5,5,7,8,9])

#unique function in python
def unique(list1):
    unique_list=[]
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print (x)
list1=[1,5,6,5,5,4,1]
print("the unique values :",unique(list1))


def unique(list1):
    unique_list=[]
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
list1=[1,5,6,5,5,4,1]
print("the unique values :",unique(list1))

num= int(input("enter a number:"))
def  count_digits():
    print(len(str(num)))

count_digits()


