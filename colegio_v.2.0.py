import os
def configuraion_usurio ():
    os.system("cls")
    print("---------------------------------BIENVENIDO AL SISTEMA DE NOTAS ESTUDIANTIL DEL SENA---------------------------------")
    print("")
    print("PARA EMPEZAR EL PROGRAMA DEBERA CONFIGURARLO, SOLO SON 3 COSAS, ESTA CONFIGURAION SE HACE PARA QUE EL\nUSUARIO TENGA UN EXPERIENCIA AGRADABLE ")
    print("")
    notas_incio=int(input("DE QUE NUMERO EMPIEZAN LAS NOTAS: EJEMPLO 0 AL 10 = 0 :--------------->   ")) 
    print("")
    notas_final = int(input("HASTA QUE NUMERO TERMINAN LAS NOTAS EJEMPLO 0 AL 10 = 10 :---------------> "))
    print("")
    pasar=float(input("CON QUE NOTA SE PASA EL AÑO: --------------------> "))
    print("")
#print(configuraion_usurio())
def menu():
    os.system("cls")
    print("--------------------------------------SOFTWARE ESTUDIANTIL DEL SENA , SEDE INDUSTRIA Y CONSTUCCION------------------------------------------")
    print("")
    m ="1) Añadir estudiante y calificación \n"
    m += "2) 1Mostrar lista de estudiantes con sus calificaciones \n"
    m += "3) Calcular la promedio de las calificaciones \n"
    m += "4) Calcular el número de aprobados \n"
    m += "5) Mostrar los estudiantes con mejor calificación \n"
    m += "6) Mostrar los estudiantes con calificación superior al promedio  \n"
    m += "7) Consultar la nota de un estudiante determinado  \n"
    m += "8) FINALIZAR EJECUCION DEL PROGRAMA \n"
    return m
#---------------------------------------------------------------------------------------------------------------
def lista(lista_estudiantes) -> list:
    os.system("cls")
    nombre = "ESTUDIANTE "
    nota_1 = "PERIODO N°1 "
    nota_2 = "PERIODO N°2 "
    nota_3 = "PERIODO N°3 "
    nota_4 = "PERIODO N°4 "
    promedio = "NOTA FINAL"
    titulo = "LISTA DE ESTUDIANTES REGUISTRADOS"
    print("___________________________________________________________________________________________________________________________________________________________")
    print(f"{titulo:>90}")
    print("")
    print("___________________________________________________________________________________________________________________________________________________________")
    print(f"{nombre:>25} {nota_1:>20} {nota_2:>20} {nota_3:>20} {nota_4:>20} {promedio:>20}")
    for i in lista_estudiantes:
        a = i[0]
        b = i[1]
        c = i[2]
        d = i[3]
        e = i[4]
        f = i[5]
        print("________________________________________________________________________________________________________________________________________________________")
        print(f"{a:>20} {b:>20} {c:>20} {d:>20} {e:>20} {f:>20}")
    print('\n')
    input("Presione ENTER para continuar...")
#print(lista(lista_estudiantes()))
#---------------------------------------------------------------------------------------------------------------
def promedio_estudiante(lista_estudiantes):
    os.system("cls")
    entrada =input("DIGITE EN NOMBRE DEL ESTUDAINTE QUE QUIERE SABER SU PROMEDIO ------------------------>  ")
    nombre = "ESTUDIANTE "
    nota_1 = "PERIODO N°1 "
    nota_2 = "PERI0DO N°2 "
    nota_3 = "PERI0DO N°3 "
    nota_4 = "PERI0DO N°4 "
    promedio = "NOTA FINAL"
    titulo = "LISTA DE ESTUDIANTES REGUISTRADOS"
    print("_________________________________________________________________________________________________________________________________________")
    print(f"{titulo:>90}")
    print("___________________________________________________________________________________________________________________________________________________________")
    print(f"{nombre:>25} {nota_1:>20} {nota_2:>20} {nota_3:>20} {nota_4:>20}  {promedio:>20}")
    print("                                  ")
    contador = 0
    for i in lista_estudiantes:
        for e in i:
            if e == entrada:
                contador += 1
                n = i[0]
                a = i[1]
                b = i[2]
                c = i[3]
                d = i[4]
                f = i[5]
                print("________________________________________________________________________________________________________________________________________________________")
                print(f"{n:>20} {a:>20} {b:>20} {c:>20} {d:>20} {f:>20}")
    if contador == 0:
        print("-------------------------------------------------------------NO EXISTE ESE ESTUDIANTE----------------------------------------------------------------------------------")
    input("Presione ENTER para continuar...")
def promedio_estudiantes(lista_promedio):
    os.system("cls")
    print("------------------------------------------PROMEDIO DE LOS ESTUDIANTES----------------------------")
    print("")
    b = len(lista_promedio)
    a = 0
    for i in lista_promedio:
        a += i[5]
        d = a/b
    return d 

#print(promedio_estudiantes(lista_estudiantes()))  
def aprobados(lista_promedio,pasar):
    os.system("cls")
    contador = 0
    nombre = "NOMBRE"
    nota = "NOTA"
    print("------------------------------------------LISTA DE ESTUDIANTES APORBADOS----------------------------")
    print("")
    c = []
    for i in lista_promedio:
        a = i[5]
        b = i[0]
        while a >= pasar :
            contador += 1
            solo = []
            solo.append(b)
            solo.append(a)
            c.append(solo)
            break
    print("NUMEROS DE APROBADOS: ",contador)
    print("               ")
    print(f"{nombre:>50} {nota:>50}")
    for j in c:
        f = j[0]
        g = j[1]
        print(f"{f:>50} {g:>50}")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    input("Presione ENTER para continuar...")
#print (aprobados(lista_estudiantes()))
def mejores(lista_estudiantes,mejor):
    os.system("cls")
    contador = 0
    print("------------------------------------------MEJORES ESTUDIANTES CON BUEN PROMEDIO----------------------------")
    print("")
    for i in lista_estudiantes:
        if i[5] >= mejor:
            print("LOS MEJORES ESTUDIANTES CON LA MEJOR NOTA FINAL :          ""NOMBRE :     ",i[0],"         ""NOTA:     ",i[5])
            while i[5] >= mejor:
                contador += 1
                break
    if contador == 0:
        print("NO HAY ESTUDIANTES CON  MEJOR NOTA DEL GRUPO")
    print("")
    input("Presione ENTER para continuar...")
#print(mejores(lista_estudiantes())) 
def mayor_media(promedio_estudiantes,lista_estudiantes):
    os.system("cls")
    print("------------------------------------------ESTUDIANTES QUE SUPERARON EL PROMEDIO DEL GRUPO----------------------------")
    print("")
    for i in lista_estudiantes:
        a = i[5]
        if a > promedio_estudiantes:
            print("ESTUDIANTES CON NOTA MAYOR AL PROMEDIO DEL GRUPO:          ""NOMBRE :     ",i[0],"         ""NOTA:     ",i[5])
    print("")
    input("Presione ENTER para continuar...")
#print(mayor_media(promedio_estudiantes(lista_estudiantes()),lista_estudiantes()))
#---------------------------------------------------------------------------------------------------------------
entrada = 0
estudiantes=[]
os.system("cls")
print("---------------------------------BIENVENIDO AL SISTEMA DE NOTAS ESTUDIANTIL DEL SENA---------------------------------")
print("")
print("PARA EMPEZAR EL PROGRAMA DEBERA CONFIGURARLO, SOLO SON 3 COSAS, ESTA CONFIGURAION SE HACE PARA QUE EL\nUSUARIO TENGA UN EXPERIENCIA AGRADABLE ")
print("")
notas_incio=float(input("DE QUE NUMERO EMPIEZAN LAS NOTAS: EJEMPLO 0 AL 10 = 0 :--------------->   ")) 
print("")
notas_final = float(input("HASTA QUE NUMERO TERMINAN LAS NOTAS EJEMPLO 0 AL 10 = 10 :---------------> "))
print("")
pasar=float(input("CON QUE NOTA SE PASA EL AÑO: --------------------> "))
print("")
mejor =float(input("CON QUE NOTA SE CONSIDERA COMO MEJOR NOTA: --------------------> "))
print("")
while entrada != 8 :
        opcion = "si"
        print("                                  ")
        print(f"{menu():>100}")
        print("                                  ")
        entrada = int(input("MARQUE LA OPCIÓN QUE QUIERE EJECUTAR    "))
        print("                                  ")
        print("                                  ")
        if entrada == 1:
            nombres = []
            os.system("cls")
            while opcion == "si":
                os.system("cls")
                estudiante = []
                nombre = input("INGRESE EL NOMBRE DEL ESTUDIANTES ------------------------------------------->  ")
                for i in nombres:
                    while i == nombre:
                        os.system("cls")
                        print("NOMBRE DEL ESTUDIANTE YA ESTA REGUISTRADO")
                        nombre = input("INGRESE EL NOMBRE DEL ESTUDIANTES ------------------------------------------->  ")
                nombres.append(nombre)
                estudiante.append(nombre)
                nota_1 = float(input("INGESE LA NOTA DEL ESTUDAINTE EN EL PERIDO N°1 ------------------------>  "))
                while notas_incio > nota_1 or notas_final < nota_1:
                    os.system("cls")
                    print("VALOR NO CONINCIDE CON LA CONFIGURACION INICIAL,DIGITE OTRA VEZ EL VALOR ")
                    print()
                    nota_1 = float(input("INGESE LA NOTA DEL ESTUDAINTE EN EL PERIDO N°1 ------------------------>  "))
                estudiante.append(nota_1)
                nota_2 = float(input("INGESE LA NOTA DEL ESTUDAINTE EN EL PERIDO N°2 ------------------------>  "))
                while notas_incio > nota_2 or notas_final < nota_2:
                    os.system("cls")
                    print("VALOR NO CONINCIDE CON LA CONFIGURACION INICIAL,DIGITE OTRA VEZ EL VALOR ")
                    print()
                    nota_2 = float(input("INGESE LA NOTA DEL ESTUDAINTE EN EL PERIDO N°2 ------------------------>  "))
                estudiante.append(nota_2)
                nota_3 = float(input("INGESE LA NOTA DEL ESTUDAINTE EN EL PERIDO N°3 ------------------------>  "))
                while notas_incio > nota_3 or notas_final < nota_3:
                    os.system("cls")
                    print("VALOR NO CONINCIDE CON LA CONFIGURACION INICIAL,DIGITE OTRA VEZ EL VALOR ")
                    print()
                    nota_3 = float(input("INGESE LA NOTA DEL ESTUDAINTE EN EL PERIDO N°3 ------------------------>  "))
                estudiante.append(nota_3)
                nota_4 = float(input("INGESE LA NOTA DEL ESTUDAINTE EN EL PERIDO N°4 ------------------------>  "))
                while notas_incio > nota_4 or notas_final < nota_4:
                    os.system("cls")
                    print("VALOR NO CONINCIDE CON LA CONFIGURACION INICIAL,DIGITE OTRA VEZ EL VALOR ")
                    print()
                    nota_4 = float(input("INGESE LA NOTA DEL ESTUDAINTE EN EL PERIDO N°4 ------------------------>  "))
                estudiante.append(nota_4)
                promedio = (nota_1+nota_2+nota_3+nota_4)/4
                estudiante.append(promedio)
                for a in range(1):  
                    estudiantes.append(estudiante)
                print("                                  ")
                opcion = input("DESEA INGRESAR MAS DATOS? SI ES SI ESCRIBA  (si)   DE LO CONTRARIO   (no) ------------------------>  ")
                print("                                  ")
            print("                                  ")
            a =estudiantes
            print("                                  ")
        elif entrada == 2:
            print("                                  ")
            lista(a)
            print("                                  ")
        elif entrada == 3:
            print("                                  ")
            print("                                  ")
            b = promedio_estudiantes((a))
            print("EL PROMEDIO DE LOS ESTUDIANTES     ",b)
            print("                                  ")
            print("                                  ")
            input("Presione ENTER para continuar...")
        elif entrada == 4:
            print("                                  ")
            print("                                  ")
            print(aprobados(a,pasar))
            print("                                  ")
            print("                                  ")
        elif entrada == 5:
            print("                                  ")
            print("                                  ")
            print(mejores(a,mejor))
            print("                                  ")
            print("                                  ")
        elif entrada == 6:
            print("                                  ")
            print("                                  ")
            print(mayor_media(b,a))
            print("                                  ")
            print("                                  ")
        elif entrada == 7:
            print("                                  ")
            print("                                  ")
            print(promedio_estudiante(a))
            print("                                  ")
            print("                                  ")
        elif entrada > 8:
            xd = "VALOR INVALIDO, INGRESE UN VALOR DEL MENU"
            print("                                  ")
            print("                                  ")
            print(f"{xd:>100}")
            print("                                  ")
            print("                                  ")
off ="¡SE HA FINALIZADO EL PROGRAMA/CÓDIGO CON EXITO!!!!!"
print("                                  ")
print("                                  ")
print("                                  ")
print("                                  ")
print("                                  ")
print("                                  ")
print("                                  ")
print("                                  ")
print(f"{off:>100}")
print("                                  ")
print("                                  ")
print("                                  ")
print("                                  ") 
print("                                  ")
print("                                  ")
print("                                  ")
print("                                  ")