'''author subhajji suhas'''
list=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    inPut=int(input("Enter element of list "))
    list.append(inPut)
print("Positive numbers in",list,"are: ")
for i in list:   
    if i >= 0:
       print(i, end = " ")
       