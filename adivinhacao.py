import random

def jogar():

    print("**************************************")
    print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número secreto.")
    print("**************************************")

    #isso é um comentário

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual é o nível de dificuldade que deseja?")
    print("(1) Fácil, (2) Médio e (3) Difícil.")

    nivel = int(input("Defina o nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas +1):
        print("Rodada {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute)
        numero_chute = int(chute)

        if(numero_chute < 1 or numero_chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_chute == numero_secreto
        maior   = numero_chute > numero_secreto
        menor   = numero_chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! Seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - numero_chute) # ex: abs e um número absoluto, ex: 40-60 = 20
            pontos = pontos - pontos_perdidos

    print("***********")
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar() #aqui estamos chamando o código de novo porque como ele agora está dentro de uma função, se executarmos esse arquivo sem rodar a função ele não retornará nada.