#forma seria dividir el numero entre 2, si se puede, el numero no es primo
#if numero no es primo, print("no es primo")
#else: print("es primo")
#Los números primos hasta 100 son 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.

numeroPrimo = 0
numeroNoPrimo = 0
cantidadDeNumeros = 0

numero1 = 0
numero2 = 0
numero3 = 0
numero4 = 0
numero5 = 0

primo = True


print("Bienvenido a mi calculadora misteriosa, esta vez la funcion de esta sera ver si un numero es primo o no")
cantidadDeNumeros = int(input("Ingresa la cantidad de numeros a verificar: "))

numero1 = int(input("Bien, ahora ingresa el primer numero, recuenda que este tiene que ser un numero entero: "))
if numero1 % 1 == 0:


    while primo:


        if numero1 % 1 == 0:
            primo = True
        
            print("Este numero es primo")
            numeroPrimo += 1
            break
    

        else:
            primo = False
            print("Este numero no es primo")
            numeroNoPrimo += 1
            break
else:
     print("El numero tiene que ser par, intenta de nuevo")


numero2 = int(input("Bien, ahora ingresa el segundo numero numero: "))

