import turtle
import time

sc = turtle.Screen()
sc.bgcolor("Gray")

write = turtle.Turtle()
write.hideturtle()
write.penup()
write.goto(-175, 0)
write.write("""Move square by using the mouse to click on it""", font=("Verdana", 15, "normal"))
time.sleep(1.75)
write.clear()
sc.update()

square1 = turtle.Turtle()
square1.speed(0)
square1.penup()
square1.goto(0, 200.0)
square1.color("red")
square1.shape("square")
square1.shapesize(stretch_wid=2.4, stretch_len=2.4)

arrow1 = turtle.Turtle()
arrow1.speed(0)
arrow1.penup()
arrow1.right(90)
arrow1.goto(square1.xcor(), square1.ycor())
arrow1.color("gray")
arrow1.shape("triangle")
arrow1.shapesize(stretch_wid=1.2, stretch_len=1.2)

circle1 = turtle.Turtle()
circle1.color("red")
circle1.penup()
circle1.goto(0, -50.0)
circle1.shape("circle")
circle1.shapesize(stretch_wid=2.4, stretch_len=2.4)

def get_mouse_click_coor1(x, y):
    if square1.xcor() - 25 <= x <= square1.xcor() + 25 and square1.ycor() - 25 <= y <= square1.ycor() + 25:
        square1.clear()
        sc.update()
        y1 = square1.ycor()
        y1 -= 50.0
        square1.sety(y1) 
        arrow1.goto(square1.xcor(),square1.ycor())
        if y1 == -50:
            s1x = 0
            s1y = 200
            s2x = 0
            s2y = -200
                
            circle1.clear()
            circle1.hideturtle()
            square1.clear()
            square1.hideturtle()
            arrow1.clear()
            arrow1.hideturtle()

            write.hideturtle()
            write.penup()
            write.goto(-125, 0)
            write.write("""The further you go the harder it will be""", font=("Verdana", 15, "normal"))
            time.sleep(1)
            write.clear()
            sc.update()

            writing = turtle.Turtle()
            writing.hideturtle()
            writing.penup()
            writing.goto(300, -300)
            writing.write("""RESET""", font=("Verdana", 15, "normal"))

            square3 = turtle.Turtle()
            square3.speed(0)
            square3.penup()
            square3.goto(s1x, s1y)
            square3.color("red")
            square3.shape("square")
            square3.shapesize(stretch_wid=2.4, stretch_len=2.4)

            square2 = turtle.Turtle()
            square2.speed(0)
            square2.penup()
            square2.goto(s2x, s2y)
            square2.color("blue")
            square2.shape("square")
            square2.shapesize(stretch_wid=2.4, stretch_len=2.4)

            arrow1.showturtle()
            arrow1.speed(0)
            arrow1.penup()
            arrow1.right(90)
            arrow1.goto(square3.xcor(), square3.ycor())
            arrow1.color("gray")
            arrow1.shape("triangle")
            arrow1.shapesize(stretch_wid=1.2, stretch_len=1.2)
            arrow1.right(90)

            arrow2 = turtle.Turtle()
            arrow2.speed(0)
            arrow2.penup()
            arrow2.right(90)
            arrow2.goto(square2.xcor(), square2.ycor())
            arrow2.color("gray")
            arrow2.shape("triangle")
            arrow2.shapesize(stretch_wid=1.2, stretch_len=1.2)
            arrow2.left(180)

            circle1.showturtle()
            circle1.color("red")
            circle1.speed(0)
            circle1.penup()
            circle1.goto(-200, 200)
            circle1.shape("circle")
            circle1.shapesize(stretch_wid=2.4, stretch_len=2.4)

            circle2 = turtle.Turtle()
            circle2.speed(0)
            circle2.color("blue")
            circle2.penup()
            circle2.goto(0, 150)
            circle2.shape("circle")
            circle2.shapesize(stretch_wid=2.4, stretch_len=2.4)

            def get_mouse_click_coord2(x, y):
                if square3.xcor() - 25 <= x <= square3.xcor() + 25 and square3.ycor() - 25 <= y <= square3.ycor() + 25:
                    square3.clear()
                    sc.update()
                    x1 = square3.xcor()
                    x1 -= 50.0
                    square3.setx(x1)
                    arrow1
                    arrow1.goto(square3.xcor(),square3.ycor()) 
                if square2.xcor() - 25 <= x <= square2.xcor() + 25 and square2.ycor() - 25 <= y <= square2.ycor() + 25:
                    square2.clear()
                    sc.update()
                    y2 = square2.ycor()
                    y2 += 50.0
                    square2.sety(y2)
                    arrow2.goto(square2.xcor(),square2.ycor())
                    if square2.ycor() == square3.ycor() and square2.xcor() == square3.xcor():
                        y1 = square3.ycor()
                        y1 += 50
                        square3.sety(y1)
                        arrow1.goto(square3.xcor(),square3.ycor())
                if 300 - 25 <= x <= 300 + 25 and -300 - 25 <= y <= -300 + 25:
                    square3.goto(s1x, s1y)
                    square2.goto(s2x, s2y)
                if square3.xcor() == circle1.xcor() and square3.ycor() == circle1.ycor() and square2.xcor() == circle2.xcor() and square2.ycor() == circle2.ycor():
                    s3x = 0
                    s3y = 150
                    s4x = 0
                    s4y = -20
                    c3x = -200
                    c3y = 200
                    c4x = 0
                    c4y = 250
                    
                    square3.clear()
                    square3.hideturtle()
                    square2.clear()
                    square2.hideturtle()
                    circle1.clear()
                    circle1.hideturtle()
                    circle2.clear()
                    circle2.hideturtle()
                    arrow1.clear()
                    arrow1.hideturtle()
                    arrow2.clear()
                    arrow2.hideturtle()
                    
                    write.hideturtle()
                    write.penup()
                    write.goto(-75, 0)
                    write.write("""You have got this!!!""", font=("Verdana", 15, "normal"))
                    time.sleep(.75)
                    write.clear()
                    sc.update()

                    
                    writing.hideturtle()
                    writing.penup()
                    writing.goto(300, -300)
                    writing.write("""RESET""", font=("Verdana", 15, "normal"))

                    square4 = turtle.Turtle()
                    square4.speed(0)
                    square4.penup()
                    square4.goto(s3x, s3y)
                    square4.color("red")
                    square4.shape("square")
                    square4.shapesize(stretch_wid=2.4, stretch_len=2.4)

                    square5 = turtle.Turtle()
                    square5.speed(0)
                    square5.penup()
                    square5.goto(s4x, s4y)
                    square5.color("blue")
                    square5.shape("square")
                    square5.shapesize(stretch_wid=2.4, stretch_len=2.4)

                    circle1.showturtle()
                    circle1.color("red")
                    circle1.speed(0)
                    circle1.penup()
                    circle1.goto(c3x, c3y)
                    circle1.shape("circle")
                    circle1.shapesize(stretch_wid=2.4, stretch_len=2.4)

                    circle2.showturtle()
                    circle2.speed(0)
                    circle2.color("blue")
                    circle2.penup()
                    circle2.goto(c4x, c4y)
                    circle2.shape("circle")
                    circle2.shapesize(stretch_wid=2.4, stretch_len=2.4)

                    def get_mouse_click_coord3(x, y):
                        if square4.xcor() - 25 <= x <= square4.xcor() + 25 and square4.ycor() - 25 <= y <= square4.ycor() + 25:
                            square4.clear()
                            sc.update()
                            x1 = square4.xcor()
                            x1 -= 50.0
                            square4.setx(x1) 
                        if square5.xcor() - 25 <= x <= square5.xcor() + 25 and square5.ycor() - 25 <= y <= square5.ycor() + 25:
                            square5.clear()
                            sc.update()
                            y2 = square5.ycor()
                            y2 += 50.0
                            square5.sety(y2)
                        if square5.ycor() == square4.ycor() and square5.xcor() == square4.xcor():
                                y1 = square4.ycor()
                                y1 += 50
                                square4.sety(y1)
                        if 300 - 25 <= x <= 300 + 25 and -300 - 25 <= y <= -300 + 25:
                                square4.goto(s3x, s3y)
                                square5.goto(s4x, s4y)
                        if square4.xcor() == circle1.xcor() and square4.ycor() == circle1.ycor() and square5.xcor() == circle2.xcor() and square5.ycor() == circle2.ycor():
                            s5x = 0+200
                            s5y = 0-250
                            s6x = 0+150
                            s6y = 0-250
                            c5x = 0-100
                            c5y = 0-250
                            c6x = 0-100
                            c6y = 0+50
                    
                            square4.clear()
                            square4.hideturtle()
                            square5.clear()
                            square5.hideturtle()
                            circle1.clear()
                            circle1.hideturtle()
                            circle2.clear()
                            circle2.hideturtle()
                            arrow1.clear()
                            arrow1.hideturtle()
                            arrow2.clear()
                            arrow2.hideturtle()
                            
                            write.hideturtle()
                            write.penup()
                            write.goto(-75, 0)
                            write.write("""You have got this!!!""", font=("Verdana", 15, "normal"))
                            time.sleep(.75)
                            write.clear()
                            sc.update()

                            writing.hideturtle()
                            writing.penup()
                            writing.goto(300, -300)
                            writing.write("""RESET""", font=("Verdana", 15, "normal"))

                            square6 = turtle.Turtle()
                            square6.speed(0)
                            square6.penup()
                            square6.goto(s5x, s5y)
                            square6.color("red")
                            square6.shape("square")
                            square6.shapesize(stretch_wid=2.4, stretch_len=2.4)

                            square7 = turtle.Turtle()
                            square7.speed(0)
                            square7.penup()
                            square7.goto(s6x, s6y)
                            square7.color("blue")
                            square7.shape("square")
                            square7.shapesize(stretch_wid=2.4, stretch_len=2.4)

                            circle1.showturtle()
                            circle1.color("red")
                            circle1.speed(0)
                            circle1.penup()
                            circle1.goto(c5x, c5y)
                            circle1.shape("circle")
                            circle1.shapesize(stretch_wid=2.4, stretch_len=2.4)

                            circle2.showturtle()
                            circle2.speed(0)
                            circle2.color("blue")
                            circle2.penup()
                            circle2.goto(c6x, c6y)
                            circle2.shape("circle")
                            circle2.shapesize(stretch_wid=2.4, stretch_len=2.4)

                            def get_mouse_click_coord4(x, y):
                                if square6.xcor() - 25 <= x <= square6.xcor() + 25 and square6.ycor() - 25 <= y <= square6.ycor() + 25:
                                    square6.clear()
                                    sc.update()
                                    x1 = square6.xcor()
                                    x1 -= 50.0
                                    square6.setx(x1) 
                                if square7.xcor() - 25 <= x <= square7.xcor() + 25 and square7.ycor() - 25 <= y <= square7.ycor() + 25:
                                    square7.clear()
                                    sc.update()
                                    y2 = square7.ycor()
                                    y2 += 50.0
                                    square7.sety(y2)
                                if square7.ycor() == square6.ycor() and square7.xcor() == square6.xcor():
                                    y1 = square6.ycor()
                                    y1 += 50
                                    square6.sety(y1)
                                if 300 - 25 <= x <= 300 + 25 and -300 - 25 <= y <= -300 + 25:
                                    square6.goto(s5x, s5y)
                                    square7.goto(s6x, s6y)
                                if square6.xcor() == circle1.xcor() and square6.ycor() == circle1.ycor() and square7.xcor() == circle2.xcor() and square7.ycor() == circle2.ycor():
                                    s7x = 0
                                    s7y = 150
                                    s8x = 0
                                    s8y = -20
                                    c7x = -200
                                    c7y = 200
                                    c8x = 0
                                    c8y = 250
                    
                                    square6.clear()
                                    square6.hideturtle()
                                    square7.clear()
                                    square7.hideturtle()
                                    circle1.clear()
                                    circle1.hideturtle()
                                    circle2.clear()
                                    circle2.hideturtle()
                                    arrow1.clear()
                                    arrow1.hideturtle()
                                    arrow2.clear()
                                    arrow2.hideturtle()

                                    write = turtle.Turtle()
                                    write.hideturtle()
                                    write.penup()
                                    write.goto(-75, 0)
                                    write.write("""Blocks are able to move each other!!!""", font=("Verdana", 15, "normal"))
                                    time.sleep(.75)
                                    write.clear()
                                    sc.update()

                                    square8 = turtle.Turtle()
                                    square8.speed(0)
                                    square8.penup()
                                    square8.goto(s7x, s7y)
                                    square8.color("red")
                                    square8.shape("square")
                                    square8.shapesize(stretch_wid=2.4, stretch_len=2.4)

                                    square9 = turtle.Turtle()
                                    square9.speed(0)
                                    square9.penup()
                                    square9.goto(s8x, s8y)
                                    square9.color("blue")
                                    square9.shape("square")
                                    square9.shapesize(stretch_wid=2.4, stretch_len=2.4)

                                    circle1.showturtle()
                                    circle1.color("red")
                                    circle1.speed(0)
                                    circle1.penup()
                                    circle1.goto(c7x, c7y)
                                    circle1.shape("circle")
                                    circle1.shapesize(stretch_wid=2.4, stretch_len=2.4)

                                    circle2.showturtle()
                                    circle2.speed(0)
                                    circle2.color("blue")
                                    circle2.penup()
                                    circle2.goto(c8x, c8y)
                                    circle2.shape("circle")
                                    circle2.shapesize(stretch_wid=2.4, stretch_len=2.4)

                                    def get_mouse_click_coord5(x, y):
                                        if square8.xcor() - 25 <= x <= square8.xcor() + 25 and square8.ycor() - 25 <= y <= square8.ycor() + 25:
                                            square8.clear()
                                            sc.update()
                                            x1 = square8.xcor()
                                            x1 -= 50.0
                                            square8.setx(x1) 
                                        if square9.xcor() - 25 <= x <= square9.xcor() + 25 and square9.ycor() - 25 <= y <= square9.ycor() + 25:
                                            square9.clear()
                                            sc.update()
                                            y2 = square9.ycor()
                                            y2 += 50.0
                                            square9.sety(y2)
                                        if square9.ycor() == square8.ycor() and square9.xcor() == square8.xcor():
                                            y1 = square8.ycor()
                                            y1 += 50
                                            square8.sety(y1)
                                        if 300 - 25 <= x <= 300 + 25 and -300 - 25 <= y <= -300 + 25:
                                            square8.goto(s7x, s7y)
                                            square9.goto(s8x, s8y)
                                        if square8.xcor() == circle1.xcor() and square8.ycor() == circle1.ycor() and square9.xcor() == circle2.xcor() and square9.ycor() == circle2.ycor():
                                            s9x = 0
                                            s9y = 150
                                            s10x = 0
                                            s10y = -20
                                            c9x = -200
                                            c9y = 200
                                            c10x = 0
                                            c10y = 250
                                    
                                            square8.clear()
                                            square8.hideturtle()
                                            square9.clear()
                                            square9.hideturtle()
                                            circle1.clear()
                                            circle1.hideturtle()
                                            circle2.clear()
                                            circle2.hideturtle()
                                            arrow1.clear()
                                            arrow1.hideturtle()
                                            arrow2.clear()
                                            arrow2.hideturtle()
                                            
                                            write.hideturtle()
                                            write.penup()
                                            write.goto(-75, 0)
                                            write.write("""You have got this!!!""", font=("Verdana", 15, "normal"))
                                            time.sleep(.75)
                                            write.clear()
                                            sc.update()

                                            writing.hideturtle()
                                            writing.penup()
                                            writing.goto(300, -300)
                                            writing.write("""RESET""", font=("Verdana", 15, "normal"))

                                            square10 = turtle.Turtle()
                                            square10.showturtle()
                                            square10.speed(0)
                                            square10.penup()
                                            square10.goto(s9x, s9y)
                                            square10.color("red")
                                            square10.shape("square")
                                            square10.shapesize(stretch_wid=2.4, stretch_len=2.4)

                                            square11 = turtle.Turtle()
                                            square11.showturtle()
                                            square11.speed(0)
                                            square11.penup()
                                            square11.goto(s10x, s10y)
                                            square11.color("blue")
                                            square11.shape("square")
                                            square11.shapesize(stretch_wid=2.4, stretch_len=2.4)

                                            circle1.showturtle()
                                            circle1.color("red")
                                            circle1.speed(0)
                                            circle1.penup()
                                            circle1.goto(c9x, c9y)
                                            circle1.shape("circle")
                                            circle1.shapesize(stretch_wid=2.4, stretch_len=2.4)

                                            circle2.showturtle()
                                            circle2.speed(0)
                                            circle2.color("blue")
                                            circle2.penup()
                                            circle2.goto(c10x, c10y)
                                            circle2.shape("circle")
                                            circle2.shapesize(stretch_wid=2.4, stretch_len=2.4)

                                            def get_mouse_click_coord6(x, y):
                                                if square10.xcor() - 25 <= x <= square10.xcor() + 25 and square10.ycor() - 25 <= y <= square10.ycor() + 25:
                                                    square10.clear()
                                                    sc.update()
                                                    x1 = square10.xcor()
                                                    x1 -= 50.0
                                                    square10.setx(x1) 
                                                if square11.xcor() - 25 <= x <= square11.xcor() + 25 and square11.ycor() - 25 <= y <= square11.ycor() + 25:
                                                    square11.clear()
                                                    sc.update()
                                                    y2 = square11.ycor()
                                                    y2 += 50.0
                                                    square11.sety(y2)
                                                    if square11.ycor() == square10.ycor() and square11.xcor() == square10.xcor():
                                                        y1 = square10.ycor()
                                                        y1 += 50
                                                        square10.sety(y1)
                                                if 300 - 25 <= x <= 300 + 25 and -300 - 25 <= y <= -300 + 25:
                                                    square1.goto(s9x, s9y)
                                                    square11.goto(s10x, s10y)
                                                if square10.xcor() == circle1.xcor() and square10.ycor() == circle1.ycor() and square11.xcor() == circle2.xcor() and square11.ycor() == circle2.ycor():
                                                    print("works")

                                            turtle.onscreenclick(get_mouse_click_coord6)
                                            turtle.mainloop()

                                    turtle.onscreenclick(get_mouse_click_coord5)
                                    turtle.mainloop()
                                            
                            turtle.onscreenclick(get_mouse_click_coord4)
                            turtle.mainloop()

                    turtle.onscreenclick(get_mouse_click_coord3)
                    turtle.mainloop()

            turtle.onscreenclick(get_mouse_click_coord2)
            turtle.mainloop()

turtle.onscreenclick(get_mouse_click_coor1)
turtle.mainloop()

turtle.done()



































import turtle
import time

# screen color
sc = turtle.Screen()
sc.bgcolor("Gray")

# text
write = turtle.Turtle()
write.hideturtle()
write.penup()
write.goto(-175, 0)
write.write("""Move square by using the mouse to click on it""", font=("Verdana", 15, "normal"))
time.sleep(1.75)
write.clear()
sc.update()

# stage 1

# object 1: stage 1
square = turtle.Turtle()
square.speed(0)
square.penup()
square.goto(0, 200.0)
square.color("red")
square.shape("square")
square.shapesize(stretch_wid=2.4, stretch_len=2.4)

arrow = turtle.Turtle()
arrow.speed(0)
arrow.penup()
arrow.right(90)
arrow.goto(square.xcor(), square.ycor())
arrow.color("gray")
arrow.shape("triangle")
arrow.shapesize(stretch_wid=1.2, stretch_len=1.2)


# object 3: stage 1
circle = turtle.Turtle()
circle.color("red")
circle.penup()
circle.goto(0, -50.0)
circle.shape("circle")
circle.shapesize(stretch_wid=2.4, stretch_len=2.4)

def get_mouse_click_coor(x, y):
    print(x, y)
    if square.xcor() - 25 <= x <= square.xcor() + 25 and square.ycor() - 25 <= y <= square.ycor() + 25:
        square.clear()
        sc.update()
        y1 = square.ycor()
        y1 -= 50.0
        square.sety(y1) 
        arrow.goto(square.xcor(),square.ycor())
    
# stage 2
        if y1 == -50:
            s1x = 0
            s1y = 200
            s2x = 0
            s2y = -200
                
            circle.clear()
            square.clear()
            arrow.clear()
            circle.hideturtle()
            square.hideturtle()
            arrow.hideturtle()

            write1 = turtle.Turtle()
            write1.hideturtle()
            write1.penup()
            write1.goto(-125, 0)
            write1.write("""The further you go the harder it is""", font=("Verdana", 15, "normal"))
            time.sleep(1)
            write1.clear()
            sc.update()
    
            writing = turtle.Turtle()
            writing.hideturtle()
            writing.penup()
            writing.goto(300, -300)
            writing.write("""RESET""", font=("Verdana", 15, "normal"))

            
# object 1: stage 2
            square1 = turtle.Turtle()
            square1.speed(0)
            square1.penup()
            square1.goto(s1x, s1y)
            square1.color("red")
            square1.shape("square")
            square1.shapesize(stretch_wid=2.4, stretch_len=2.4)

# object 2: stage 2
            square2 = turtle.Turtle()
            square2.speed(0)
            square2.penup()
            square2.goto(s2x, s2y)
            square2.color("blue")
            square2.shape("square")
            square2.shapesize(stretch_wid=2.4, stretch_len=2.4)

# object 3: stage 2
            arrow1 = turtle.Turtle()
            arrow1.speed(0)
            arrow1.penup()
            arrow1.right(90)
            arrow1.goto(square1.xcor(), square1.ycor())
            arrow1.color("gray")
            arrow1.shape("triangle")
            arrow1.shapesize(stretch_wid=1.2, stretch_len=1.2)
            arrow1.right(90)

# object 3: stage 2
            arrow2 = turtle.Turtle()
            arrow2.speed(0)
            arrow2.penup()
            arrow2.right(90)
            arrow2.goto(square2.xcor(), square2.ycor())
            arrow2.color("gray")
            arrow2.shape("triangle")
            arrow2.shapesize(stretch_wid=1.2, stretch_len=1.2)
            arrow2.left(180)

# object 4: stage 2
            circle1 = turtle.Turtle()
            circle1.color("red")
            circle1.speed(0)
            circle1.penup()
            circle1.goto(-200, 200)
            circle1.shape("circle")
            circle1.shapesize(stretch_wid=2.4, stretch_len=2.4)

# object 3: stage 2
            circle2 = turtle.Turtle()
            circle2.speed(0)
            circle2.color("blue")
            circle2.penup()
            circle2.goto(0, 150)
            circle2.shape("circle")
            circle2.shapesize(stretch_wid=2.4, stretch_len=2.4)

            def get_mouse_click_coord(x, y):
                print(x, y)
                print(square1.xcor(), square1.ycor())
                if square1.xcor() - 25 <= x <= square1.xcor() + 25 and square1.ycor() - 25 <= y <= square1.ycor() + 25:
                    square1.clear()
                    sc.update()
                    x1 = square1.xcor()
                    x1 -= 50.0
                    square1.setx(x1)
                    arrow1.goto(square1.xcor(),square1.ycor()) 
                if square2.xcor() - 25 <= x <= square2.xcor() + 25 and square2.ycor() - 25 <= y <= square2.ycor() + 25:
                    square2.clear()
                    sc.update()
                    y2 = square2.ycor()
                    y2 += 50.0
                    square2.sety(y2)
                    arrow2.goto(square2.xcor(),square2.ycor())
                    if square2.ycor() == square1.ycor() and square2.xcor() == square1.xcor():
                        y1 = square1.ycor()
                        y1 += 50
                        square1.sety(y1)
                        arrow1.goto(square1.xcor(),square1.ycor())
                if writing.xcor() - 25 <= x <= writing.xcor() + 25 and writing.ycor() - 25 <= y <= writing.ycor() + 25:
                    square1.goto(s1x, s1y)
                    square2.goto(s2x, s2y)
                if square1.xcor() == circle1.xcor() and square1.ycor() == circle1.ycor() and square2.xcor() == circle2.xcor() and square2.ycor() == circle2.ycor():
                    s3x = 0
                    s3y = 150
                    s4x = 0
                    s4y = -20
                    c3x = -200
                    c3y = 200
                    c4x = 0
                    c4y = 250
                    
                    square1.clear()
                    square1.hideturtle()
                    square2.clear()
                    square2.hideturtle()
                    circle1.clear()
                    circle1.hideturtle()
                    circle2.clear()
                    circle2.hideturtle()

                    write2 = turtle.Turtle()
                    write2.hideturtle()
                    write2.penup()
                    write2.goto(-75, 0)
                    write2.write("""You have got this!!!""", font=("Verdana", 15, "normal"))
                    time.sleep(.75)
                    write2.clear()
                    sc.update()


                    # object 1: stage 2
                    square3 = turtle.Turtle()
                    square3.speed(0)
                    square3.penup()
                    square3.goto(s3x, s3y)
                    square3.color("red")
                    square3.shape("square")
                    square3.shapesize(stretch_wid=2.4, stretch_len=2.4)

# object 1: stage 3
                    square4 = turtle.Turtle()
                    square4.speed(0)
                    square4.penup()
                    square4.goto(s4x, s4y)
                    square4.color("blue")
                    square2.shape("square")
                    square2.shapesize(stretch_wid=2.4, stretch_len=2.4)

 # object 2: stage 3
                    circle3 = turtle.Turtle()
                    circle3.color("red")
                    circle3.speed(0)
                    circle3.penup()
                    circle3.goto(c3x, c3y)
                    circle3.shape("circle")
                    circle3.shapesize(stretch_wid=2.4, stretch_len=2.4)

# object 3: stage 3
                    circle4 = turtle.Turtle()
                    circle4.speed(0)
                    circle4.color("blue")
                    circle4.penup()
                    circle4.goto(c4x, c4y)
                    circle4.shape("circle")
                    circle4.shapesize(stretch_wid=2.4, stretch_len=2.4)

                    def get_mouse_click_coord(x, y):
                        print(x, y)
                        print(square1.xcor(), square1.ycor())
                        if square1.xcor() - 25 <= x <= square1.xcor() + 25 and square1.ycor() - 25 <= y <= square1.ycor() + 25:
                            square1.clear()
                            sc.update()
                            x1 = square1.xcor()
                            x1 -= 50.0
                            square1.setx(x1) 
                        if square2.xcor() - 25 <= x <= square2.xcor() + 25 and square2.ycor() - 25 <= y <= square2.ycor() + 25:
                            square2.clear()
                            sc.update()
                            y2 = square2.ycor()
                            y2 += 50.0
                            square2.sety(y2)
                            if square2.ycor() == square1.ycor() and square2.xcor() == square1.xcor():
                                y1 = square1.ycor()
                                y1 += 50
                                square1.sety(y1)
                        if writing.xcor() - 25 <= x <= writing.xcor() + 25 and writing.ycor() - 25 <= y <= writing.ycor() + 25:
                            square1.goto(s1x, s1y)
                            square2.goto(s2x, s2y)
                        if square1.xcor() == circle1.xcor() and square1.ycor() == circle1.ycor() and square2.xcor() == circle2.xcor() and square2.ycor() == circle2.ycor():
                            s5x = 0
                            s5y = 150
                            s6x = 0
                            s6y = -20
                            c5x = -200
                            c5y = 200
                            c6x = 0
                            c6y = 250
                    
                            square3.hideturtle()
                            square4.hideturtle()
                            circle3.hideturtle()
                            circle4.hideturtle()
                            arrow1.hideturtle
                            arrow2.hideturtle()
                            
                            write2 = turtle.Turtle()
                            write2.hideturtle()
                            write2.penup()
                            write2.goto(-75, 0)
                            write2.write("""You have got this!!!""", font=("Verdana", 15, "normal"))
                            time.sleep(.75)
                            write2.clear()
                            sc.update()

# indent this for stage 3
                    # object 1: stage 2
                    square3 = turtle.Turtle()
                    square3.speed(0)
                    square3.penup()
                    square3.goto(s3x, s3y)
                    square3.color("red")
                    square3.shape("square")
                    square3.shapesize(stretch_wid=2.4, stretch_len=2.4)

# object 1: stage 3
                    square4 = turtle.Turtle()
                    square4.speed(0)
                    square4.penup()
                    square4.goto(s4x, s4y)
                    square4.color("blue")
                    square2.shape("square")
                    square2.shapesize(stretch_wid=2.4, stretch_len=2.4)

 # object 2: stage 3
                    circle3 = turtle.Turtle()
                    circle3.color("red")
                    circle3.speed(0)
                    circle3.penup()
                    circle3.goto(c3x, c3y)
                    circle3.shape("circle")
                    circle3.shapesize(stretch_wid=2.4, stretch_len=2.4)

# object 3: stage 3
                    circle4 = turtle.Turtle()
                    circle4.speed(0)
                    circle4.color("blue")
                    circle4.penup()
                    circle4.goto(c4x, c4y)
                    circle4.shape("circle")
                    circle4.shapesize(stretch_wid=2.4, stretch_len=2.4)

                    def get_mouse_click_coord(x, y):
                        print(x, y)
                        print(square1.xcor(), square1.ycor())
                        if square1.xcor() - 25 <= x <= square1.xcor() + 25 and square1.ycor() - 25 <= y <= square1.ycor() + 25:
                            square1.clear()
                            sc.update()
                            x1 = square1.xcor()
                            x1 -= 50.0
                            square1.setx(x1) 
                        if square2.xcor() - 25 <= x <= square2.xcor() + 25 and square2.ycor() - 25 <= y <= square2.ycor() + 25:
                            square2.clear()
                            sc.update()
                            y2 = square2.ycor()
                            y2 += 50.0
                            square2.sety(y2)
                            if square2.ycor() == square1.ycor() and square2.xcor() == square1.xcor():
                                y1 = square1.ycor()
                                y1 += 50
                                square1.sety(y1)
                        if writing.xcor() - 25 <= x <= writing.xcor() + 25 and writing.ycor() - 25 <= y <= writing.ycor() + 25:
                            square1.goto(s1x, s1y)
                            square2.goto(s2x, s2y)
                        if square1.xcor() == circle1.xcor() and square1.ycor() == circle1.ycor() and square2.xcor() == circle2.xcor() and square2.ycor() == circle2.ycor():

                    turtle.onscreenclick(get_mouse_click_coord)
                    turtle.mainloop()



            turtle.onscreenclick(get_mouse_click_coord)
            turtle.mainloop()
   
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

turtle.done()
