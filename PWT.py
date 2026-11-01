import turtle

t = turtle.Turtle()


input()

t.penup()
t.fillcolor('beige')
t.pencolor("black")
t.pensize(5)
t.begin_fill()
t.goto(-100,-100)

t.pendown()
t.goto(-100, 100)
t.goto(-60, 100)
t.goto(-60, 40)
t.goto(-20, 40)
t.goto(-20, 100)
t.goto(20, 100)
t.goto(20, 40)
t.goto(60, 40)
t.goto(60, 100)
t.goto(100, 100)
t.goto(100, -100)
t.goto(-100, -100)
t.end_fill()
turtle.done()


