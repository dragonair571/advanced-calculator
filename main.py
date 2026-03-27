import math

rop = 'yes'

def add(n1, n2):
   return n1 + n2

def subtract(n1, n2):
   return n1 - n2

def multiply(n1, n2):
   return n1 * n2

def divide(n1, n2):
   return n1 / n2

def power(n1, n2):
   return n1 ** n2

def remainder(n1, n2):
   return n1 % n2

def sqrt(n1):
   return n1 ** 0.5

def cube(n1):
   return n1 ** 3

def factorial(n1):
  if n1 == 0:
    return 1
  else:
    return n1 * factorial(n1 - 1)

def sin(n1):
   return math.sin(n1)

def cos(n1):
   return math.cos(n1)

def tan(n1):
   return math.tan(n1)

def log(n1):
   return math.log(n1)

def log10(n1):
   return math.log10(n1)

def exp(n1):
   return math.exp(n1)



def square(n1):
   return n1 ** 2




def restart():
   global rop
   answer = input("Do you want to restart the calculator? (yes/no): ")
   if answer == "yes":
      rop = 'yes'
   else:
      print("Goodbye!")
      rop = 'no'

def calculate():
   operation = input("Enter the operation you want to perform: (add, subtract, multiply, divide, power, remainder, sqrt, cube, factorial, sin, cos, tan, log, log10, exp, square):")

   num1 = int(input('Enter first number: '))
   num2 = int(input('Enter second number: (If you are using sqrt, cube, factorial, sin, cos, tan, log, log10, exp, square, enter anything you want for the second number)'))

   if operation == 'add':
      print(num1, "+", num2, "=", add(num1, num2))
   elif  operation == 'subtract':
      print(num1, "-", num2, "=", subtract(num1, num2))
   elif operation == 'multiply':
      print(num1, "*", num2, "=", multiply(num1, num2))
   elif operation == 'divide':
      print(num1, "/", num2, "=", divide(num1, num2))
   elif operation == 'power':
      print(num1, "**", num2, "=", power(num1, num2))
   elif operation == 'remainder':
      print(num1, "%", num2, "=", remainder(num1, num2))
   elif operation == 'sqrt':
      print(num1, "**", 0.5, "=", sqrt(num1))
   elif operation == 'cube':
      print(num1, "**", 3, "=", cube(num1))
   elif operation == 'factorial':
      print(num1, "!", "=", factorial(num1))
   elif operation == 'sin':
      print("sin(", num1, ")", "=", sin(num1))
   elif operation == 'cos':
      print("cos(", num1, ")", "=", cos(num1))
   elif operation == 'tan':
      print("tan(", num1, ")", "=", tan(num1))
   elif operation == 'log':
      print("log(", num1, ")", "=", log(num1))
   elif operation == 'log10':
      print("log10(", num1, ")", "=", log10(num1))
   elif operation == 'exp':
      print("exp(", num1, ")", "=", exp(num1))
   elif operation == 'square':
      print(num1, "**", 2, "=", square(num1))
   else:
      print('Invalid input')



operation = input("Enter the operation you want to perform: (add, subtract, multiply, divide, power, remainder, sqrt, cube, factorial, sin, cos, tan, log, log10, exp, square):")

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: (If you are using sqrt, cube, factorial, sin, cos, tan, log, log10, exp, square, enter anything you want for the second number)'))

if operation == 'add':
   print(num1, "+", num2, "=", add(num1, num2))
elif  operation == 'subtract':
   print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == 'multiply':
   print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == 'divide':
   print(num1, "/", num2, "=", divide(num1, num2))
elif operation == 'power':
   print(num1, "**", num2, "=", power(num1, num2))
elif operation == 'remainder':
   print(num1, "%", num2, "=", remainder(num1, num2))
elif operation == 'sqrt':
   print(num1, "**", 0.5, "=", sqrt(num1))
elif operation == 'cube':
   print(num1, "**", 3, "=", cube(num1))
elif operation == 'factorial':
   print(num1, "!", "=", factorial(num1))
elif operation == 'sin':
   print("sin(", num1, ")", "=", sin(num1))
elif operation == 'cos':
   print("cos(", num1, ")", "=", cos(num1))
elif operation == 'tan':
   print("tan(", num1, ")", "=", tan(num1))
elif operation == 'log':
   print("log(", num1, ")", "=", log(num1))
elif operation == 'log10':
   print("log10(", num1, ")", "=", log10(num1))
elif operation == 'exp':
   print("exp(", num1, ")", "=", exp(num1))
elif operation == 'square':
   print(num1, "**", 2, "=", square(num1))
else:
   print('Invalid input')


restart();

while rop == 'yes':
   calculate();
   restart();

   # This is a calculator program that can perform basic arithmetic operations and some advanced operations like square root, cube, factorial, sine, cosine, tangent, logarithm, exponential, and square.
           

