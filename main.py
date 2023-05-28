from tkinter import *

def ButtonClick(item):  #Функция обработки нажатия на кнопку
    global StringWithExpression #Строка с выражением
    try:
        InputField['state'] = "normal" #Разрешаем ввод
        StringWithExpression += item #Добавляем к строке значение кнопки
        InputField.insert(END, item) #Добавляем к полю ввода значение кнопки

        if item == '=': #если значение кнопки равно "="
            result = str(eval(StringWithExpression[:-1])) #С помощью метода EVAL обрабатываем выражение
            InputField.insert(END, result) #Добавляем в поле ввода результат
            StringWithExpression = "" #Обнуляем строку
        InputField['state'] = "readonly" #Запрещаем ввод

    except ZeroDivisionError: #Проверка деления на ноль
        InputField.delete(0, END) #Очищаем поле ввода
        InputField.insert(0, 'Ошибка (деление на 0)') #Добавляем в поле ввода текст ошибки
    except SyntaxError:  #Проверка на синтаксическую ошибку
        InputField.delete(0, END) #Очищаем поле ввода
        InputField.insert(0, 'Ошибка')  #Добавляем в поле ввода текст ошибки


def ButtonClear(): #Функция очистки поля ввода по кнопке очистить
    global StringWithExpression  #Строка с выражением
    StringWithExpression = "" #Обнуляем строку
    InputField['state'] = "normal" #Разрешаем ввод
    InputField.delete(0, END) #Обнуляем поле ввода
    InputField['state'] = "readonly" #Запрещаем ввод


Box = Tk()  #Создадим объект класса Tk()
Box.geometry("268x288")  #Укажем разрешение окна 268×288
Box.title("Калькулятор") #Заголовок “Калькулятор”
Box.resizable(0, 0)  #Запретим возможность изменять разрешение окна

FrameOfTheInputField = Frame(Box) #Создадим виджет Frame(). Фрейм - вспомогательный виджет, область позиционирования элементов
FrameOfTheInputField.grid(row=0, column=0, columnspan=4, sticky="nsew")  #Отобразим его методом grid()

InputField = Entry(FrameOfTheInputField, font='Arial 15 bold', width=24, state="readonly")  #Создадим поле ввода Entry. Разместим в поле frame_input, запретим ввод текста.
InputField.pack(fill=BOTH) #fill: определяет, будет ли виджет растягиваться, чтобы заполнить свободное пространство вокруг. BOTH - элемент растягивается по вертикали и горизонтали.

ButtonC = Button(Box, text='C', command=lambda: ButtonClear()) #Кнопка для очистки текстового поля. lambda создает временную функцию, которая будет вызываться при нажатии кнопки Button.
ButtonC.grid(row=1, column=3, sticky="nsew")  #Размещаем кнопку

ButtonsText = (('7', '8', '9', '/'),  #Создадим кортеж с кнопками
               ('4', '5', '6', '*'),
               ('1', '2', '3', '-'),
               ('0', '.', '=', '+'))

StringWithExpression = ""  #Пустая переменная строкового. Также добавим кнопку, которая в последующем будет служить для очищения текстового поля:

for Row in range(4):   #Создаем 16 кнопок. sticky - выравнивание элемента в ячейке, если ячейка больше элемента. padx и pady: отступы по горизонтали и вертикали соответственно от границ ячейки грида до границ элемента.
    for Column in range(4):
        Button(Box, width=2, height=3, text=ButtonsText[Row][Column], command=lambda row=Row, col=Column: ButtonClick(ButtonsText[row][col])).grid(row=Row + 2, column=Column, sticky="nsew", padx=1, pady=1)

Box.mainloop()  #Главный цикл программы