idade = int(input('Digite sua idade:'))
peso = int(input('Digite seu peso(Kg):'))
if 18 <= idade < 30:
    sexo = int(input('HOMEM[1]\nMULHER[2]\nDigite seu sexo:'))
    if sexo == 1:
        caloria_diaria = (15.057 * peso) + 679
    else:
        caloria_diaria = (14.7 * peso) + 486.6


elif 30 <= idade < 60:
    sexo = int(input('HOMEM[1]\nMULHER[2]\nDigite seu sexo:'))
    if sexo == 1:
        caloria_diaria = (11.6 * peso) + 879
    else:
        caloria_diaria = (8.7 * peso) + 829

elif idade > 60:
    sexo = int(input('HOMEM[1]\nMULHER[2]\nDigite seu sexo:'))
    if sexo == 1:
        caloria_diaria = (13.5 * peso) + 487
    else:
        caloria_diaria = (10.5 * peso) + 596

caloria_consumida = float(input('Digita quantas calorias voce ja consumiu hoje:'))
print(caloria_diaria)
if caloria_diaria > caloria_consumida:
    print(f'Voce ja consumiu {caloria_consumida} mas ainda tem que consumir {caloria_diaria - caloria_consumida} calorias')
else:
    print(f'Voce ja consumiu {caloria_consumida} mas deveria ter consumido {caloria_consumida - caloria_diaria} calorias a menos.')