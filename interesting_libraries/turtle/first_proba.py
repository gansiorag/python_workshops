import turtle

def sqrt_col():
    pass

cursor = turtle.Turtle()
cursor.speed(20)

for _ in range(4):
    cursor.forward(50)
    cursor.left(90)# повернуть на лево на 90 градусов
cursor.up()# поднять курсор что бы не оставлял след
cursor.setposition(-250, -200)
cursor.down()
cursor.color('red')
cursor.hideturtle()# делаем сам курсор невидимым

turtle.mainloop()
