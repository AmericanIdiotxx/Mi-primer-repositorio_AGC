#En teoría estoy en development
from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from division import dividir

while True:
    print("""Hola, bienvenido a la super calculadora de Arturo y Male, ¿con qué operación te podemos ayudar hoy? 
          1. Sumar 
          2. Restar 
          3. Multiplicar 
          4. Dividir 
          5. Salir""") #Les mostramos las opciones
    
    operacion = int(input("Elige una opción (1-5): ")) #Pedimos que elijan

    x = float(input("Ingresa el primer número: "))
    y = float(input("Ingresa el segundo número: "))

    if operacion == 1:
        resultado = sumar(x, y)
        print(f"El resultado de la suma es: {resultado}")
    elif operacion == 2:
        resultado = restar(x, y)
        print(f"El resultado de la resta es: {resultado}")
    elif operacion == 3:
        resultado = multiplicar(x, y)
        print(f"El resultado de la multiplicación es: {resultado}")
    elif operacion == 4:
        if y != 0:
            resultado = dividir(x, y)
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Trataste de dividir entre cero <(°_°)>")
    elif operacion == 5:
        print("Arturo y Male te dicen adióooooooos :))")
        break
    else:
        print("Opción no válida pipipi")