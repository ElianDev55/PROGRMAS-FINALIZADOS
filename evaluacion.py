import os
def menu ():
    os.system("cls")
    menu = "REGISTRO E INFROMACION DE TOUR DE FRANCIA \n"
    menu += "\n"
    menu += "1)  REGISTRAR A LOS CICLISTAS DEL TOUR DE FRANCIA, ¡SOLO SE PUEDEN REGISTRAR 5! \n"
    menu += "\n"
    menu  += "2)  BUSCAR EL GANADOR DE CADA ETAPA\n"
    menu += "\n"
    menu += "3)  GANADOR DEL TOUR DE FRANCIA\n"
    menu += "\n"
    menu += "4)  LISTA DE GANADORES DE CADA ETAPA\n"
    menu += "\n"
    menu += "5)  GRAFICA DEL TOUR DE FRANCIA\n"
    menu += "\n"
    return menu
os.system("cls")
print("|-------------------------------------------------------------------------------------|\n")
print("|  BIENVENIDO AL PROGRAMA DE REGISTRO E INFROMACION DE TOUR DE FRANCIA                |\n")
print("|  DONDE PODRA VER LAS ESTADISTICAS DEL TOUR Y DE LOS COMPETIDORES                    |\n")
print("|  ESPEREMOS QUE TENGO UNA BUENA EXPERIENCIA CON NUESTRO PROGRAMA                     |\n")
print("|-------------------------------------------------------------------------------------|\n")
lol = input("PRECSIONE LA TECLA ENTER PARA CONTINUAR....")
print("\n")


""""
GANADOR DE CADA ETAPA
"""
def ganador_etapa (lista_madre):
    primera = []
    contador = 0
    contador_segunda= 0
    contador_tercera = 0
    contador_cuarta = 0
    contador_quinta = 0
    for a in lista_madre :
        contador += a[1]
    promedio_1 = contador/5
    for i in lista_madre :
        x = []
        nombre = i[0]
        uno = i[1]
        if uno < promedio_1:
            x.append(nombre)
            x.append(uno)
            primera.append(x)
    if primera [0][1] < primera [1][1]:
        c = primera[0][0]
        b = primera[0][1]
    else:
        c = primera[1][0]
        b = primera[1][1]
    print("\n")
    print("PRIMERA ETAPA LA GANO",c,"CON",b,"SEGUNDOS")
    print("\n")
    segunda = []
    for a_a in lista_madre :
        contador_segunda += a_a[2]
    promedio_segunda = contador_segunda/5
    for i_i in lista_madre :
        z = []
        nombre_dos = i_i[0]
        dos = i_i[2]
        if dos < promedio_segunda:
            z.append(nombre_dos)
            z.append(dos)
            segunda.append(z)
    if segunda [0][1] < segunda [1][1]:
        e = segunda[0][0]
        f = segunda[0][1]
    else:
        e = segunda[1][0]
        f = segunda[1][1]
    print("\n")
    print("SEGUNDA ETAPA LA GANO",e,"CON",f,"SEGUNDOS")
    print("\n")
    tercera = []
    for a_b in lista_madre :
        contador_tercera += a_b[3]
    promedio_tercera = contador_tercera/5
    for i_e in lista_madre :
        y = []
        nombre_tercera = i_e[0]
        tres = i_e[3]
        if tres < promedio_tercera:
            y.append(nombre_tercera)
            y.append(tres)
            tercera.append(y)
    if tercera [0][1] < tercera [1][1]:
        h = tercera[0][0]
        g = tercera[0][1]
    else:
        h = tercera[1][0]
        g =tercera[1][1]
    print("\n")
    print("TERCERA ETAPA LA GANO",h,"CON",g,"SEGUNDOS")
    print("\n")
    cuarta = []
    for a_c in lista_madre :
        contador_cuarta += a_c[4]
    promedio_cuarta = contador_cuarta/5
    for i_o in lista_madre :
        p = []
        nombre_cuarta = i_o[0]
        cuarto = i_o[4]
        if cuarto < promedio_cuarta:
            p.append(nombre_cuarta)
            p.append(cuarto)
            cuarta.append(p)
    if cuarta [0][1] < cuarta [1][1]:
        w = cuarta[0][0]
        u = cuarta[0][1]
    else:
        w = cuarta[1][0]
        u =cuarta[1][1]
    print("\n")
    print("CUARTA ETAPA LA GANO",w,"CON",u,"SEGUNDOS")
    print("\n")
    quinta = []
    for a_d in lista_madre :
        contador_quinta += a_d[5]
    promedio_quinto = contador_quinta/5
    for i_p in lista_madre :
        l = []
        nombre_quinto = i_p[0]
        quinto = i_p[5]
        if quinto < promedio_quinto:
            l.append(nombre_quinto)
            l.append(quinto)
            quinta.append(l)
    if quinta [0][1] < quinta [1][1]:
        k = quinta[0][0]
        ñ = quinta[0][1]
    else:
        k = quinta[1][0]
        ñ =quinta[1][1]
    print("\n")
    print("QUINTA ETAPA LA GANO",k,"CON",ñ,"SEGUNDOS")
    print("\n")

""""
GANADOR DE LA COPETENCIA
"""
def ganador_copetencia (lista_madre):
    solo = []
    total = 0
    for i in lista_madre:
        total += i[6]
    promedio = total / 5
    for a in lista_madre:
        sola = []
        c = a[0]
        b = a[6]
        if b < promedio:
            sola.append(c)
            sola.append(b)
            solo.append(sola)
    if solo [0][1] < solo [1][1]:
        a = solo[0][0]
        b = solo[0][1]
    else:
        a = solo[1][0]
        b = solo[1][1]
    return print("GANADOR DEL TOUR DE FRANCIA",a, b)



"""
BUSCAR EL GANADOR DE CADA ETAPA
"""

def buscador (lista_madre,busca):
    if busca == "1":
            primera = []
            contador = 0
            for a in lista_madre :
                contador += a[1]
            promedio_1 = contador/5
            for i in lista_madre :
                x = []
                nombre = i[0]
                uno = i[1]
                if uno < promedio_1:
                    x.append(nombre)
                    x.append(uno)
                    primera.append(x)
            if primera [0][1] < primera [1][1]:
                c = primera[0][0]
                b = primera[0][1]
            else:
                c = primera[1][0]
                b = primera[1][1]
            return print("PRIMERA ETAPA LA GANO",c,"CON",b,"SEGUNDOS")
    elif busca == "2":
        segunda = []
        contador_segunda= 0
        for a_a in lista_madre :
            contador_segunda += a_a[2]
        promedio_segunda = contador_segunda/5
        for i_i in lista_madre :
            z = []
            nombre_dos = i_i[0]
            dos = i_i[2]
            if dos < promedio_segunda:
                z.append(nombre_dos)
                z.append(dos)
                segunda.append(z)
        if segunda [0][1] < segunda [1][1]:
            e = segunda[0][0]
            f = segunda[0][1]
        else:
            e = segunda[1][0]
            f = segunda[1][1]
        return print("SEGUNDA ETAPA LA GANO",e,"CON",f,"SEGUNDOS")
    elif busca == "3":
        tercera = []
        contador_tercera = 0
        for a_b in lista_madre :
            contador_tercera += a_b[3]
        promedio_tercera = contador_tercera/5
        for i_e in lista_madre :
            y = []
            nombre_tercera = i_e[0]
            tres = i_e[3]
            if tres < promedio_tercera:
                y.append(nombre_tercera)
                y.append(tres)
                tercera.append(y)
        if tercera [0][1] < tercera [1][1]:
            h = tercera[0][0]
            g = tercera[0][1]
        else:
            h = tercera[1][0]
            g =tercera[1][1]
        return print("TERCERA ETAPA LA GANO",h,"CON",g,"SEGUNDOS")
    elif busca == "4":
        cuarta = []
        contador_cuarta = 0
        for a_c in lista_madre :
            contador_cuarta += a_c[4]
        promedio_cuarta = contador_cuarta/5
        for i_o in lista_madre :
            p = []
            nombre_cuarta = i_o[0]
            cuarto = i_o[4]
            if cuarto < promedio_cuarta:
                p.append(nombre_cuarta)
                p.append(cuarto)
                cuarta.append(p)
        if cuarta [0][1] < cuarta [1][1]:
            w = cuarta[0][0]
            u = cuarta[0][1]
        else:
            w = cuarta[1][0]
            u =cuarta[1][1]
        return print("CUARTA ETAPA LA GANO",w,"CON",u,"SEGUNDOS")
    elif busca == "5":
        quinta = []
        contador_quinta = 0
        for a_d in lista_madre :
            contador_quinta += a_d[5]
        promedio_quinto = contador_quinta/5
        for i_p in lista_madre :
            l = []
            nombre_quinto = i_p[0]
            quinto = i_p[5]
            if quinto < promedio_quinto:
                l.append(nombre_quinto)
                l.append(quinto)
                quinta.append(l)
        if quinta [0][1] < quinta [1][1]:
            k = quinta[0][0]
            ñ = quinta[0][1]
        else:
            k = quinta[1][0]
            ñ =quinta[1][1]
        return print("QUINTA ETAPA LA GANO",k,"CON",ñ,"SEGUNDOS")


def grafica (lista_madre):
    for i in lista_madre :
        print(f"|{i[0]}|{i[1]:>20}|{i[2]:>20}|{i[3]:>20}|{i[4]:>20}|{i[5]:>20}|")









lista_madre = []
numeros = 0
while  numeros != 6:
    print(menu())
    numeros = int(input("DIGITE LA OPCION QUE QUIERA ACEDER : "))
    if numeros == 1:
        """
        REGISTRO
        """
        contador = 1
        for i in range (0,5,1):
            os.system("cls")
            lista_hijo = []
            ciclista = input(f"DIGITE EL {contador} CICLISTA : ")
            lista_hijo.append(ciclista)
            etapa_1 = int(input("CUANTOS SEGUNDOS PASO LA ETAPA 1 : "))
            lista_hijo.append(etapa_1)
            etapa_2 = int(input("CUANTOS SEGUNDOS PASO LA ETAPA 2 : "))
            lista_hijo.append(etapa_2)
            etapa_3 = int(input("CUANTOS SEGUNDOS PASO LA ETAPA 3 : "))
            lista_hijo.append(etapa_3)
            etapa_4 = int(input("CUANTOS SEGUNDOS PASO LA ETAPA 4 : "))
            lista_hijo.append(etapa_4)
            etapa_5 = int(input("CUANTOS SEGUNDOS PASO LA ETAPA 5 : "))
            lista_hijo.append(etapa_5)
            suma = etapa_1 + etapa_2 + etapa_3 + etapa_4 + etapa_5 
            lista_hijo.append(suma)
            contador += 1
            lista_madre.append(lista_hijo)
    elif numeros == 2:
        os.system("cls")
        print("\n")
        busca = input("DIGITE EL NUMERO DE ETAPA QUE QUIERE SABER : ")
        print("\n")
        print(buscador(lista_madre,busca))
        print("\n")
        input("PRECSIONE LA TECLA ENTER PARA CONTINUAR....")
        print("\n")
    
    elif numeros == 3:
        os.system("cls")
        print("\n")
        print(ganador_copetencia(lista_madre))
        print("\n")
        input("PRECSIONE LA TECLA ENTER PARA CONTINUAR....")
        print("\n")
    elif numeros == 4:
        os.system("cls")
        print("\n")
        print(ganador_etapa(lista_madre))
        print("\n")
        input("PRECSIONE LA TECLA ENTER PARA CONTINUAR....")
        print("\n")
    elif numeros == 5 :
        os.system("cls")
        titulo_1 = "NOMBRES"
        titulo_2 = "SEGUNDOS"
        print(f"{titulo_1}{titulo_2:>100}")
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print(grafica (lista_madre))
        print("\n")
        input("PRECSIONE LA TECLA ENTER PARA CONTINUAR....")
        print("\n")
    elif  numeros == 6 or numeros > 6:
        os.system("cls")
        print("\n")
        print("NUMERO ERRONEO, VUELVA A MARCAR")
        print("\n")
        input("PRECSIONE LA TECLA ENTER PARA CONTINUAR....")
        print("\n")
        numeros = 0