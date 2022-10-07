
from cmath import pi
from pickletools import stringnl_noescape

import math as M  

print('''
+ = Addition, - = Subtract, x = Multiply, / = Division, ^ = Power of, A = Area
''')


stringOne = "THE ANSWER IS: "

def calc():
    sym = input('Type symbol(+, -, *, /, ^, A): ')
    
    if sym == '+':
        num1 = input('Number one: ')
        num2 = input('Number two: ')
        out = int(num1) + int(num2)
        print(stringOne, out)
    elif sym == '-':
        num1 = input('Number one: ')
        num2 = input('Number two: ')
        out = int(num1) - int(num2)
        print(stringOne, out)  
    elif sym == '*':
        num1 = input('Number one: ')
        num2 = input('Number two: ')
        out = int(num1) * int(num2) 
        print(stringOne, out)
    elif sym == '/':
        num1 = input('Number one: ')
        num2 = input('Number two: ')
        out = int(num1) / int(num2)
        print(stringOne, out)
    elif sym == '^':
        num1 = input('Number one: ')
        num2 = input('Number two: ')
        out = int(num1) ** int(num2)
        print(stringOne, out)
    elif sym == 'A':
        
        def area():
            print('''
        S = Square, R = Rectange, P = Parallelogram, T = Triangle, Tr = Trapezoid, E = Ellipse, C = Circle
        ''')
            a = input('Area of a: ')

            if a == 'S':
                num1 = input('Side: ')
                out = 2 * int(num1)
                print(stringOne, out)
            elif a == 'R':
                num1 = input('Base: ')
                num2 = input('Height: ')
                out = int(num1) * int(num2)
                print(stringOne, out)
            elif a == 'P':
                num1 = input('Base: ')
                num2 = input('Height: ')
                out = int(num1) * int(num2)
                print(stringOne, out)
            elif a == 'T':
                num1 = input('Base: ')
                num2 = input('Height: ')
                out = 0.5(int(num1)) * int(num2)
                print(stringOne, out)
            elif a == 'Tr':
                num1 = input('Base one: ')
                num2 = input('Base two: ')
                num3 = input('Height: ')
                out = (int(num1) + int(num2))/2 * int(num3)
                print(stringOne, out)
            elif a == 'E':
                num1 = input('Major Axis: ')
                num2 = input('Minor Axis: ')
                out = M.pi*(int(num1) * int(num2))
                print(stringOne, out)
            elif a == 'C':
                num1 = input('Radius: ')
                out = M.pi*int(num1) * int(num1)
                print(stringOne, out)
        area()
    else:
        return calc()
    
    def again():
        rep = input('Calculate Again(Y or N): ')

        if rep == 'Y' :
            calc()
        elif rep == 'N':
            print('Bye Bye')
        else:
            again()

    again()


calc()

