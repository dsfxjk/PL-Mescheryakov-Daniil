import tkinter as tk
from tkinter import messagebox
import requests
import json


def get_info(event=None):
    repo = entry.get()
    if not repo:
        return

    try:
        # получаем данные репозитория
        repo_url = "https://api.github.com/repos/" + repo
        repo_data = requests.get(repo_url).json()

        # получаем данные владельца
        owner_data = requests.get(repo_data['owner']['url']).json()

        # формируем результат
        result = {
            'company': owner_data.get('company'),
            'created_at': repo_data.get('created_at'),
            'email': owner_data.get('email'),
            'id': repo_data.get('id'),
            'name': repo_data.get('name'),
            'url': owner_data.get('url')
        }

        # сохраняем в файл
        filename = repo.replace('/', '_') + "_info.json"
        with open(filename, 'w') as f:
            json.dump(result, f, indent=2)

        # показываем сообщение
        tk.messagebox.showinfo("Успех", "Данные сохранены в " + filename)

    except:
        tk.messagebox.showerror("Ошибка", "Репозиторий не найден")


# создаем окно
root = tk.Tk()
root.title("GitHub Info")
root.geometry("400x150")

# поле ввода
tk.Label(root, text="Введите репозиторий (user/repo):").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# кнопка
tk.Button(root, text="Получить данные", command=get_info).pack(pady=10)

root.mainloop()