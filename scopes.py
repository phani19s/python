'''
#scopes

name="PHANI"
role="DEVELOPER"
def details():
    name="phani"
    role="developer"
    print(f"{name} is a {role}")
details() #local variables
print(f"{name} is a {role}") #global variables
'''

ex_1="Global value."
def function():
    ex_2="With in the funtion."
    print(ex_1)
    print(ex_2)
    print("Function Ends..")
    def sub_function():
        ex_3="With in the sub_function."
        print(ex_1)
        print(ex_2)
        print(ex_3)
        print("Sub_function Ends..")
    sub_function()
function()
print(ex_1,"Outside the functions..")

    
