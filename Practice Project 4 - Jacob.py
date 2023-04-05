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
