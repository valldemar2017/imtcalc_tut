# импорт необходимых библиотек
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# создание и настройка окна
window = Tk()
window.title("Калькулятор индекса массы тела (ИМТ)")
window.geometry('400x300')

# Инициализация компонентов визуального оформления
frame = Frame(      #основной контейнер
    window,
    padx = 10,
    pady = 10
)
frame.pack(expand=True)
# надписи
height_lb = Label(  
    frame,
    text = "Введите свой рост (в см)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Введите свой вес (в кг)  "
)
weight_lb.grid(row=4, column=1)
# конец блока надписей

# поля ввода роста и веса
height_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
height_tf.grid(row=3, column=2)

weight_tf = Entry(
   frame,
)
weight_tf.grid(row=4, column=2, pady=5)
# конец блока полей ввода

# функция подсчета индекса массы тела
def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m**2)
    bmi = round(bmi, 1)
    if bmi < 18.5:
        messagebox.showinfo("bmi-pythonguides", f'ИМТ = {bmi} соответствует недостаточному весу')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')

# кнопка для расчета ИМТ
cal_btn = Button(
   frame, #Заготовка с настроенными отступами.
   text = 'Рассчитать ИМТ', #Надпись на кнопке.
   command = calculate_bmi
)
cal_btn.grid(row=5, column=2) #Размещаем кнопку в ячейке, расположенной ниже, чем наши надписи, но во втором столбце, то есть под ячейками для ввода информации.

# Запуск цикла окна
window.mainloop()