apetece_helado_input = input("te apetece un helado? (si / no )").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("lo que has puesto no coincide con ninguna de las opciones por lo tanto se tomara como un no")
    apetece_helado = False


dinero_helado_input = input("tenes dinero para un helado? (si / no )").upper()


esta_tia_input = input("estas con tu tia? (si / no )").upper()

senior_helados_input = input("esta el se;or de los helados (si / no ?").upper()

if senior_helados_input == "SI":
    senior_helados = True
elif senior_helados_input == "NO":
    senior_helados = False
else:
    print("lo que pusiste no coincide con ninguna de las opciones por lo tanto se tomara como un no")
    senior_helados = False

podes_permitirtelo = dinero_helado_input == "SI" or esta_tia_input == "SI"

if apetece_helado and podes_permitirtelo and senior_helados:
    print("comprate un helado")
else:
    print("bue pobre de mierda no te comas nada")