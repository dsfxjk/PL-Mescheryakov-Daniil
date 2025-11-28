import tkinter as tk
from tkinter import messagebox, filedialog

# создание главного окна приложения
root = tk.Tk()
root.title("Мещеряков Даниил Евгеньевич")
root.geometry("400x250")

# вкладка 1: калькулятор
frame1 = tk.Frame(root)
frame1.pack(fill='both', expand=True)

tk.Label(frame1, text="Число 1:").grid(row=0, column=0)
num1 = tk.Entry(frame1)
num1.grid(row=0, column=1)

tk.Label(frame1, text="Операция:").grid(row=1, column=0)
op_var = tk.StringVar(value='+')
tk.OptionMenu(frame1, op_var, '+', '-', '*', '/').grid(row=1, column=1)

tk.Label(frame1, text="Число 2:").grid(row=2, column=0)
num2 = tk.Entry(frame1)
num2.grid(row=2, column=1)

def calc():
    try:
        a = float(num1.get())
        b = float(num2.get())
        op = op_var.get()
        if op == '+': r = a + b
        elif op == '-': r = a - b
        elif op == '*': r = a * b
        elif op == '/': r = a / b
        messagebox.showinfo("Результат", str(a) + " " + op + " " + str(b) + " = " + str(r))
    except:
        messagebox.showerror("Ошибка", "Ошибка ввода")

tk.Button(frame1, text="Вычислить", command=calc).grid(row=3, column=0, columnspan=2, pady=10)

# вкладка 2: чекбоксы
frame2 = tk.Frame(root)

v1 = tk.BooleanVar()
v2 = tk.BooleanVar()
v3 = tk.BooleanVar()

tk.Checkbutton(frame2, text="Первый", variable=v1).pack()
tk.Checkbutton(frame2, text="Второй", variable=v2).pack()
tk.Checkbutton(frame2, text="Третий", variable=v3).pack()

def show_choice():
    s = []
    if v1.get(): s.append("Первый")
    if v2.get(): s.append("Второй")
    if v3.get(): s.append("Третий")
    if s: messagebox.showinfo("Выбор", "Вы выбрали: " + ", ".join(s))
    else: messagebox.showwarning("Внимание", "Ничего не выбрано")

tk.Button(frame2, text="Показать выбор", command=show_choice).pack(pady=10)

# вкладка 3: текст
frame3 = tk.Frame(root)
# текстовое поле для ввода и отображения текста
text = tk.Text(frame3, height=8)
text.pack(fill='both', expand=True, padx=5, pady=5)

# загрузка текста из файла
def load_text():
    file = filedialog.askopenfilename()
    if file:
        with open(file, 'r') as f:
            text.delete(1.0, tk.END)
            text.insert(1.0, f.read())

# создание меню "Файл"
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить текст", command=load_text)

# переключение вкладок
def show_frame1():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame1.pack(fill='both', expand=True)

def show_frame2():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame2.pack(fill='both', expand=True)

def show_frame3():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame3.pack(fill='both', expand=True)

# панель с кнопками для переключения вкладок
btn_frame = tk.Frame(root)
btn_frame.pack(fill='x')

# кнопки переключения вкладок
tk.Button(btn_frame, text="Калькулятор", command=show_frame1).pack(side='left')
tk.Button(btn_frame, text="Чекбоксы", command=show_frame2).pack(side='left')
tk.Button(btn_frame, text="Текст", command=show_frame3).pack(side='left')

# открытие 1 вкладки и запуск
show_frame1()
root.mainloop()