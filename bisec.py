import math
def bisection_method(func, a, b, err):
    def f(x):
        f= eval(func)
        return f
    error = abs(b-a)

    

    while error> err:
        c = (b+a)/2
        if f(a)*f(b)>=0:
            print("no hay raices o hay multiples raices en este intervalo")
            quit()
        elif f(c)*f(a) <0:
            b =c
            error = abs(b-a)
        elif f(c)*f(b) <0:
            a =c
            error = abs(b-a)
        else:
            print("Presiento que algo anda mal")
            quit()

    print(f"El error es {error}")
    print(f"La cota inferior a es {a}, la cota superior b es {b}")
    print(f"f(a)={f(a)} ")
    print(f"f(b)={f(b)} ")

bisection_method("math.e**-x - x", 0 , 1, 0.001)