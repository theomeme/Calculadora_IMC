from tkinter import *
import tkinter as tk

root = Tk()
root.minsize(height=250, width=250)
root.title('Super Calculadora!')


def tab1():
    def tab2():
        label1.destroy()
        button_imc.destroy()
        button_calories.destroy()

        # --- function ---
        def generate():
            try:
                a = float(height1.get())
                b = a * a
                result = float(weight1.get()) / b
            except Exception as ex:
                print(ex)
                result = 'error'
            imc1.set(f'{result:3.2f}')

        # --- main ---

        height1 = tk.StringVar()
        weight1 = tk.StringVar()
        imc1 = tk.StringVar()

        height = Label(root, text="Altura: (ex: 1.70)")
        height.grid(row=0, column=0, columnspan=1)
        weight = Label(root, text="Peso: (ex: 69.2)")
        weight.grid(row=2, column=0, columnspan=1)
        label_imc = Label(root, text="Seu IMC:")
        label_imc.grid(row=4, column=0, columnspan=1)

        height_variable = Entry(root, textvariable=height1, borderwidth=5)
        height_variable.grid(row=1, column=0, columnspan=1, padx=80)
        weight_variable = Entry(root, textvariable=weight1, borderwidth=5)
        weight_variable.grid(row=3, column=0, columnspan=1, padx=80)
        imc_variable = Entry(root, textvariable=imc1, borderwidth=5)
        imc_variable.grid(row=5, column=0, columnspan=1, padx=80)

        button_calculate = tk.Button(root, text="Calculate", command=generate, borderwidth=2)
        button_calculate.grid(row=8, column=0, columnspan=1, padx=80, pady=5)

        def back():
            height.destroy()
            weight.destroy()
            label_imc.destroy()
            height_variable.destroy()
            weight_variable.destroy()
            imc_variable.destroy()
            button_calculate.destroy()
            button_back.destroy()

            tab1()

        button_back = Button(root, text='Back', command=back, borderwidth=2)
        button_back.grid(row=9, columnspan=1, column=0, padx=80, pady=5)

    label1 = Label(root, text='Sejam Bem Vindos! \n Escolha uma das opções:')
    label1.grid(row=1, columnspan=1, column=0, padx=80, pady=20)

    button_imc = Button(root, text='Calcular IMC', borderwidth=2, command=tab2)
    button_imc.grid(row=2, column=0, pady=10, padx=60, columnspan=1)

    button_calories = Button(root, text='Calcular Calorias',borderwidth=2)
    button_calories.grid(row=3, column=0, columnspan=1, pady=10, padx=60)


tab1()
root.mainloop()
