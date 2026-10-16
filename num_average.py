# Average of two numbers :

def average(a, b):
    print("the average is : ", (a+b)/2)
    
average(1, 5)

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is : ", sum / len(numbers))

average(5, 6)

def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"],    name["lname"])
   
name(fname="Karan", mname="Singh", lname="Patwal")

def average(a, b):
    print(f"the average of {a} and {b} is : ", (a+b)/2)
    
average(3, 8)