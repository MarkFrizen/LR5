import tkinter as tk
from tkinter import ttk
# Функция для открытия второго окна
def open_second_window():
    # Создаем новое окно (дочернее)
    second_window = tk.Toplevel(root)
    second_window.title("Второе окно")
    second_window.geometry("300x200")
    # Добавляем элементы во второе окно
    ttk.Label(second_window, text="Это второе окно!", font=("Helvetica", 14)).pack(pady=20)
    ttk.Button(second_window, text="Закрыть", command=second_window.destroy).pack(pady=10)
# Основное окно
root = tk.Tk()
root.title("Основное окно")
root.geometry("300x200")
# Кнопка для открытия второго окна
ttk.Button(root, text="Открыть второе окно", command=open_second_window).pack(pady=50)
# Запуск главного цикла
root.mainloop()