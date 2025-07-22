import random
import string

def gerador_senha(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punts_options = string.punctuation
    
    options = ascii_options + number_options + punts_options
    
    password_user = ""
    
    for i in range(0, len_pass):
        digit = random.choice(options)
        password_user = password_user + digit
        
    return password_user

choice_user = input("Quantos digitos na senha?\n")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada invalida!!")
    quit()
    
response = gerador_senha(len_pass = choice_user)
print(f"Senha gerada: {response}")
