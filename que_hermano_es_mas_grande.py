numero_adivinar = 7
numero_usuario = int(input("elegi un numero a adivinar"))
if numero_adivinar == numero_usuario:
    print("adivinaste!")
else:
    intento_2 = int(input("intenta de nuevo"))
    if numero_adivinar == intento_2:
        print("ahora si has adivinado!")
    else:
        print("perdiste")