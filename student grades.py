#Program to generate students results
sno = int(input("enter student id"))
sname = input("enter the name")
group = input("enter the group")
s1 = int(input("enter the maths marks"))
s2 = int(input("enter the chem marks"))
s3 = int(input("enter the cs marks"))

total = s1+s2+s3
avg = total/3

if avg>=90:
    print("O-Grade")
elif avg>=80:
    print("A-Grade")
elif avg>=70:
    print("B-Grade")
elif avg>=60:
    print("C-Grade")
elif avg>=50:
    print("D-Grade")
else:
    print("Pass")

    
