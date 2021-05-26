import turtle

print("Welcome to Better Turtle!")

wn = turtle.Screen()
wn.title("Better Turtle")
tk = turtle.Turtle()
def car():
    tk.color('#ff0000')
    tk.fillcolor('#ff0000')
    tk.penup()
    tk.goto(0,0)
    tk.pendown()
    tk.begin_fill()
    tk.forward(370)
    tk.left(90)
    tk.forward(50)
    tk.left(90)
    tk.forward(370)
    tk.left(90)
    tk.forward(50)
    tk.end_fill()
    
        
    # Below code for drawing window and roof
    tk.penup()
    tk.goto(100, 50)
    tk.pendown()
    tk.setheading(45)
    tk.forward(70)
    tk.setheading(0)
    tk.forward(100)
    tk.setheading(-45)
    tk.forward(70)
    tk.setheading(90)
    tk.penup()
    tk.goto(200, 50)
    tk.pendown()
    tk.forward(49.50)
    
        
    # Below code for drawing two tyres
    tk.penup()
    tk.goto(100, -10)
    tk.pendown()
    tk.color('#000000')
    tk.fillcolor('#000000')
    tk.begin_fill()
    tk.circle(20)
    tk.end_fill()
    tk.penup()
    tk.goto(300, -10)
    tk.pendown()
    tk.color('#000000')
    tk.fillcolor('#000000')
    tk.begin_fill()
    tk.circle(20)
    tk.end_fill()
def star():
    while True:
        tk.forward(200)
        tk.left(170)
        if abs(tk.pos()) < 1:
            break
while True:
    command = input("BetterTurtle@Console: ")
    if command == 'car':
        car()
    elif command == 'star':
        star()
    elif command == 'forward':
        howMuch = input("How much steps do you want the turtle to take? ")
        tk.forward(int(howMuch))
    elif command == 'left':
        howMuch_2 = input("How much degree do to turn? ")
        tk.left(int(howMuch_2))
    elif command == 'right':
        howMuch_2 = input("How much degree do to turn? ")
        tk.right(int(howMuch_2))
    elif command == 'circle':
        howMuch_2 = input("How much radius do you want in the circle? ")
        tk.circle(int(howMuch_2))
    elif command == 'quit':
        quit()
    else:
        print("Invalid command!")