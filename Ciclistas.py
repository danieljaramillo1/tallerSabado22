bandera = 1
ciclistas = []


def agregarCiclista(nombre,edad,pais,equipo,min):

    ciclista = {}
    ciclista["nombre"] = nombre
    ciclista["edad"] = edad
    ciclista["pais"] = pais
    ciclista["equipo"] = equipo
    ciclista["min"] = min
    ciclistas.append(ciclista)

    return(ciclistas)

def mostrarMenor():
    
    menor = 50000
    for i in range(0, len(ciclistas)):
                if ciclistas[i]["min"] < menor:
                  nombre = ciclistas[i]["nombre"]
                  menor = ciclistas[i]["min"]
    print(f"el ganador fue : {nombre}") 
    print(f"el tiempo menor fue de: {menor}") 
    return(menor)
    



while bandera != 0:
    print(".1 Para agregar ciclista")
    print(".2 Mostrar menor tiempo")
    print(".0 Para la Salir  ")
    seleccion = int(input(" Elije Tu opcion: "))
    bandera = seleccion
    if seleccion == 0:
        print("Hasta luego")
    elif seleccion == 1:

        nombre = input("Dame nombre del Ciclista: ")
        edad = input("Dame edad del Ciclista: ")
        pais = input("Dame nacionalidad del Ciclista: ")
        equipo = input("Dame equipo del Ciclista: ")
        min = int(input("Dame tiempo del Ciclista: "))

        agregarCiclista(nombre,edad,pais,equipo,min)

    elif seleccion == 2:
        mostrarMenor()


        





    




    
