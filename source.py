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
        root.title('Calculadora IMC!')
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

    def tab3():

        label1.destroy()
        button_imc.destroy()
        button_calories.destroy()
        root.title('Calculadora Calorias')

        # -- Functions --

        def calculo_caloria_homem():
            a = float(age_button.get())
            b = float(calories_button.get())
            c = float(weight_button.get())
            if 18 <= a < 30:
                caloria_diaria = (15.057 * c) + 679
                if caloria_diaria > b:
                    result = f'Voce ja consumiu {b}\n mas ainda tem que consumir {caloria_diaria - b} calorias'
                else:
                    result = f'Voce ja consumiu {b}\n mas deveria ter consumido {b - caloria_diaria} calorias a menos.'

            elif 30 <= a < 60:
                caloria_diaria = (11.6 * c) + 879
                if caloria_diaria > b:
                    result = f'Voce ja consumiu {b} mas ainda tem que consumir {caloria_diaria - b} calorias'
                else:
                    result = f'Voce ja consumiu {b} mas deveria ter consumido {b - caloria_diaria} calorias a menos.'
            else:
                caloria_diaria = (13.5 * c) + 487
                if caloria_diaria > b:
                    result = f'Voce ja consumiu {b} mas ainda tem que consumir {caloria_diaria - b} calorias'
                else:
                    result = f'Voce ja consumiu {b} mas deveria ter consumido {b - caloria_diaria} calorias a menos.'

            ideal.set(f'{result}')

        # -- main --

        ideal = tk.StringVar()

        age_label = Label(root, text='Idade')
        age_label.grid(row=1, column=0, pady=5, padx=2)
        age_button = Entry(root, text='Idade', borderwidth=5)
        age_button.grid(row=2, column=0, padx=2, pady=5)

        weight_label = Label(root, text="Peso: (ex: 69.2)")
        weight_label.grid(row=3, column=0, padx=2, pady=5)
        weight_button = Entry(root, text="Weight", borderwidth=5)
        weight_button.grid(row=4, column=0, padx=2, pady=5)

        calories_label = Label(root, text='Calorias consumida hoje:')
        calories_label.grid(row=5, columnspan=1, column=0, padx=80, pady=5)
        calories_button = Entry(root, text='Calories', borderwidth=5)
        calories_button.grid(row=6, columnspan=1, column=0, padx=80, pady=5)

        sex_label = Label(root, text="Escolha seu sexo:")
        sex_label.grid(row=7, columnspan=1, column=0, padx=80, pady=5)
        sex_male_button = Button(root, text='Homem', borderwidth=5, command=calculo_caloria_homem)
        sex_male_button.grid(row=8, column=0, pady=5, padx=80, columnspan=1)
        sex_woman_button = Button(root, text='Mulher', borderwidth=5)
        sex_woman_button.grid(row=9, column=0, pady=5, columnspan=1, padx=80)

        result_label = Label(root, text='Resultado:')
        result_label.grid(row=10, column=0, pady=5, padx=80, columnspan=1)
        result_button = Label(root, textvariable=ideal, borderwidth=5)
        result_button.grid(row=11, column=0, pady=5, padx=80)

        def back():
            age_label.destroy()
            weight_label.destroy()
            age_button.destroy()
            weight_button.destroy()
            sex_label.destroy()
            sex_male_button.destroy()
            sex_woman_button.destroy()
            result_label.destroy()
            result_button.destroy()
            calories_button.destroy()
            calories_label.destroy()
            tab1()

        button_back = Button(root, text='Back', command=back, borderwidth=2)
        button_back.grid(row=12, columnspan=1, column=0, padx=80, pady=5)

    label1 = Label(root, text='Sejam Bem Vindos! \n Escolha uma das opções:')
    label1.grid(row=1, columnspan=1, column=0, padx=80, pady=20)

    button_imc = Button(root, text='Calcular IMC', borderwidth=2, command=tab2)
    button_imc.grid(row=2, column=0, pady=10, padx=60, columnspan=1)

    button_calories = Button(root, text='Calcular Calorias', borderwidth=2, command=tab3)
    button_calories.grid(row=3, column=0, columnspan=1, pady=10, padx=60)


tab1()
root.mainloop()
