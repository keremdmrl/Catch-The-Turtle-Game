import turtle
import random
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")
FONT = ("Arial", 20, "normal")
score = 0
game_over = False

grid_size = 15


skor_turtle = turtle.Turtle()

countdown_turtle = turtle.Turtle()

turtle_list = []

def setup_score_turtle():
    skor_turtle.speed('fastest')

    skor_turtle.color("black")
    skor_turtle.hideturtle()
    skor_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    skor_turtle.setpos(0,y)
    skor_turtle.write(arg='Score: 0', move=False, align='center', font=FONT)


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        skor_turtle.clear()
        skor_turtle.write(arg= 'Score: {}'.format(score), move=False, align='center', font=FONT)
        #print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.shape('turtle')
    t.color('green')
    t.shapesize(2,2)
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10,-20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    global game_over
    countdown_turtle.speed('fastest')
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    countdown_turtle.setpos(0, y - 30)

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg='time: {}'.format(time), move=False, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1),1000 )
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg='Game Over!'.format(time), move=False, align='center', font=FONT)

def start_game():
    turtle.tracer(0)

    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(30)

    turtle.tracer(1)

start_game()

'''
make_turtle(20,20)
make_turtle(10,20)
make_turtle(0,20)
make_turtle(-10,20)
make_turtle(-20,20)

make_turtle(20,10)
make_turtle(10,10)
make_turtle(0,10)
make_turtle(-10,10)
make_turtle(-20,10)

make_turtle(20,0)
make_turtle(10,0)
make_turtle(0,0)
make_turtle(-10,0)
make_turtle(-20,0)

make_turtle(20,-10)
make_turtle(10,-10)
make_turtle(0,-10)
make_turtle(-10,-10)
make_turtle(-20,-10)

make_turtle(20,-20)
make_turtle(10,-20)
make_turtle(0,-20)
make_turtle(-10,-20)
make_turtle(-20,-20)
'''

turtle.mainloop()