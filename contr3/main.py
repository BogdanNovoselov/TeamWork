import tkinter as tk

def text_Check():
    text = text_field.get()
    if text.isdigit():
        label_text.config(text="Все хорошо")
    else:
        label_text.config(text="Уберите буквы")

root = tk.Tk()
root.title("Проверка текста")

text_field = tk.Entry(root, width=30)
text_field.pack(padx=10, pady=10)

label_text = tk.Label(root, text="")
label_text.pack(padx=10, pady=10)

button = tk.Button(root, text="Проверить", command=text_Check)
button.pack(padx=10, pady=10)

root.mainloop()