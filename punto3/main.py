

from Persona import Persona


opcion = 99
persona = Persona("", "", "", "")
while(opcion != 0):


 
    print("1). crear cliente")
    print("2). consultar saldo")
    print("3). monto a retirar")
    print("4). monto a ingresar")
    opcion = int(input("elige la opcion: "))

    if opcion == 1:
        nombre = input("nombre del cliente: ")
        apellido = input("apellido del cliente: ")
        cedula = input("cedula del cliente: ")
        ciudad = input("ciudad del cliente: ")
        persona = Persona(nombre, apellido, cedula, ciudad)
    elif opcion==2:
        print(persona.cuenta.consultarSaldo())
    elif opcion == 3:
        monto = int(input("monto a retirar: "))
        print(persona.cuenta.retirar(monto))
    elif opcion == 4:
        monto = int(input("monto a consignar: "))
        print(persona.cuenta.consignar(monto))
    else:
        print("Opcion invalido")
        
else:
    print("gracias hasta luego")
    

   
