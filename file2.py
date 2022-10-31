from re import I


def power(a,b):
    x=1
    i=1
    for i in range (b):
        x*=a
        ++i
    print(a,"to the power",b," = ",x)

def add(a,b):
    print(a,'+',b,'=',a+b)



def factorial(b):
    num=1
    i=1
    while (i<=b):
        num*=i
        ++i
    print(num)