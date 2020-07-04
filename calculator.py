def calculate():
    operation = input('''
    Digite a operação matematica a ser realizada:
    + para Adição
    - para Subtração
    * para Multiplicação
    / para Divisão
    ** para Potenciação
        ''')
    number_1 = int(input('Por favor digite o primeiro numero: '))
    number_2 = int(input('Por favor digite o segundo numero: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    elif operation == '**':
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1**number_2)
    else:
        print("Você Não Digitou um operador valido por favor reinicie o programa")

    #Adiciona Again() a função calculate()
    again()
def again():
    calc_again = input('''
        Deseja Calcular Novamente?
        Por Favor Pressione S Para SIM ou N para NÃO. 
    ''')
    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print("Até Depois")
    else:
        again()
calculate()
