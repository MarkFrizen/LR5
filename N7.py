import tkinter as tk
# Создание основного окна
window = tk.Tk()
window.title("Окно с меню (File → Exit)")
window.geometry("400x300")
# Создание строки меню
menu = tk.Menu(window)
window.config(menu=menu)
# Создание выпадающего меню "File"
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Exit", command=window.quit)
# Добавление меню "File" в строку меню
menu.add_cascade(label="File", menu=file_menu)
# Запуск главного цикла
window.mainloop()