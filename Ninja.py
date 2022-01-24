import turtle

imanNinja = turtle.Turtle()

for i in range(180):
    imanNinja.forward(100)
    imanNinja.right(30)
    imanNinja.forward(20)
    imanNinja.left(60)
    imanNinja.forward(50)
    imanNinja.right(30)

    imanNinja.penup()
    imanNinja.setposition(0,1)
    imanNinja.pendown()
    imanNinja.right(20)

turtle.done()