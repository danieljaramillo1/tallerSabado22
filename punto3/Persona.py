import random

from Cuenta import Cuenta

class Persona:

    def __init__(self, nombre,apellido,cedula,ciudad):
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        self.ciudad=ciudad
        self.cuenta = Cuenta(random.randint(1000000,9999999),random.randint(0,10000000))

    def mostrarPersona(self):
        print(self)