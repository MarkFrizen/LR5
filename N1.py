import tkinter as tk
# Создание основного окна
window = tk.Tk()
window.title("Окно с кнопкой «Привет»")
window.geometry("500x250")
# Кнопка
button = tk.Button(window, text="Привет")
button.pack(pady=10)
# Запуск главного цикла
window.mainloop()