import tkinter as tk


def read_values():
    generators = entry1.get()
    relations = entry2.get()
    return generators, relations

def calculate(result_text):
    generators, relations = read_values()
    new_generators = ""
    for gen in generators:
        if gen != " ":
            new_generators += gen
    new_generators += "e"
    left = []
    right = []
    new_relations = relations.split(" ")
    for rel in new_relations:
        parts = rel.split("=")
        left.append(parts[0])
        right.append(parts[1])
    table = []
    for i in range(len(new_generators)):
        row = []
        for j in range(len(new_generators)):
            if new_generators[i] == new_generators[j]:
                row.append("e ")
            else:
                found = False
                for k in range(len(left)):
                    if new_generators[i] + new_generators[j] == left[k]:
                        row.append(right[k] + " ")
                        found = True
                        break
                    elif new_generators[j] + new_generators[i] == left[k]:
                        row.append(right[k] + " ")
                        found = True
                        break
                if not found:
                    row.append("e ")
        table.append(row)
    for i in range(len(new_generators)):
        print(table[i])
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "    ")
    for i in range(len(new_generators)):
        result_text.insert(tk.END, new_generators[i] + " ")
    result_text.insert(tk.END, "\n")
    for i in range(len(new_generators)):
        result_text.insert(tk.END, new_generators[i] + "   " + "".join(table[i]) + "\n")
    pass


root = tk.Tk()
root.title("Образующие и соотношения")

# создаем поля ввода
label1 = tk.Label(root, text="Образующие:")
label1.grid(row=1, column=0)
entry1 = tk.Entry(root,width = 100)
entry1.grid(row=1, column=1)

label2 = tk.Label(root, text="Определяющие соотношения:")
label2.grid(row=3, column=0)
entry2 = tk.Entry(root, width = 100)
entry2.grid(row=3, column=1)

result_text = tk.Text(root, height=30, width=100)  # создаем текстовое поле
result_text.grid(row=5, column=0, columnspan=2)


# создаем кнопку для запуска расчетов
button = tk.Button(root, text="Рассчитать", command=lambda: calculate(result_text))
button.grid(row=4, column=0)

root.mainloop()
