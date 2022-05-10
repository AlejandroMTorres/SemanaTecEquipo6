from math import*

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle2(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x,start.y)
    down()
    begin_fill()
    d= math.sqrt(((end.x - start.x)**2)+((end.y - start.y)**2))
    circle(d/2)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


def info_alumnos():
    up()
    goto(14,190)
    color('blue')
    write("Kevin ALberto Crisostomo A00832188", align='right',font=('Arial',10,'normal'))
    goto(18,170)
    color('pink')
    write("Alejandro Melendez Torres A00832494", align='right',font=('Arial',10,'normal'))
    goto(35,150)
    color('green')
    write("José Edmundo Romo Castillo A01197772", align='right',font=('Arial',10,'normal'))
    



state = {'start': None, 'shape': line }
setup(420, 420, 500, 0)
info_alumnos() 
#Programacion basada en eventos 
#funcion que atinde los eventos del mosuse


onscreenclick(tap)
listen()


#funcion que atiene los eventos del teclado
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
#siempre debe ser la ultima instrucción- glutmainloop()- 
done()
