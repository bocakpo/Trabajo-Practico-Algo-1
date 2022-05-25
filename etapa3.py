PALABRA_A_ADIVINAR = "CASAS"
LISTA_ACENTOS = ["Á", "á", "É", "é", "Í", "í", "Ó", "ó", "Ú", "ú"]

'''Permite colorear la impresion por pantalla'''
def obtener_color (color) :
    colores = {"Verde": "\x1b[32m" , "Amarillo" : "\x1b[33m","Gris" : "\x1b[90m","Defecto" : "\x1b[39m"
    }
    return colores[color]


'''Cambia la letra con tilde por la misma sin tilde'''
def cambio_acentos(letra):
    letra_cambiada = {"á":"a","é":"e","í":"i","ó":"o","ú":"u","Á":"a","É":"e","Í":"i","Ó":"o","Ú":"u"}
    for key, value in letra_cambiada.items():
        letra = letra.replace(key, value)
    return letra


'''colorea las letras correctas de la palabra
    Pre: palabra ingresada por usuario
    Post: palabra coloreada de acuerdo a las reglas del juego'''
def verificar_palabra(palabra):
    lista_dato = list(PALABRA_A_ADIVINAR)
    lista_ingresada = list(palabra)
    palabra_color = ""
    letra_nueva = ""
    palabra = ""
    for numero in range(len(lista_dato)):
        letra = lista_ingresada[numero]
        if letra in LISTA_ACENTOS:
            letra = cambio_acentos(letra)
            letra = letra.upper()
        if letra == lista_dato[numero]:
            letra_nueva = obtener_color("Verde") + letra + obtener_color("Defecto")
        elif letra in lista_dato:
            letra_nueva = obtener_color("Amarillo") + letra + obtener_color("Defecto")
        else:
            letra_nueva = obtener_color("Gris") + letra + obtener_color("Defecto")
        palabra_color += letra_nueva
        palabra += letra
    verificar_palabra.palabra = palabra
    return palabra_color

'''Envía el mensaje "Perdiste!" o "Ganaste!" según corresponda'''
def ganar_o_perder(palabra):
    if palabra == PALABRA_A_ADIVINAR:
       resultado = "Ganaste!"
    else:
        resultado = "Perdiste!"
    return resultado


'''pide el ingreso de la palabra y verifica que cumple con los requisitos para ser ingresada'''
def ingreso():
    palabra = input("Arriesgo: ").upper()
    while palabra.isalpha() == False or len(palabra)!= len(PALABRA_A_ADIVINAR):
        if palabra.isalpha() == False:
            print("\nNo ha ingresado una palabra, vuelva a intentarlo.")
            palabra = input("Arriesgo: ").upper()
        elif len(palabra)!= len(PALABRA_A_ADIVINAR):
            print("\nLa palabra ingresada debe tener " + f"{len(PALABRA_A_ADIVINAR)}" + " letras, vuelva a intentarlo.")
            palabra = input("Arriesgo: ").upper()
    return palabra


'''muestra y devuelve todas las palabras intentadas y el progreso de como se va formando la palabar a adivinar'''
def mostrar_interfaz(historial, progreso,cantidad_de_intentos, intento, intento_coloreado):
    for pos, letra in enumerate(intento):
        if letra == PALABRA_A_ADIVINAR[pos]:
            progreso[pos] = letra
    print("Palabra a adivinar: ", "".join(progreso))
    historial[cantidad_de_intentos] = intento_coloreado
    for palabra in historial:
        print(palabra)
    return historial,progreso
    

def juego():
    historial = ["?????","?????","?????","?????","?????"]
    progreso = ["?","?","?","?","?"]
    resultado = ""
    MAXIMO_INTENTOS= 5
    cantidad_de_intentos = 0

    while cantidad_de_intentos < MAXIMO_INTENTOS and resultado != "Ganaste!":
        intento = ingreso()
        intento_coloreado = verificar_palabra(intento)
        resultado = ganar_o_perder(intento)
        historial,progreso = mostrar_interfaz(historial, progreso,cantidad_de_intentos,intento, intento_coloreado)
        cantidad_de_intentos +=1            

    print(resultado)
        
juego()