import tkinter as tk

def imc():
 # --- functions ---

    def generate():
        try:
            a = float(num1.get())
            b = a*a
            result = float(num2.get()) / b

        except Exception as ex:
            print(ex)
            result = 'error'
            num3.set(f'{result:3.2f}')
# --- main ---

    root = tk.Tk()
    root.title('Calculadora de IMC!')

    num1 = tk.StringVar()
    num2 = tk.StringVar()
    num3 = tk.StringVar()

    tk.Label(root, text="Altura: (ex: 1.70)").grid(row=0, column=0,columnspan=1)
    tk.Label(root, text="Peso: (ex: 69.2)").grid(row=2, column=0, columnspan=1)
    tk.Label(root, text="Seu IMC:").grid(row=4, column=0, columnspan=1)

    tk.Entry(root, textvariable=num1, borderwidth=5).grid(row=1, column=0, columnspan=1, padx=80)
    tk.Entry(root, textvariable=num2, borderwidth=5).grid(row=3, column=0, columnspan=1, padx=80)
    tk.Entry(root, textvariable=num3, borderwidth=5).grid(row=5, column=0, columnspan=1, padx=80)

    button = tk.Button(root, text="Calculate", command=generate)
    button.grid(row=8, column=0, columnspan=1, padx=80, pady=20)

    main_button = tk.Button(root, text='Back <-', command=main_page)
    main_button.grid(row=10, columspawn=1, column=0)

    root.mainloop()

def calory():
    ...

def main_page():
    apresentation_text = tk.Label(main, text='Seja Bem Vindo!\n Escolha uma das opções!')
    apresentation_text.grid(row=2, columnspan=1, column=1, padx=80, pady=10)

    imc_button = tk.Button(main, text='IMC', width=15, command=imc, borderwidth=2)
    imc_button.grid(row=3, columnspan=1, column=1, padx=80)

    calory_button = tk.Button(main, text='Caloria',width=15, command=calory, borderwidth=2)
    calory_button.grid(row=5, columnspan=1, column=1, padx=80, pady=10)

    # calory_button = tk.Button(main, borderwidth=5, width=5)
    # calory_button.pack()


main = tk.Tk()
main.title('Main Page.')
main_page()

main.mainloop()








# def imc():
# # --- functions ---
#     def generate():
#         try:
#             a = float(num1.get())
#             b = a*a
#             result = float(num2.get()) / b
#
#         except Exception as ex:
#             print(ex)
#             result = 'error'
#             num3.set(f'{result:3.2f}')
# # --- main ---
#
#     root = tk.Tk()
#     root.title('Calculadora de IMC!')
#
#     num1 = tk.StringVar()
#     num2 = tk.StringVar()
#     num3 = tk.StringVar()
#
#     tk.Label(root, text="Altura: (ex: 1.70)").grid(row=0, column=0,columnspan=1)
#     tk.Label(root, text="Peso: (ex: 69.2)").grid(row=2, column=0, columnspan=1)
#     tk.Label(root, text="Seu IMC:").grid(row=4, column=0, columnspan=1)
#
#     tk.Entry(root, textvariable=num1, borderwidth=5).grid(row=1, column=0, columnspan=1, padx=80)
#     tk.Entry(root, textvariable=num2, borderwidth=5).grid(row=3, column=0, columnspan=1, padx=80)
#     tk.Entry(root, textvariable=num3, borderwidth=5).grid(row=5, column=0, columnspan=1, padx=80)
#
#     button = tk.Button(root, text="Calculate", command=generate)
#     button.grid(row=8, column=0,columnspan=1, padx=80, pady=20)
#
#     root.mainloop()

