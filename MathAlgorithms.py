print("hello! these are some simple math algorithms for practice.")

print("address: https://github.com/amrezalou/simple-MathAlgorithms.git")

print("""
1) fibonacci series
2) show prime number
3) LCM
4) calculate factorial
5) check-odd-even
6) check perfect number
7) pythagorean numbers
8) discount calculation
9) area of some shapes
10) GCD
""")



# 1

def FibonacciSeries(n):
   """Function that calculates fibonacci series up to n."""
   result = []
   a, b = 0, 1
   while a < n:
       result.append(a)
       a, b = b, a+b
   print(result)


# -------------------------------------------------------------------------

# 2

def PrimeNumber(n):
    """ Shows prime numbers. """

    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "is prime.")
        else:
            print(num, "is not prime.")


#-------------------------------------------------------------------------

# 3

def LCM(a, b):
   """ Shows LCM between 2 numbers. """
   MAX = max(a, b)
   MIN = min(a, b)

   if MAX % MIN == 0:
       print("LCM (a, b):" , MAX)
   else:
       while(True):
           if MAX % a == 0 and MAX % b == 0:
               lcm = MAX
               break
           MAX+=1
       print("LCM (a, b): ", lcm)




#-------------------------------------------------------------------------

# 4

def Factorial(n):
   """ Calculate the factorial of n. """
   if n == 0 or n == 1:
       return 1
   else:
       return n * Factorial(n - 1)




#-------------------------------------------------------------------------

# 5


def ODD_and_EVEN(number):
   """ Check for type of number among odd and even. """

   if number % 2 == 0:
       print("the number is even!")
   else:
       print(number, "is odd!")



# -------------------------------------------------------------------------

# 6

def Perfect(n):
   result = []
   for i in range(1, n):
       if n % i == 0:
           result.append(i)
   sum_of_result = sum(result)
   return sum_of_result == n



#-------------------------------------------------------------------------

# 7

def pythagorean_number_checker():
   """ Check if 3 numbers are Pythagorean or they're not. """
   # a**2 + b**2 = c**2 (chord)
   a = int(input("enter the smallest number: "))
   b = int(input("enter the number with average value(second): "))
   c = int(input("enter the bigges one now: "))

   if a**2 + b**2 == c**2:
       print("True, these numbers are pythagorean numbers.")

   else:
       print("False, numbers are not pythagorean numbers.")




#-------------------------------------------------------------------------

# 8

def discount_calculation(price, precentageD):
   """ A simple fucntion to calculte discount of something product. """
   discount = price * precentageD / 100
   print(price - discount)




#-------------------------------------------------------------------------

# 9

import math

def Acircle(r):
   """ Computing area of circle. """

   aoc = r*r*math.pi
   print(aoc)


def Atriangle(b, h):
   """ Computing area of triangle. """

   aot = b*h*0.5
   print(aot)


def Atrapeziod(b1, b2, h):
   """ Computing area of trapeziod. """

   aot2 = ((b1+b2) / 2 ) * h
   print(aot2)



#-------------------------------------------------------------------------

# 10

def GCD(a, b):
   """ Compute GCD of two numbers."""

   small = min(a, b)

   for i in range (1, small + 1):
       if a % i == 0  and b % i == 0:
           gcd = i
   print(gcd)





user = input("which one do you want to see/use? (1 to 10): ")

if user == '1':
    n = int(input("enter the number of fibonacci up to the: "))
    FibonacciSeries(n)

elif user == '2':
    n = int(input("check range of prime numbers up to n: "))
    PrimeNumber(n)

elif user == '3':
    n1 = int(input("enter the first number: "))
    n2 = int(input("enter the first number: "))

    LCM(n1, n2)
elif user == '4':
    n = int(input("factorial of your number: "))
    print("factorial of", n, "is: ", Factorial(n))

elif user == '5':
    n = int(input("enter number for typecheck: "))
    ODD_and_EVEN(n)

elif user == '6':
    n = int(input("check if its perfect number: "))
    if Perfect(n):
        print(n, "is a perfect.")
    else:
        print(n, "is not a perfect.")

elif user == '7':
    pythagorean_number_checker()

elif user == '8':
    price = float(input("enter price: "))
    precentage = float(input("enter precentage: "))
    discount_calculation(price, precentage)

elif user == '9':
    ask = input("which shape? \n 1)circle \n 2)triangle \n 3)trapeziod: ")
    if ask == '1':
        n = float(input("enter value of radius of the circle: "))
        Acircle(n)

    elif ask == '2':
        b = float(input("enter base value: "))
        h = float(input("enter height value: "))
        Atriangle(b, h)

    else:
        b1 = float(input("base1 value: "))
        b2 = float(input("base2 value: "))
        h = float(input("and finally enter the value of height: "))
        Atrapeziod(b1, b2, h)

elif user == '10':
    n = int(input("the first: "))
    m = int(input("the second: "))
    GCD(n, m)

