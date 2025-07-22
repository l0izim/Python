import time

user = input("Quer começar o Quiz? (S/N): ")

erro = 0
acertos = 0

if user != "S":
    quit()

print("Começando...")
time.sleep(1)

print("Qual empresa é responsavel pelo jogo GTA? \n (A) Rockstar Games \n (B) Ubisoft \n (C) EA \n")
resposta_1 = input("Resposta: ")

if resposta_1 == "A":
    time.sleep(1)
    print("Correto!!")
    acertos = acertos + 1
else:
    time.sleep(1)
    print("Incorreto!")
    erro = erro + 1 

time.sleep(1)
print("Qual empresa é responsavel pelo jogo R6? \n (A) Rockstar Games \n (B) Ubisoft \n (C) EA \n")
resposta_2 = input("Resposta: ")

if resposta_2 == "B":
    time.sleep(1)
    print("Correto!!")
    acertos = acertos + 1
else:
    time.sleep(1)
    print("Incorreto!")
    erro = erro + 1 

time.sleep(1)
print("Qual empresa é responsavel pelo jogo FIFA? \n (A) Rockstar Games \n (B) Ubisoft \n (C) EA \n")
resposta_3 = input("Resposta: ")

if resposta_3 == "C":
    time.sleep(1)
    print("Correto!!")
    acertos = acertos + 1
else:
    time.sleep(1)
    print("Incorreto!")
    erro = erro + 1 
    
print(f"Acabou o Quiz! \n Acertos: {acertos} \n Erros: {erro}")