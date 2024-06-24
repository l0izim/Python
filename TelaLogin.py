#Imports
import customtkinter

#Criando janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.title("Login")
janela.geometry("500x300")

def Clique():
    print("Login feito!!")

texto = customtkinter.CTkLabel(janela,text="Fazer Login")

email = customtkinter.CTkEntry(janela,placeholder_text="E-mail")

senha = customtkinter.CTkEntry(janela, placeholder_text="Senha",show="*")

botao = customtkinter.CTkButton(janela, text="Login", command=Clique)

texto.pack(padx=10,pady=10)
email.pack(padx=10,pady=10)
senha.pack(padx=10,pady=10)
botao.pack(padx=10,pady=10)

janela.mainloop()