numero_adivinar = 2
user_number = int(input("elegi un numero a adivinar"))
if numero_adivinar == user_number:
    print("adivinaste!")
else:
    intento_2 = int(input("tienes otra oportunidad!"))
    if intento_2 == numero_adivinar:
        print("adivinaste")
    else:
        intento_3 = int(input("te quedan tres oportunidades"))
        if intento_3 == numero_adivinar:
            print("adivinaste!")
        else:
            intento_4 = int(input("te quedan dos oportunidades"))
            if intento_4 == numero_adivinar:
                print("adivinaste!")
            else:
                intento_5 = int(input("te queda una oportunidad!!"))
                if intento_5 == numero_adivinar:
                    print("adivinaste")
                else:
                    print("no te quedan oportunidades :c has perdido")





