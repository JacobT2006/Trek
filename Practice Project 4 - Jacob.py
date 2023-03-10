import turtle
import time

a = 1
b = 2

# screen color
sc = turtle.Screen()
sc.bgcolor("Gray")


# text
write = turtle.Turtle()
write.hideturtle()
write.penup()
write.goto(-150, 0)
write.write("""Press 1 key to move red square to red circle
and 2 key to move blue square to blue circle""", font=("Verdana", 15, "normal"))
time.sleep(1)
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


# object 2: stage 1
circle = turtle.Turtle()
circle.color("red")
circle.penup()
circle.goto(0, -50.0)
circle.shape("circle")
circle.shapesize(stretch_wid=2.4, stretch_len=2.4)

# object 3: stage 1
# arrow = turtle.Turtle()
# arrow.shape("arrow")
# arrow.penup()
# arrow.shapesize(stretch_wid=1, stretch_len=2)
# arrow.goto(square.xcor(), square.ycor())
# arrow.towards(circle.xcor(), circle.ycor())
# if arrow.xcor() != square.xcor() and arrow.ycor() != square.ycor():
#     arrow.goto(square.xcor(), square.ycor())

def squaredown():
        square.clear()
        sc.update()
        y = square.ycor()
        y -= 50.0
        square.sety(y)    
        
# stage 2
        if y == -50:
            circle.clear()
            square.clear()
            #arrow.clear()
            circle.hideturtle()
            square.hideturtle()
            #arrow.hideturtle()
            sc.update()
    
    
# object 1: stage 2
            square1 = turtle.Turtle()
            square1.speed(0)
            square1.penup()
            square1.goto(0, 200)
            square1.color("red")
            square1.shape("square")
            square1.shapesize(stretch_wid=2.4, stretch_len=2.4)

# object 2: stage 2
            square2 = turtle.Turtle()
            square2.speed(0)
            square2.penup()
            square2.goto(0, -200)
            square2.color("blue")
            square2.shape("square")
            square2.shapesize(stretch_wid=2.4, stretch_len=2.4)

 # object 3: stage 2
            circle1 = turtle.Turtle()
            circle1.color("red")
            circle1.penup()
            circle1.goto(-200, 200)
            circle1.shape("circle")
            circle1.shapesize(stretch_wid=2.4, stretch_len=2.4)

# object 4: stage 2
            circle2 = turtle.Turtle()
            circle2.color("blue")
            circle2.penup()
            circle2.goto(0, 150)
            circle2.shape("circle")
            circle2.shapesize(stretch_wid=2.4, stretch_len=2.4)


            def square1side():
                square1.clear()
                sc.update()
                x = square1.xcor()
                x -= 50
                square1.setx(x)
                if (square1.xcor() == circle1.xcor() and square1.ycor() == circle1.ycor()) and (square2.xcor() == circle2.xcor() and square2.ycor() == circle2.ycor()):
                    square1.clear()
                    square2.clear()
                    circle1.clear()
                    circle2.clear()
                    

            def square2up():
                square2.clear()
                sc.update()
                y = square2.ycor()
                y += 50
                square2.sety(y)
                if square2.ycor() == square1.ycor() and square2.xcor() == square1.xcor():
                    y = square1.ycor()
                    y += 50
                    square1.sety(y)
                if (square1.xcor() == circle1.xcor() and square1.ycor() == circle1.ycor()) and (square2.xcor() == circle2.xcor() and square2.ycor() == circle2.ycor()):
                    run3()
        
            turtle.listen()
            turtle.onkey(square1side, '1')
            turtle.onkey(square2up, '2')






        
turtle.listen()
turtle.onkey(squaredown, '1')

turtle.done()
