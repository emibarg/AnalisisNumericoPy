import math

# Define the default functions
def f(x):
    return x * x * x + x * x - 1

def g(x):
    return 1 / math.sqrt(1 + x)

# Implement Fixed Point Iteration Method
def fixedPointIteration(x0, e, N, f, g):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Input Section
x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

# Allow the user to input the functions f(x) and g(x)
f_str = input("Enter the function f(x) (e.g., 'x*x*x + x*x - 1'): ")
g_str = input("Enter the function g(x) (e.g., '1/math.sqrt(1 + x)'): ")

# Define the functions based on user input
def custom_f(x):
    return eval(f_str)

def custom_g(x):
    return eval(g_str)

# Starting Fixed Point Iteration Method
fixedPointIteration(x0, e, N, custom_f, custom_g)
