import turtle as trtl
import random as rand

t = trtl.Turtle()
mainpiece = trtl.Turtle(shape = "turtle")

t.pensize(10)
t.speed(0)
sumnum = 20
path_width = 25
wall_len = path_width

def turl():
  for h in range (sumnum):
    global wall_len
    wall_len = wall_len + path_width
    if (h > 4):
      t.left(90)
      door = rand.randint(path_width*2, (wall_len - path_width*2))
      barer = rand.randint(path_width*2, (wall_len - path_width*2))
      while abs(door-barer) < path_width:
        door = rand.randint(path_width*2, (wall_len - path_width*2))
      if (door < barer):
        dar(door)
        bare(barer - door - path_width*2)
        t.forward(wall_len - barer)
      else: 
        t.forward(wall_len - door - path_width*2)
        bare(barer)
        dar(door-barer)

def dar(forward):
    t.forward(forward)
    t.penup()
    t.forward(path_width * 2)
    t.pendown()

def bare(forward):
  t.forward(forward)
  t.left(90)
  t.forward(path_width*2)
  t.back(path_width*2)
  t.right(90)

def north():
  mainpiece.setheading(90)
  mainpiece.forward(1)

def west():
  mainpiece.setheading(270)
  mainpiece.forward(1)

def south():
  mainpiece.setheading(180)
  mainpiece.forward(1)

def east():
  mainpiece.setheading(0)
  mainpiece.forward(1)

turl()

mainpiece.goto(0,1)
wn = trtl.Screen()
wn.onkeypress(north, "w")
wn.onkeypress(west, "a")
wn.onkeypress(south, "s")
wn.onkeypress(east, "d")
wn.listen()
wn.mainloop()
