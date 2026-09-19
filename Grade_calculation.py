#grade calculation
s1,s2,s3,s4,s5 = map(int,input().split())
total = s1+s2+s3+s4+s5
per = total*100/500
print(per)
if per>=90:
    print("A")
elif per>=75:
    print("B")
elif per>=50:
    print("C")
elif per>=35:
    print("D")
else:
    print("Fail")
    
