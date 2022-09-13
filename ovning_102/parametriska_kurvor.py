import turtle as t
import numpy as np
from operator import add
FONTSIZE = 24

def plot_descartes(origo):
    a = 250
    tim.color("light green")
    tim.penup()
    tim.goto(calc_function(0, origo, "a*t/(1+(t**3))", "a*(t**2)/(1+(t**3))", a))
    tim.pendown()

    t = np.arange(-0.5, 75, 0.1)
    for i in t:  # Ritar Descarts löv, övre delen + "lövet"
        if i == t[0]:
            tim.penup()
        tim.goto(calc_function(i, origo, "a*t/(1+(t**3))", "a*(t**2)/(1+(t**3))", a))
        tim.pendown()

    t = np.arange(-50, -2, 0.1)
    for i in t:  # Ritar Descarts löv, undre delen
        if i == t[0]:
            tim.penup()
        tim.goto(calc_function(i, origo, "a*t/(1+(t**3))", "a*(t**2)/(1+(t**3))", a))
        tim.pendown()

def plot_asteroid(origo, a, b):
    tim.color("yellow")
    tim.penup()
    tim.goto(calc_function(0, origo, "a*(np.cos(t)**3)", "b*(np.sin(t)**3)", a ,b))
    tim.pendown()

    t = np.arange(0, 2*np.pi, 0.05)

    for i in t:
        tim.goto(calc_function(i, origo, "a*(np.cos(t)**3)", "b*(np.sin(t)**3)", a, b))


def plot_lemniskata(origo):
    tim.color("light blue")
    tim.penup()
    tim.goto(calc_function(0, origo, "(a*np.cos(t))/(1+((np.sin(t)**2)))", "(a*np.cos(t)*np.sin(t))/(1+((np.sin(t)**2)))"))
    tim.pendown()

    t = np.arange(0, 2*np.pi, 0.05)

    for i in t:
        tim.goto(calc_function(i, origo, "(a*np.cos(t))/(1+(np.sin(t)**2))", "(a*np.cos(t)*np.sin(t))/(1+(np.sin(t)**2))"))

def plot_hyperbel(origo, a, b):
    tim.color("red")
    tim.penup()
    tim.goto(calc_function(-2.2, origo, "a*np.cosh(t)", "b*np.sinh(t)", a, b))
    tim.pendown()

    t = np.arange(-2.2, 2.2, 0.05)

    for i in t:
        tim.goto(calc_function(i, origo, "a*np.cosh(t)", "b*np.sinh(t)", a, b))

def plot_parable(origo):
    """
    Parameter: En tupel (koordinat), som anger centrum för parabeln
    Returnerar: Inget
    Kommentar: Proceduren ritar parabeln, koordinater beräknas i
    funktionen calc_function
    """
    tim.color("Red")
    tim.penup()
    tim.goto(calc_function(-2, origo, "a*(t**2)", "a*t", a=50))  # Gå till första punkten på ellipsen
    tim.pendown()

    t = np.arange(-2, 2, 0.05)

    for i in t:  # Ritar ellipsen
        tim.goto(calc_function(i, origo, "a*(t**2)", "a*t", a=50))

def plot_ellipse(origo):
    """
    Parameter: En tupel (koordinat), som anger centrum för ellipsen
    Returnerar: Inget
    Kommentar: Proceduren ritar ellipsen, koordinater beräknas i
    funktionen calc_ellips
    """
    tim.color("Red")
    tim.penup()
    tim.goto(calc_function(0, origo,"a*np.cos(t)", "b*np.sin(t)", 100, 50))  # Gå till första punkten på ellipsen
    tim.pendown()

    # Skapar en lista med tal mellan 0 och 2*pi med avståndet 0.025, dvs
    # 0, 0.025, 0.050, ... , 6.275
    t = np.arange(0, 2*np.pi, 0.1)

    for i in t:  # Ritar ellipsen
        tim.goto(calc_function(i, origo, "a*np.cos(t)", "b*np.sin(t)", 100, 50))

def calc_function(t, origo, function_x, function_y, a=100, b=50):
    """
    Paramater: Ett tal, en tupel (koordinat), funktion för x, funktion för y och sedan två godtyckliga tal
    Returnerar: En koordinat
    Kommentar: Returkoordinaterna ligger på de givna funktionerna
    """
    x = eval(function_x)
    y = eval(function_y)

    # Exempel på hur returen fungerar:
    # Om x = 100, y = 200 och origo = (30, -50)
    # så returneras (130, 150)
    return list(map(add, (x, y), origo))

def print_text(text, origo):
    """
    Parametrar: En text och en tupel (koordinat) som anger centrum för texten
    Returnerar: Inget
    Kommentar: Procedur som skriver ut texten i ellipsen
    """
    tim.penup()
    tim.color("white")
    tim.goto(origo[0], origo[1] - FONTSIZE/2)
    tim.write(text, font=("Arial", FONTSIZE, "normal"), align="center")


### Huvudprogram ###
tim = t.Turtle()
tim.hideturtle()
tim.pensize(6)
tim.shape("triangle")
tim.shapesize(0.4)
tim.speed(0)  # 0 - 10, 1 - 10 ökad hastighet, 0 snabbast
screen = t.Screen()
screen.bgcolor("Black")
screen.setup(900, 600)
screen.title("Några parametriska kurvor")

origo = (-300, 150)  # Runt vilken punkt plotten ska vara centererad
plot_ellipse(origo)  # Plottar ellipsen
print_text("Ellips", origo)  # Skriver texten i ellipsen

origo = (-100,150)
plot_parable(origo)
print_text("Parabel", (origo[0]+100, origo[1]))

origo = (100, 150)
plot_hyperbel(origo, 60, 20)
print_text("Hyperbel", (origo[0]+200, origo[1]))

origo = (-300, -100)
plot_lemniskata(origo)
print_text("Lemniskata", (origo[0], origo[1]-100))

origo = (0, -100)
plot_asteroid(origo, 100, 100)
print_text("Asteroid", (origo[0], origo[1]-150))

origo = (250, -100)
plot_descartes(origo)
print_text("Descartes löv", (origo[0], origo[1]-100))


screen.exitonclick()
