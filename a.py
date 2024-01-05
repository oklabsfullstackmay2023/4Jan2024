#1. Function Defination is one time process
a=10 #Global Variable
def vishal():
    b=50 #Local Variable
    print(a+b)
    pass

#2. Function calling/invoking is many time process
result=vishal()
print(result)