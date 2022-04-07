try:
    height = float(input('Digite aqui sua altura(Metros e cm):'))
    weight = float(input('Digite aqui seu peso(Kg):'))
    imc = weight/(height*height)


    if imc < 0:
        print("digite apenas valores positivos")
    elif imc <= 18.5:
        print(f'O seu IMC é de {imc:3.2f}\nClassificação: Baixo Peso.')
    elif imc >= 18.5 or imc <= 24.9:
        print(f'O seu IMC é de {imc:3.2f}\nClassificação: Peso Normal.')
    elif imc >= 25 or imc <= 29.9:
        print(f'O seu IMC é de {imc:3.2f}\nClassificação: Sobrepeso.')
    elif imc >= 30 or imc<= 34.9:
        print(f'O seu IMC é de {imc:3.2f}\nClassificação: Obesidade grau I.')
    elif imc >= 35 or imc <= 39.9:
        print(f'O seu IMC é de {imc:3.2f}\nClassificação: Obesidade grau II.')
    elif imc>=40:
        print(f'O seu IMC é de {imc:3.2f}\nClassificação: Obesidade grau III.')


except (ValueError):
    print("insira apenas numeros.Exemplo:'1.76'")