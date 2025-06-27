'''
#given num is +ve or -ve

n=int(input())
if n>0:
    print("+ve")
elif n<0:              
    print("-ve")
else:
    print("Zero")
''' '''
#Even or Odd

n=int(input())
if n%2==0:
    print("Even")       
else:             
    print("Odd")
''''''
n=int(input())
for i in range(0,n):
    print(i)                 
for i in range(n,0,-1):
    print(i)
''''''
#printing even sum

n=int(input())
Esum=0
for i in range(2,n+1,2):
    print(i,end=" ")       
    Esum+=i
print("\n Sum =",Esum)
''''''
#printing list
 
Fruits=['mango','orange','grapes']
for i in Fruits:                    
    print(i)
''''''
#reversing the list

for i in range(-1,-(len(Fruits))-1,-1):
    print(Fruits[i])                       
'''    '''
#taking list from console

Fruits=list(input().split())
print(Fruits)                           
''''''
#Even Sum and Odd Sum

abc=list(map(int,input().split()))
Esum=0
Osum=0
for i in abc:
    if i%2==0:
        Esum+=i               
    else:
        Osum+=i
print("even sum",Esum)
print("Odd sum",Osum)
''''''
#vowels in a string

name=input()
vowels='aeiouAEIOU'
vowelstr=""
vowellist=[]
for i in name:              
    if i in vowels:
        vowelstr+=i
        vowellist.append(i)
print(vowelstr)
print(vowellist)

''''''
#Max vowels string in a list

fruits=list(input().split())
vowels='aeiouAEIOU'
Max_c=0
Max_cn=''
V={}
for i in fruits:
    if len(i)>5:
        c=0                  
        for j in i:
            if j in vowels:
                c+=1
            if c>Max_c:
                Max_c=c
                Max_cn=i
        #print(c,i)
        V[i]=c
print(V)
print(Max_cn)
''''''
a=int(input())
print(a,"num",a,"is")
''''''
#Max num in list

abc=list(map(int,input().split()))
Start=abc[0]                         
for i in abc:
    if Start<i:
        Start=i
print(Start)
''''''
#Min num in list

abc=list(map(int,input().split()))
Start=abc[0]
for i in abc:                        
    if Start>i:                 
        Start=i
print(Start)
''''''
#remove Duplicates

a=[1,2,3,1,1,1,2,2,3,3,44,44,100]
r=[]
for i in a:
    if i not in r:           
        r.append(i)
print(r)
''''''
#removing duplicates without using new list

a=[1,1,1,1,2,2,2,3,3,3,4,4,4,1,2,3,4]

for i in range(len(a)):               
    for j in range(len(a)-1,i,-1):
        if a[i] == a[j]:
            del a[j]
print(a)
'''
        
     














        
        
                


















        

