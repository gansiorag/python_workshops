import turtle

def sqrt_col():
    pass

wndow = turtle.Screen()# создаем окно
wndow.title("Screen & Button")
wndow.setup(width=500, height=500)# устанавливаем размер окна
wndow.colormode(255) # устанавливаем что цвета назначать бувем RGB
cursor = turtle.Turtle() # создаем курсор для рисования
cursor.speed(20) # скорость рисования

for k in range(10,0,-1):
    for d in range(10,0,-1):
        cursor.setposition(-250+k*40+25, -250+d*40+25) # устанавливаем курсор в соответствующую позицию экрана
        cursor.color(150+d*10,k*20,k*20) # рассчитываем цвет заливки
        cursor.begin_fill() # начало заливки
        cursor.circle(20) # нарисовать круг
        cursor.end_fill() # конец заливки

#cursor.up()# поднять курсор что бы не оставлял след
#cursor.down()



turtle.mainloop()
