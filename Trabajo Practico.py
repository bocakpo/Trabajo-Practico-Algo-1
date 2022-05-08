PALABRA_A_ADIVINAR = "gatos"


def obtener_color (color) :
    colores = {"Verde": "\x1b[32m" , "Amarillo" : "\x1b[33m","GrisOscuro" : "\x1b[90m","Defecto" : "\x1b[39m"
    }
    return colores[color]

def verificacion(palabra):
    retorno = ""
    for i,letra in enumerate(palabra):
        if letra in PALABRA_A_ADIVINAR:
            letra_nueva = obtener_color("Amarillo") + letra + obtener_color("Defecto")
            if i == PALABRA_A_ADIVINAR.find(letra):
                letra_nueva = obtener_color("Verde") + letra + obtener_color("Defecto")
        else:letra_nueva = letra
        retorno = retorno + letra_nueva
    return(retorno)

def mostrar_interfas(progreso):
    print("Palabra a adivinar: ", progreso)
    arriesgo = input("Arriesgo: ")
    print(verificacion(arriesgo))

def main():
    progreso = "?????"
    mostrar_interfas(progreso)

main()

#print ( obtener_color ( "Verde" ) + " A " + obtener_color ( "Amarillo" ) + "B" + obtener_color ( "GrisOscuro" ) + " C " + obtener_color ( "Defecto" ) )