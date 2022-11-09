# Created 10/25/22
# By JacobT2006

from cmath import pi
from pickletools import stringnl_noescape

import math as M  



stringOne = """YOUR CALCULATED ANSWER IS:"""

def calc():
    type = input('''
    Degree(Deg) or Radian(Rad):\t ''')
    if type == 'Deg' or 'deg':
        print('''
        + = Addition, - = Subtract, x = Multiply, / = Division, ^ = Power of, A = Area, S = Sine, C = Cosine, T = Tangent
        ''')
        sym = input('Type symbol(+, -, *, /, ^, A, S, C, T):\t')
    
        if sym == '+':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) + int(num2)
            print( "*" * 80)
            print(stringOne, out)
            print( "*" * 80)
        elif sym == '-':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) - int(num2)
            print( "*" * 80)
            print(stringOne, out)
            print( "*" * 80)  
        elif sym == '*':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) * int(num2) 
            print( "*" * 80)
            print(stringOne, out)
            print( "*" * 80)
        elif sym == '/':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) / int(num2)
            print( "*" * 80)
            print(stringOne, out)
            print( "*" * 80)        
        elif sym == '^':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) ** int(num2)
            print( "*" * 80)
            print(stringOne, out)
            print( "*" * 80)
        elif sym == 'S' or 's':
            num1 = int(input("Number:\t"))
            out = M.sin(num1)
            ans = out * M.pi / 180
            print( "*" * 80)
            print(stringOne, ans)
            print( "*" * 80)
        elif sym == 'C' or 'c':
            num1 = int(input("Number:\t"))
            out = M.cos(num1)
            ans = out * M.pi / 180
            print( "*" * 80)
            print(stringOne, ans)
            print( "*" * 80)
        elif sym == 'T' or 't':
            num1 = int(input("Number:\t"))
            out = M.tan(num1)
            ans = out * M.pi / 180
            print( "*" * 80)
            print(stringOne, ans)
            print( "*" * 80)
        elif sym == 'A' or 'a':
            def area():
                print('''
                 S = Square, R = Rectange, P = Parallelogram, T = Triangle, Tr = Trapezoid, E = Ellipse, C = Circle
                ''')
                a = input('Area of a:\t')

                if a == 'S' or 's':
                    num1 = input('Side:\t')
                    out = 2 * int(num1)
                    print( "*" * 80)
                    print(stringOne, out)
                    print( "*" * 80)
                elif a == 'R' or 'r':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = int(num1) * int(num2)
                    print( "*" * 80)
                    print(stringOne, out)
                    print( "*" * 80)
                elif a == 'P' or 'p':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = int(num1) * int(num2)
                    print( "*" * 80)
                    print(stringOne, out)
                    print( "*" * 80)
                elif a == 'T' or 't':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = 0.5(int(num1)) * int(num2)
                    print( "*" * 80)
                    print(stringOne, out)
                    print( "*" * 80)
                elif a == 'Tr' or 'tr':
                    num1 = input('Base one:\t')
                    num2 = input('Base two:\t')
                    num3 = input('Height:\t')
                    out = (int(num1) + int(num2))/2 * int(num3)
                    print( "*" * 80)
                    print(stringOne, out)
                    print( "*" * 80)
                elif a == 'E' or 'e':
                    num1 = input('Major Axis:\t')
                    num2 = input('Minor Axis:\t')
                    out = M.pi*(int(num1) * int(num2))
                    print( "*" * 80)
                    print(stringOne, out)
                    print( "*" * 80)
                elif a == 'C' or 'c':
                    num1 = input('Radius:\t')
                    out = M.pi*int(num1) * int(num1)
                    print( "*" * 80)
                    print(stringOne, out)
                    print( "*" * 80)
            area()
        else:
            return calc()
    
        def again():
            rep = input('Calculate Again(Y or N):\t')

            if rep == 'Y' or 'y' :
                calc()
            elif rep == 'N' or 'n':
                print('Bye Bye')
            else:
                again()
        again()

    if type == 'Rad' or 'rad':
        print('''
        + = Addition, - = Subtract, x = Multiply, / = Division, ^ = Power of, A = Area, S = Sine, C = Cosine, T = Tangent
        ''')
        sym = input('Type symbol(+, -, *, /, ^, A, S, C, T):\t')
    
        if sym == '+':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) + int(num2)
            print(stringOne, out)
        elif sym == '-':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) - int(num2)
            print(stringOne, out)  
        elif sym == '*':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) * int(num2) 
            print(stringOne, out)
        elif sym == '/':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) / int(num2)
            print(stringOne, out)
        elif sym == '^':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) ** int(num2)
            print(stringOne, out)
        elif sym == 'S' or 's':
            num1 = int(input("Number:\t"))
            out = M.sin(num1)
            ans = out * M.pi / 180
            print(stringOne, ans)
        elif sym == 'C' or 'c':
            num1 = int(input("Number:\t"))
            out = M.cos(num1)
            ans = out * M.pi / 180
            print(stringOne, ans)
        elif sym == 'T' or 't':
            num1 = int(input("Number:\t"))
            out = M.tan(num1)
            ans = out * M.pi / 180
            print(stringOne, ans)
        elif sym == 'A' or 'a':
            def area():
                print('''
                 S = Square, R = Rectange, P = Parallelogram, T = Triangle, Tr = Trapezoid, E = Ellipse, C = Circle
                ''')
                a = input('Area of a: ')

                if a == 'S' or 's':
                    num1 = input('Side: ')
                    out = 2 * int(num1)
                    print(stringOne, out)
                elif a == 'R' or 'r':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = int(num1) * int(num2)
                    print(stringOne, out)
                elif a == 'P' or 'p':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = int(num1) * int(num2)
                    print(stringOne, out)
                elif a == 'T' or 't':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = 0.5(int(num1)) * int(num2)
                    print(stringOne, out)
                elif a == 'Tr' or 'tr':
                    num1 = input('Base one:\t')
                    num2 = input('Base two:\t')
                    num3 = input('Height:\t')
                    out = (int(num1) + int(num2))/2 * int(num3)
                    print(stringOne, out)
                elif a == 'E' or 'e':
                    num1 = input('Major Axis:\t')
                    num2 = input('Minor Axis:\t')
                    out = M.pi*(int(num1) * int(num2))
                    print(stringOne, out)
                elif a == 'C' or 'c':
                    num1 = input('Radius:\t')
                    out = M.pi*int(num1) * int(num1)
                    print(stringOne, out)
            area()
        else:
            return calc()
    
        def again():
            rep = input('Calculate Again(Y or N):\t')

            if rep == 'Y' or 'y' :
                calc()
            elif rep == 'N' or 'n':
                print('Bye Bye')
            else:
                again()
        again()

calc()





















#monkeism
