import forca
import adivinhacao

print("**************************************")
print("****** Olá, escolha o seu jogo! ******")
print("**************************************")

print("(1) Forca ou (2) Adivinhação")

jogo = int(input("Qual jogo você quer jogar? "))

if(jogo == 1):
    print("Vamos jogar forca.")
    forca.jogar()
elif(jogo == 2):
    print("Vamos jogar adivinhação.")
    adivinhacao.jogar()
