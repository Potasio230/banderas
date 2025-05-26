#banderassss
#esto se llama "programacion FUNCIONAL "
abrirMenu = False

abrirPokedex = False
abrirEquipo = False
abrirMochila = False
Guardado = False
volver = False

def pokedex(abrirPokedex):
    if abrirPokedex == True:
        int(input("Ingresa el numero de pokedex de un pokemon, por ahora, esta pokedex está actualizada hasta el quinto pokemon"))
    else:
        abrirPokedex == False
        print("Cierra pokedex")

def equipo(abrirEquipo):
    if abrirEquipo == True:
        print("Este es tu equipo: ")
        print("1. Aegilash")
        print("2. Gengar")
        print("3. Decidueye")
        print("4. Tiranitar")
        print("5. Pikachu")
        print("6. Charizard")

        def elegirEquipo():
            if elegirEquipo == 1:
                print("Aegilash:")
            elif elegirEquipo == 2:
                print("Gengar")
            elif elegirEquipo == 3:
                print("Decidueye")
            elif elegirEquipo == 4:
                print("Tiranitar")
            elif elegirEquipo == 5:
                print("Pikachu")
            elif elegirEquipo == 6:
                print("Charizard")
    else:
        abrirEquipo == False
        print("Cierras el equipo")

def mochila(abrirMochila):
    if abrirMochila == True:
        print("Has abierto la mochila")
        print("Tienes los siguientes objetos: ")
    else:
        abrirMochila == False
        print("Cierro mochila")

def guardar(Guardado):
    if Guardado == True:
        print("Guardando...")
        print("¡Partida guardada!")
    else:
        print("Cuidado, la partida no se ha guardado")

def menuDos():
    print("Menu abierto")
    print("1. Pokedex")
    print("2. Equipo")
    print("3. Mochila")
    print("4. Guardar")
    print("5. Volver")
    opcionDentroMenu = int(input("Ingrese la opcion que desee:"))

#opcion 1
    if opcionDentroMenu == 1:
        print("Has abierto la pokédex")
        pokedex(True)
    else:
        print("Cierras la pokedex")
#opcion 2
    if opcionDentroMenu == 2:
        print("Has abierto tu equipo")

def pokedex(abrirEquipo):
    if abrirEquipo == True:
        print("Este es tu equipo: ")
        print("1. Aegilash")
        print("2. Gengar")
        print("3. Decidueye")
        print("4. Tiranitar")
        print("5. Pikachu")
        print("6. Charizard")

        def elegirEquipo():
            if elegirEquipo == 1:
                print("Aegilash:")
            elif elegirEquipo == 2:
                print("Gengar")
            elif elegirEquipo == 3:
                print("Decidueye")
            elif elegirEquipo == 4:
                print("Tiranitar")
            elif elegirEquipo == 5:
                print("Pikachu")
            elif elegirEquipo == 6:
                print("Charizard")

    else:
        print("Cierras tu equipo")  

#opcion 3
    if opcionDentroMenu == 3:
        print("Has abierto tu mochila")
        mochila(True)
    else:
        print("Cierro mochila")
#opcion 4
    if opcionDentroMenu == 4:
        print("Has guardado la partida")

    else:
        print()
#opcion 5
    if opcionDentroMenu == 5:
        print("Volviendo...")



def menu(opcion): #aca invocamos a la funcion menu
    global abrirMenu

    if opcion == 1:
        abrirMenu = True
        menuDos()

    if opcion == 2:
        abrirMenu = False
        print("Menu cerrado")




print("Bienvenido al menu")
print("1. Abrir menu")
print("2. Cerrar menu")
opcion = int(input("Ingrese la opcion que desee:"))
menu(opcion)