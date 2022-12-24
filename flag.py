#Bangladesh Flag with Python


import turtle

        ###------flag------###

 

obj=turtle.Turtle()
obj.speed(1)

win=turtle.Screen()
win.bgcolor("gray")

######## green field start ###########

obj.penup()
obj.goto(-100,150)
obj.pendown()
obj.begin_fill()
obj.fillcolor("seagreen")
obj.setheading(0)
obj.forward(250)
obj.setheading(270)
obj.forward(150)
obj.setheading(180)
obj.forward(250)
obj.setheading(90)
obj.forward(150)
obj.end_fill()


obj.setheading(270)
obj.forward(122)
obj.setheading(360)

obj.penup()
obj.forward(120)
obj.pendown()

###### Green Field End ######

###### Red Field Start ######



obj.begin_fill()
obj.fillcolor("red")
obj.circle(50)
obj.end_fill() 

###### red Field End ######


### Pillar ###
obj.setheading(180)
obj.penup()
obj.forward(120)
obj.pendown()

obj.begin_fill()
obj.fillcolor("orange")


obj.setheading(90)
obj.forward(150)
obj.setheading(180)
obj.forward(20)
obj.setheading(270)
obj.forward(400)
obj.setheading(180)
obj.forward(50)
obj.setheading(270)
obj.forward(30)
obj.setheading(360)
obj.forward(120)
obj.setheading(90)
obj.forward(30)
obj.setheading(180)
obj.forward(50)
obj.setheading(90)
obj.forward(400)
obj.end_fill()

 



obj.hideturtle()

turtle.done()

#thank you all
 