num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
salida = 0

mayor = lambda num1,num2,salida: salida+1 if num1>num2 else salida-1

print(mayor(num1,num2,salida))
print("El primer numero es mayor") if salida==1 else print("El segundo numero es mayor")
