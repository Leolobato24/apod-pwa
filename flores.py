import turtle
import random
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

# Ocultar cursor
t.hideturtle()

# Función para dibujar un pétalo
def petalo():
    t.circle(60, 60)
    t.left(120)
    t.circle(60, 60)
    t.left(120)

# Animación de flores infinitas
h = 0  # Hue inicial

while True:
    t.penup()
    # Elegir posición aleatoria
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    t.goto(x, y)
    t.pendown()

    # Elegir color con rueda HSV
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)

    t.begin_fill()
    # Dibujar flor con varios pétalos
    for _ in range(6):
        petalo()
        t.right(60)
    t.end_fill()

    # Cambiar matiz para siguiente flor
    h += 0.02
    if h > 1:
        h = 0
