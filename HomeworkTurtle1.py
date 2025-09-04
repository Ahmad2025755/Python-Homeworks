import turtle

turtle.Screen().bgcolor("Green")

pen = turtle.Turtle()

# Circle

pen.circle(100) 

#end

pen.penup()
pen.forward(150)  
pen.pendown()


# Square

pen.forward(100)
pen.left(90)

pen.forward(100)
pen.left(90)

pen.forward(100)
pen.left(90)

pen.forward(100)
pen.left(90)

#end

pen.penup()
pen.forward(150)
pen.pendown()

# Triangle

pen.pendown()
pen.right(90)
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.right(120)
pen.foward(100) 





turtle.done()