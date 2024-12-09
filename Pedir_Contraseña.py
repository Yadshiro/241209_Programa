#Escribe un prtograma que pida al usuario su contraseña y la valide.
#El programa debe seguir pidiendo la contraseña hasta que sea correcta.

pswd_real = "python123"
pswd_user = ""

while pswd_user != pswd_real.lower():
    pswd_user = input("Inserte su contraseña:")
    if pswd_user.lower() != pswd_real.lower():
        print("Contraseña Incorrecta")

print("Contraseña correcta")
