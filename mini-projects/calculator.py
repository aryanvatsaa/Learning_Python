import math
def sum(a,b):
    a = a + b
    return a

def sub(a,b):
    if a > b:
        a -= b
        return a
    else:
        b -= a
        return b


def mul(a,b):
    a = a * b
    return a

def div(a,b):
    q = a/b
    r = a%b
    print("The quotient is : %s" %q)
    print("The quotient is : %s" %r)

def sqr(a):
    x = math.sqrt(a)
    return x

while(True):
    print("Choose the operation you want to perform : ")
    print("\t1.ADDITION")
    print("\t2.SUBTRACTION")
    print("\t3.MULTIPLICATION")
    print("\t4.DIVISION")
    print("\t5.SQAURE ROOT")
    print("\t6.EXIT")

    choice = int(input('>'))

    if choice==1:
        print("Enter two Numbers : ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        s = sum(num1,num2)
        print("The sum is : %s" %s)

    elif choice==2:
        print("Enter two Numbers : ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        m = sub(num1,num2)
        print("The sum is : %s" %m)

    elif choice==3:
        print("Enter two Numbers : ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        p = mul(num1,num2)
        print("The sum is : %s" %p)

    elif choice==4:
        print("Enter two Numbers : ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        div(num1,num2)

    elif choice==5:
        print("Enter a Number : ")
        num1 = int(input('>'))
        r=sqr(num1)
        print("The Square root is : %s" %r)

    else:
        print("you chose to exit. Bye.........")
        break
