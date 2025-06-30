'''
#Area of square

s=int(input())
area=s*s
print("Area of the square is:",area)
'''
'''
#Area of rectangle

l=int(input())
b=int(input())
area=l*b
print("Area :",area)
''''''
#Area of triangle

b=int(input())
h=int(input())
area=0.5*h*b
print("Area :",area)
''''''
#perimeter of square

s=int(input())
pe=4*s
print("Perimeter :",pe)
''''''
#perimeter of retangle

l=int(input())
b=int(input())
p=2*(l+b)
print("Perimeter :",p)
''''''
#perimeter of triangle

a,b,c=map(int,input().split())
p=a+b+c
print("Perimeter :",p)
''''''
#Denomination

N=int(input())
A=N//1000
N-=1000*A
B=N//500
N-=500*B
print("1000_notes :",A)
print("500_notes :",B)
print("change :",N)
''''''
#convert seconds into Hours,Minutes and seconds

t=int(input())
h=t//3600
t-=h*3600
m=t//60
t-=m*60
print("Hours :",h)
print("Minutes :",m)
print("Seconds :",t)
''''''
#sum of marks(maths,physics,chemistry)

m=int(input())
p=int(input())
c=int(input())
print("Sum :",(m+p+c))
#Average of marks
print("Average :",((m+p+c)/3))
'''

























































































































































































