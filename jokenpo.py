import random
import time

opcoes = ['pedra' , 'papel', 'tesoura']

def contagem():
    print("JO...")
    time.sleep(1)
    print("KEN...")
    time.sleep(1)
    print("Pô!")
    time.sleep(1)

    
def resultado (jogador, computador):
    if jogador == computador :
        return"empate!"
    elif(
        (jogador == 'pedra' and computador == 'tesoura') or
        (jogador == 'tesoura'    and computador == 'papel') or
        (jogador == 'pepel' and computador == 'pedra')
    ):
        return "Você venceu!!"
    else:
        return "Você perdeu!"
    
    
def jogar():
    print("Bem-vindo ao JOKENPÔ!")
    print("Escolha entre pedra, papel e tesoura")
    
    jogador = input("sua jogada: ").strip().lower()
    
    if jogador not in opcoes:
        print ("jogada invalida.")
        return
    
    computador = random.choice(opcoes)
    
    contagem()
    
    print(f"\nVocê jogou: {jogador}")
    print(f"Computador jogou: {computador}")
    print(f"\nResultado: {resultado (jogador, computador)}")
    
#exutador
jogar()
    