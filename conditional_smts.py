'''
#check even or odd

n=int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")
''''''
#Divisible by 5 and 10

n=int(input())
if n%5==0 and n%10==0:
    print("Divisible")
else:
    print("Not Divisible")
''''''
#Biggest among two nums

a=int(input())
b=int(input())
if a>b:
    print("a is biggest")
elif a<b:
    print("b is biggest")
else:
    print("Equal")
''''''
#Smallest among two nums

a=int(input())
b=int(input())
if a<b:
    print("a is smallest")
elif a>b:
    print("b is smallest")
else:
    print("equal")
''''''
#Divisible by 2,3 and 6

n=int(input())
if n%2==0 and n%3==0 and n%6==0:
    print("Divisible")
else:
    print("Not Divisible")
''''''
#voting eligibility

age=int(input())
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")
''''''
#Stundent pass/fail >=35 in all subs

m=int(input())
p=int(input())
c=int(input())
if m>=35 and p>=35 and c>=35:
    print("Pass")
else:
    print("Fail")
''''''
#Stundent pass/fail >=35 in any one sub

m=int(input())
p=int(input())
c=int(input())
if m>=35 or p>=35 or c>=35:
    print("Pass")
else:
    print("Fail")
''''''
#Student pass/fail >=35 in two subs

m=int(input())
p=int(input())
c=int(input())
if m>=35 and p>=35:
    print("Pass")
elif p>=35 and c>=35:
    print("Pass")
elif m>=35 and c>=35:
    print("Pass")
else:
    print("Fail")
''''''
#biggest among 3 nums

a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("a is biggest")
elif b>c:
    print("b is biggest")
else:
    print("c is biggest")
''''''
#Smallest among 3 nums

a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
    print("a is smallest")
elif b<c:
    print("b is smallest")
else:
    print("c is smallest")
''''''
#perfect Squares

n=int(input())
a=n**0.5
b=a**2
if b==n:
    print("Perfect Square")
else:
    print("Not")
''''''
#Cars required for members(max =5)

n=int(input())
a=n//5
b=n%5
if b>0:
    print(a+1,"Cars Needed")
else:
    print(a,"Cars Needed")
'''
 
    































    
