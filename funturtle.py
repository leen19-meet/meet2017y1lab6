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

direction = UP

def up():
    global direction
    direction = UP
    print("you pressed UP")
def down():
    global direction
    direction = DOWN
    print("you pressed down")
def left():
    global direction
    direction = LEFT
def right():
    global direction
    direction = RIGHT
