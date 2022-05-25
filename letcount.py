def lrtcount(str1):
    ic = {}
    for n in str1:
        keys = ic.keys()
        if n in keys:
            ic[n] += 1
        else:
            ic[n] = 1
    return ic  
str1=str(input("Please enter astring"))
sol=lrtcount(str1)
sol.sort()
print(sol)

