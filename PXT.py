import turtle

t = turtle.Turtle()

t.pencolor("black")



def draw_line(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)

def draw_rectangle(x0, y0, len, hgt, clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0, y0, x0+len, y0)
    draw_line(x0+len, y0, x0+len, y0+hgt)
    draw_line(x0+len, y0+hgt, x0, y0+hgt)
    draw_line(x0, y0+hgt, x0, y0)
    t.end_fill()

ts.tracer(0)

n_cols = 25
x_val = -100
y_val = 0



for rr in range(n_cols):
    if rr < 5:
       draw_rectangle(x_val, y_val, 20, 20, "red")
    elif rr > 4 and rr < 15:
       draw_rectangle(x_val, y_val, 20, 20, "blue")
    elif rr > 3 and rr < 10:
        draw_rectangle(x_val,y_val, 20, 20, "yellow")
    else:
       draw_rectangle(x_val, y_val, 20, 20, "green")
    x_val = x_val + 20
