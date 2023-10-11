#Program to check whether student pass or fail

sno = int(input("enter the num"))
sname = input("enter the name")
group = input("enter the group")
s1 = int(input("enter the python marks"))
s2 = int(input("enter the stat marks"))
s3 = int(input("enter the cs marks"))

if(s1>=40 or s2>=40 or s3>=40):
         print("PASS")
else:
         print("FAIL")
