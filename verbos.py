import os
import re
os.system("cls")


yo = "o"
tu = "as"
el = "a"
nosotros = "amos"
vosotros = "áis"
ellos = "an"


def yo(palabra):
    palabra = list(palabra)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    palabra.append("o")
    unir = "".join(palabra)
    return(f" YO : {unir}")

def tu(palabra):
    palabra = list(palabra)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    palabra.append("a")
    palabra.append("s")
    unir = "".join(palabra)
    return(f" TU : {unir}")

def el(palabra):
    palabra = list(palabra)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    unir = "".join(palabra)
    return(f" EL : {unir}")

def ella(palabra):
    palabra = list(palabra)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    unir = "".join(palabra)
    return(f" ELLA : {unir}")

def nosotros(palabra):
    palabra = list(palabra)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    palabra.append("a")
    palabra.append("m")
    palabra.append("o")
    palabra.append("s")
    unir = "".join(palabra)
    return(f" NOSOTROS : {unir}")

def vosotros(palabra):
    palabra = list(palabra)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    palabra.append("á")
    palabra.append("i")
    palabra.append("s")
    unir = "".join(palabra)
    return(f" VOSOTROS : {unir}")

def ellos(palabra):
    palabra = list(palabra)
    tamano = len(palabra)
    palabra.pop(tamano-1)
    palabra.append("n")
    unir = "".join(palabra)
    return(f" ELLOS : {unir}")
continuar = "si"
while continuar == "si":
    palabra = input("DIGITE LA PALABRA QUE QUIERA CONJUGAR :")
    print()
    print(yo(palabra))
    print(tu(palabra))
    print(el(palabra))
    print(ella(palabra))
    print(nosotros(palabra)) 
    print(vosotros(palabra))
    print(ellos(palabra))
    print()
    
    continuar = input("DESEA CONJUAR MAS PALABRAS si o no :")
    os.system("cls")
