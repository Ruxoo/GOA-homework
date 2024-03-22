from turtle import *

speed()


width(7)
color("purple")
begin_fill()
forward(200)
left(90)



forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

#end of square


#drawing a door


forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)   #heigtht of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window 1

penup()
goto(190, 180)
pendown()
color("green")
begin_fill()
right(60)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

left(180)
forward(20)
color("black")
right(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)



#window 2

penup()
goto(20, 180)
pendown()
color("green")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

color("black")
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)


penup()
goto(20, 160)
pendown()
left(90)
forward(40)




exitonclick()
