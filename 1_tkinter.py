# app-это просто переменная, её можно назвать как угодно:)

import tkinter 
import codecs # Кодировщик(чтобы русский язык сохранялся)
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename, asksaveasfilename # Открыть как, сохранить как
from tkinter.messagebox import showerror # Показ всех ошибок
from tkinter import messagebox # Уведомления приложения

from nastroiki_prilojeniya import * # Импортируем настройки

from class_text_editor import *

# app = tkinter.Tk() # Создаём окно нашего приложения 
app.title(APP_NAME) # Указываем название нашего приложение
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT) # Из-за этого нельзя увеличить иконку

text = tkinter.Text(app, width=WIDTH - 100, height=HEIGHT, wrap = 'word') # Виджет текста + указание к какому окну он принадлежит
scroll = Scrollbar(app, orient = VERTICAL, command = text.yview) # Создали scroll (движение с текстом)
scroll.pack(side = "right", fill = "y") # Разместили наж scroll
text.configure(yscrollcommand = scroll.set) # Связь текста со scroll
text.pack() # Разместили поле с текстом

menuBar = tkinter.Menu(app) # Создаём меню

editor = Text_editor()

app_menu = tkinter.Menu(menuBar) # Выпадающее меню у 'Файл'
app_menu.add_command(label="Новый файл", command = editor.new_file)
app_menu.add_command(label="Открыть", command = editor.open_file)
app_menu.add_command(label="Сохранить", command = editor.save_file)
app_menu.add_command(label="Сохранить как", command = editor.save_as_file)

app_spravka = tkinter.Menu(menuBar)
app_spravka.add_command(label="Приветствие")
app_spravka.add_command(label="Документация")
app_spravka.add_command(label="Заметки о выпуске")

menuBar.add_cascade(label="Файл", menu=app_menu)
menuBar.add_cascade(label="Вид")
menuBar.add_cascade(label="Справка", menu=app_spravka, command = editor.get_info)
menuBar.add_cascade(label="Выход", command=app.quit)

app.config(menu=menuBar)

app.mainloop() # Бесконечный цикл нашего приложения(чтобы появлялась иконка)
