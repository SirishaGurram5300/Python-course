#printing EMI
p=int(input("enter principal amount"))
t=int(input("enter time"))
r=int(input("enter rate of interest"))
si=p*t*r/100
print(si)

total = si+p
EMI = total/(12*t)

print(EMI)
