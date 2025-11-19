import tkinter as tk
from tkinter import ttk
# Создание основного окна
root = tk.Tk()
root.title("Программа со вкладками (Notebook)")
root.geometry("400x300")
# Создание виджета Notebook (вкладки)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True, fill='both')
# Создание фреймов для вкладок
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
# Добавление вкладок
notebook.add(tab1, text="Вкладка 1")
notebook.add(tab2, text="Вкладка 2")
notebook.add(tab3, text="Вкладка 3")
# Добавление содержимого на вкладки
ttk.Label(tab1, text="Содержимое первой вкладки", font=("Helvetica", 16)).pack(pady=20)
ttk.Label(tab2, text="Содержимое второй вкладки", font=("Helvetica", 16)).pack(pady=20)
ttk.Label(tab2, text="Люля у мамы - пирожок", font=("Helvetica", 16)).pack(pady=20)
# Запуск главного цикла
root.mainloop()