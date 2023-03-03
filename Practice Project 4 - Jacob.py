import turtle
import time

# screen color
sc = turtle.Screen()
sc.bgcolor("Gray")

# text
write = turtle.Turtle()
write.hideturtle()
write.penup()
write.goto(-200, 0)
write.write("Press down arrow to move red and W key to move blue", font=("Verdana", 15, "normal"))
time.sleep(1)
write.clear()


    # object 1: stage 1
    square1 = turtle.Turtle()
    square1.speed(0)
    square1.hideturtle()
    square1.penup()
    square1.goto(-50, 200)
    square1.pendown()
    def sqre1():
        square1.fillcolor("red")
        square1.begin_fill()
        square1.color("red")
        for _ in range(4):
            square1.forward(100)
            square1.left(90)
            square1.end_fill()
    sqre1()

# object 2: stage 1
circle1 = turtle.Turtle()
circle1.hideturtle()
#circle1.goto()
circle1.shape("circle")
circle1.shapesize(stretch_wid=4, stretch_len=4)

# stage 2
if square1.ycor() == "":
# object 1: stage 2
    square1 = turtle.Turtle()
    square1.speed(0)
    square1.hideturtle()
    square1.penup()
    square1.goto(-50, 200)
    square1.pendown()
    def sqre1():
        square1.fillcolor("red")
        square1.begin_fill()
        square1.color("red")
        for _ in range(4):
            square1.forward(100)
            square1.left(90)
        square1.end_fill()
    sqre1()

# object 2: stage 2
    square2 = turtle.Turtle()
    square2.speed(0)
    square2.hideturtle()
    square2.penup()
    square2.goto(-50, -200)
    square2.pendown()
    def sqre2():
        square2.fillcolor("red")
        square2.begin_fill()
        square2.color("blue")
        for _ in range(4):
            square2.forward(100)
            square2.left(90)
        square2.end_fill()
    sqre2()

# object 3: stage 2
    circle1 = turtle.Turtle()
    circle1.hideturtle()
    #circle1.goto()
    circle1.shape("circle")
    circle1.shapesize(stretch_wid=4, stretch_len=4)

# object 4: stage 2
    circle2 = turtle.Turtle()
    circle2.hideturtle()
    #circle2.goto()
    circle2.shape("circle")
    circle2.shapesize(stretch_wid=4, stretch_len=4)

    def square1down():
        square1.clear()
        sc.update()
        y = square1.ycor()
        y -= 100
        square1.sety(y)        
        sqre1()
    
    def square2up():
        square2.clear()
        sc.update()
        y = square2.ycor()
        y += 100
        square2.penup()
        square2.sety(y)  
        square2.pendown()      
        sqre2()



turtle.onkey(square1down, 'Down')
turtle.onkey(square2up, 'w')
turtle.listen()



error = turtle.Turtle()
while 0 == 0:
    error.hideturtle()
    error.penup()
    error.goto(1000, 1000)
    error.pendown()
    for _ in range(4):
        error.forward(100)
        error.left(90)


turtle.done()
