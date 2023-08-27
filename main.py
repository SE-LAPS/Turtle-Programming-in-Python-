import turtle

turtle.setup(width=800, height=600)
screen = turtle.Screen()
screen.bgcolor("black")


turtle.register_shape("logo.gif")
turtle.register_shape("man-1.gif")
turtle.register_shape("man-2.gif")

turtle.delay(50)  # 1 millisecond delay

t = turtle.Turtle()
t.speed(1)

text_properties = [
    ("NSBM", "Arial", "blue", "italic", "bold"),
    ("GREEN", "Goudy Titling", "green", "normal", "bold"),
    ("UNIVERSITY", "Goudy Titling", "green", "normal", "bold"),
    ("TOWN", "Goudy Titling", "blue", "normal", "bold")
]

total_height = sum(40 for _, _, _, _, _ in text_properties)

y = total_height // 2

for text, font, color, style, weight in text_properties:
    t.penup()
    t.goto(80, y)
    t.color(color)
    t.pendown()
    t.write(text, align="center", font=(font, 30, style, weight))
    y -= 40

t.hideturtle()

image_turtle = turtle.Turtle()
image_turtle.penup()
image_turtle.goto(-120, 30)
image_turtle.shape("logo.gif")
image_turtle.shapesize(0.6)
image_turtle.stamp()


picture1_turtle = turtle.Turtle()
picture1_turtle.penup()
picture1_turtle.goto(30, 130)
picture1_turtle.shape("man-1.gif")
picture1_turtle.shapesize(0.1)
picture1_turtle.stamp()


picture2_turtle = turtle.Turtle()
picture2_turtle.penup()
picture2_turtle.goto(160, 130)
picture2_turtle.shape("man-2.gif")
picture2_turtle.shapesize(0.1)
picture2_turtle.stamp()


screen.exitonclick()
