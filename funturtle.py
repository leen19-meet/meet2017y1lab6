def up():
    global direction
    direction = UP
    print("you pressed UP")
    old_pos= turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x, y+10)
    print(turtle.pos())
def down():
    global direction
    direction = DOWN
    print("you pressed down")
    old_pos= turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x, y-10)
    print(turtle.pos())
def left():
    global direction
    direction = LEFT
    print("you pressed left")
    old_pos= turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x-10, y)
    print(turtle.pos())
def right():
    global direction
    direction = RIGHT
    print("you pressed right")
    old_pos= turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x+10, y)
    print(turtle.pos())
def spaces():S
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()


################################################333

import turtle

##
##leen= turtle.clone()
##turtle.shape("square")
##leen.shape("circle")
##
##leen.goto(100,100)
##turtle.mainloop()

##square = turtle.clone()
##
##square.shape('square')
##square.goto(100,0)
##square.goto(100,100)
##square.goto(0,100)
##square.goto(0,0)
##square.mainloop()

##turtle.shape('turtle')
##square= turtle.clone()
##square.shape('square')
##square.goto(100,100)
##
##square.goto(300,300)
##square.stamp()
##square.goto(100,100)
##turtle.mainloop()

UP= 0
LEFT= 1
DOWN= 2
RIGHT= 3

UP_ARROW = "Up"
DOWN_ARROW = "Down"
LEFT_ARROW = "Left"
RIGHT_ARROW = "Right"
SPACEBAR = "space"

direction = UP

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(spaces, SPACEBAR)
turtle.listen()

turtle.mainloop()
