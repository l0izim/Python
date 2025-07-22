import time

t = input("Digite a quantidade de tempo (em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("entrada invalida!")
    quit()

while t: # 0 --> false | 1, 2, 3... --> true
    minutos , segundos = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutos, segundos)
    time.sleep(1)
    print(timer , end="\r")
    t = t - 1

print("TEMPO ACABOU!!")