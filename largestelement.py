''' author :subhajji suhas'''
list1=[]
n=int(input("enter the number"))
for i in range(1,n+1):
    element=int(input("enter the elements:"))
    list1.append(element)
print("largest ele:",max(list1))