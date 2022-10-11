from cmath import pi
from pickletools import stringnl_noescape

import math as M  

stringOne = "THE ANSWER IS: "

def calc():
    type = input('Degree(Deg) or Radian(Rad):\t')
    if type == 'Deg':
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
        elif sym == 'S':
            num1 = int(input("Number:\t"))
            out = M.sin(num1)
            ans = out * M.pi / 180
            print(stringOne, ans)
        elif sym == 'C':
            num1 = int(input("Number:\t"))
            out = M.cos(num1)
            ans = out * M.pi / 180
            print(stringOne, ans)
        elif sym == 'T':
            num1 = int(input("Number:\t"))
            out = M.tan(num1)
            ans = out * M.pi / 180
            print(stringOne, ans)
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
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = int(num1) * int(num2)
                    print(stringOne, out)
                elif a == 'P':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = int(num1) * int(num2)
                    print(stringOne, out)
                elif a == 'T':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = 0.5(int(num1)) * int(num2)
                    print(stringOne, out)
                elif a == 'Tr':
                    num1 = input('Base one:\t')
                    num2 = input('Base two:\t')
                    num3 = input('Height:\t')
                    out = (int(num1) + int(num2))/2 * int(num3)
                    print(stringOne, out)
                elif a == 'E':
                    num1 = input('Major Axis:\t')
                    num2 = input('Minor Axis:\t')
                    out = M.pi*(int(num1) * int(num2))
                    print(stringOne, out)
                elif a == 'C':
                    num1 = input('Radius:\t')
                    out = M.pi*int(num1) * int(num1)
                    print(stringOne, out)
            area()
        else:
            return calc()
    
        def again():
            rep = input('Calculate Again(Y or N):\t')

            if rep == 'Y' :
                calc()
            elif rep == 'N':
                print('Bye Bye')
            else:
                again()
        again()

    if type == 'Rad':
        print('''
        + = Addition, - = Subtract, x = Multiply, / = Division, ^ = Power of, A = Area, S = Sine, C = Cosine, T = Tangent
        ''')
        sym = input('Type symbol(+, -, *, /, ^, A, S, C, T):\t')
    
        if sym == '+':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) + int(num2)
            ans = out * M.pi / 180
            print(stringOne, ans)
        elif sym == '-':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) - int(num2)
            ans = out * M.pi / 180
            print(stringOne, ans)  
        elif sym == '*':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) * int(num2) 
            ans = out * M.pi / 180
            print(stringOne, ans)
        elif sym == '/':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) / int(num2)
            ans = out * M.pi / 180
            print(stringOne, ans)
        elif sym == '^':
            num1 = input('Number one:\t')
            num2 = input('Number two:\t')
            out = int(num1) ** int(num2)
            ans = out * M.pi / 180
            print(stringOne, ans)
        elif sym == 'S':
            num1 = int(input("Number:\t"))
            print(M.sin(num1))
        elif sym == 'C':
            num1 = int(input("Number:\t"))
            print(M.cos(num1))
        elif sym == 'T':
            num1 = int(input("Number:\t"))
            print(M.tan(num1))
        elif sym == 'A':
            def area():
                print('''
                 S = Square, R = Rectange, P = Parallelogram, T = Triangle, Tr = Trapezoid, E = Ellipse, C = Circle
                ''')
                a = input('Area of a: ')

                if a == 'S':
                    num1 = input('Side: ')
                    out = 2 * int(num1)
                    ans = out * M.pi / 180
                    print(stringOne, ans)
                elif a == 'R':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = int(num1) * int(num2)
                    ans = out * M.pi / 180
                    print(stringOne, ans)
                elif a == 'P':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = int(num1) * int(num2)
                    ans = out * M.pi / 180
                    print(stringOne, ans)
                elif a == 'T':
                    num1 = input('Base:\t')
                    num2 = input('Height:\t')
                    out = 0.5(int(num1)) * int(num2)
                    ans = out * M.pi / 180
                    print(stringOne, ans)
                elif a == 'Tr':
                    num1 = input('Base one:\t')
                    num2 = input('Base two:\t')
                    num3 = input('Height:\t')
                    out = (int(num1) + int(num2))/2 * int(num3)
                    ans = out * M.pi / 180
                    print(stringOne, ans)
                elif a == 'E':
                    num1 = input('Major Axis:\t')
                    num2 = input('Minor Axis:\t')
                    out = M.pi*(int(num1) * int(num2))
                    ans = out * M.pi / 180
                    print(stringOne, ans)
                elif a == 'C':
                    num1 = input('Radius:\t')
                    out = M.pi*int(num1) * int(num1)
                    ans = out * M.pi / 180
                    print(stringOne, ans)
            area()
        else:
            return calc()
    
        def again():
            rep = input('Calculate Again(Y or N):\t')

            if rep == 'Y' :
                calc()
            elif rep == 'N':
                print('Bye Bye')
            else:
                again()
        again()

calc()
