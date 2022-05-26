from tkinter import *
from turtle import width

root = Tk()
list = [('', 'IMC', 'Classificação'),
    (1, 'Abaixo de 18.5', 'Baixo peso'),
    (2, 'Entre 18,6 e 24,9', 'Peso normal'),
    (3, 'Entre 25 e 29.19', 'Sobrepeso'),
    (4, 'Entre 30 e 34.9', 'Obsesidade grau I'),
    (5, 'Entre 35 e 39.9', 'Obesidade grau II'),
    (6, 'Acima de 40', 'Obesidade grau III'),
]
total_rows = len(list)
total_columns = len(list[1])
for i in range(total_rows):
    for j in range(total_columns):
        e = Entry(
                root,
                width=20,
                fg='black',
                font=('Arial', 16, 'bold')
                )
        e.grid(row=i, column=j)
        e.insert(0, list[i][j])
root.mainloop()
