def my_function():
  print("hello world")
  print("Bye")


def turn_left():
  print("turn left")


def turn_right():
  print("turn right")
  turn_left()

def move():
  print("move")
my_function()
turn_right()


def square():
  turn_right()
  turn_right()

def jump():
  move()
  turn_right()



  for step in range(6):
    jump()

  
  number_of_hurdles = 6

  while number_of_hurdles < 6: 
    jump()
    number_of_hurdles -= 1

#     while jump() !True:
#       jump()

#     while not at_goal():
    
#     The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.