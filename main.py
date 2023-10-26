def isDivisible(num):
    
    res = []
    i = 2;

    while i < num:
        if num % i == 0:
            res.append(i)
        i += 1
    
    if not res:
        print(f"{num} is prime!")
    else:
        print(f"The divisors of {num} are: {res}")

    return res


def getCommonDivisors(num1, num2):
    
    divisorsNum1 = []
    divisorsNum2 = []

    i = 2

    while i <= num1:
        if num1 % i == 0:
            divisorsNum1.append(i)
        i += 1

    i = 2

    while i <= num2:
        if num2 % i == 0:
            divisorsNum2.append(i)
        i += 1
        
    common_divisors = list(set(divisorsNum1) & set(divisorsNum2))
    print(f"common divisors are: {common_divisors}")

    return common_divisors

def findGCF(common_divisors):
    GCF = max(common_divisors)
    print(f"the GCF is: {GCF}")
    pass




num1 = int(input("num1: "))
num2 = int(input("num2: "))

common_divisors = getCommonDivisors(num1, num2)

findGCF(common_divisors)

num = int(input("enter a number to see what its divisors are: "))

isDivisible(num)



#Challenge: write a function that finds the GCF of two numbers
#Make it return the the furthest reduced fraction

#Challenge: create a pythagorean theorum calculator