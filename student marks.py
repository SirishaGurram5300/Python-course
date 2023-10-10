#printing student marks
sno = int(input("enter the student id"))
sname = input("enter the student name")
grp = input("enter the group")
s1 = int(input("enter the python marks"))
s2 = int(input("enter the DBMS marks"))
s3 = int(input("enter the stat marks"))

total = (s1 + s2 + s3)
avg = total/3

print(total)
print(avg)
