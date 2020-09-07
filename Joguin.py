from random import randint
computador = randint(0, 10)
print("sou seu computador .. acabei de pensar em um numero de 0 a 10 será que você consegue adivinhar qual foi : ")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual o seu palpite ?  : "))
    palpites += 1
    if jogador == computador :
        acertou = True
    else:
        if jogador < computador:
            print("Mais...Tente de novo")
        elif jogador > computador:
             print("Menos... Tente de novo")
print("Acertou com {} Tentativas Parabéns!! ".format(palpites))
