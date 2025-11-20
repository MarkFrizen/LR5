import tkinter as tk
# Создание основного окна
root = tk.Tk()
root.title("Окно с кнопкой «Привет»")
root.geometry("300x200")
# Функция, которая вызывается при нажатии кнопки
def say_hello():
    label.config(text="Привет!")
# Кнопка
button = tk.Button(root, text="Нажми меня", command=say_hello)
button.pack(pady=20)
# Метка для отображения текста
label = tk.Label(root, text="", font=("Helvetica", 14))
label.pack(pady=10)
# Запуск главного цикла
root.mainloop()