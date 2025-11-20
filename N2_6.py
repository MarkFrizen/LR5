import tkinter as tk
from tkinter import ttk
# Функция для конвертации валют
def convert_currency():
    try:
        amount = float(amount_entry.get())
        rate = float(rate_entry.get())
        result = amount * rate
        result_label.config(text=f"Результат: {result:.2f}")
    except ValueError:
        result_label.config(text="Ошибка: введите число")
# Создание основного окна
root = tk.Tk()
root.title("Конвертер валют")
root.geometry("300x200")
# Поля ввода
ttk.Label(root, text="Сумма:").pack(pady=5)
amount_entry = ttk.Entry(root)
amount_entry.pack(pady=5)
ttk.Label(root, text="Курс:").pack(pady=5)
rate_entry = ttk.Entry(root)
rate_entry.pack(pady=5)
# Кнопка конвертации
convert_button = ttk.Button(root, text="Конвертировать", command=convert_currency)
convert_button.pack(pady=10)
# Метка для результата
result_label = ttk.Label(root, text="Результат: ")
result_label.pack(pady=10)
# Запуск главного цикла
root.mainloop()