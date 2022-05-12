# SemanaTec - Herramientas Computacionales

Integrantes del Equipo
- Kevin Alberto Crisostomo A00832188
- Alejandro Melendez Torres
- Jose Edmundo Romo Castillo A01197772


>El codigo a continuacion fue modificado por Jose Romo y Alejandro Melendez

```python
from random import randrange, choice
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
speed = 100
contador = 0
lista_mov_food = [vector(20,0), vector(-20,0), vector(0,20), vector(0,-20)]

colores = ['black', '#6b54d3', '#2fb022', '#cb58d2', 'green', 'blue', 'yellow', '#ea7428', '#32bd26', '#f3618d']
color_snake = choice(colores)
colores.remove(color_snake)
color_food = choice(colores)
colores.remove(color_food)
print(color_snake, color_food, colores)

def faster(): //se creo una funcion con la que se le dara mas velocidad
    global speed
    speed -= 10

def slower(): //se creo una funcion con la que se le dara menos velocidad
    global speed
    speed += 10

def change(x, y):
    ""Change snake direction.""
    aim.x = x
    aim.y = y


def inside(head):
    ""Return True if head inside boundaries.""
    return -200 < head.x < 190 and -200 < head.y < 190
        
def move(): //se modifico el move para poder mover la comida 
    ""Move snake forward one segment.""
    global contador
    contador += 1
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    if ((contador % 4) == 0):
        food_dir = choice(lista_mov_food)
        food.move(food_dir)
        while (food in snake or not(inside(food))):
            food_dir = choice(lista_mov_food)
            food.move(food_dir)            
        
    clear()

    for body in snake:
        square(body.x, body.y, 9, color_snake)

    square(food.x, food.y, 9, color_food)
    update()
    ontimer(move, speed)

writer = Turtle()
tracer(False)


def info_alumnos():
    writer.hideturtle()
    writer.up()
    writer.goto(0,190)
    writer.color('blue')
    writer.write("Kevin ALberto Crisostomo A00832188", align='center',font=('chalkboard',15,'normal'))
    writer.goto(0,170)
    writer.color('pink')
    writer.write("Alejandro Melendez Torres A00832494", align='center',font=('chalkboard',15,'normal'))
    writer.goto(0,150)
    writer.color('green')
    writer.write("José Edmundo Romo Castillo A01197772", align='center',font=('chalkboard',15,'normal'))

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
info_alumnos()
onkey(lambda: faster(),'+') //se le llama a la funcion y se activara con el simbolo +
onkey(lambda: slower(),'-')//se le llama a la funcion y se activara con el simbolo -
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')    
move()
done()

#imagen
![Mi video1 (1)](https://i.giphy.com/media/lwFoLdLvBtvs8Ad0IN/giphy.mp4)

