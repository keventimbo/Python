from random import randint
print('Bem vindo')
sort = randint(1, 1000)
chute = 0
while chute != sort:
    chute = int(input('Chute :  '))
    if chute == sort:
        print("Você Venceu")
    else:
        if chute > sort:
            print("Alto >>> ",sort)
        else:
            print("Baixo >>> ",sort)
    print("Fim do jogo!")
sort()
