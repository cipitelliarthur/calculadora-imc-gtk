#Ainda falta acrescentar a diferença entre idade e sexo

while True:
    print('''[ 1 ] Calcular IMC\n[ 2 ] Sair''')
    option = int(input('Opção: '))

    if option == 2:
        break
    else:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        idade = int(input('Idade: '))
        altura = float(input('Altura (m): '))
        peso = float(input('Peso (Kg):'))
        imc = peso / (altura ** 2)

        print('==' * 30)

        print(f'Seu IMC foi de {imc:.2f} Kg/m²')

        if sexo == 'M': #Essa ainda não é a verdadeira tabela masculina
            if imc < 16.9:
                print('Muito abaixo do peso')
            elif imc < 18.49:
                print('Abaixo do peso')
            elif imc < 24.99:
                print('Peso normal')
            elif imc < 29.99:
                print('Acima do peso')
            elif imc < 34.99:
                print('Obesidade Grau I')
            elif imc < 39.99:
                print('Obesidade Severa Grau II ')
            elif imc > 40.00:
                print('Obesidade Mórbida Grau III ')
        if sexo == 'F': #Essa ainda não é a verdadeira tabela feminina
            if imc < 16.9:
                print('Muito abaixo do peso')
            elif imc < 18.49:
                print('Abaixo do peso')
            elif imc < 24.99:
                print('Peso normal')
            elif imc < 29.99:
                print('Acima do peso')
            elif imc < 34.99:
                print('Obesidade Grau I')
            elif imc < 39.99:
                print('Obesidade Severa Grau II ')
            elif imc > 40.00:
                print('Obesidade Mórbida Grau III ')
    print('==' * 30)
