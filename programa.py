#Funcion que no retorna ningun valor, pero realiza una tarea en especifico
def saludar():
    print('Hola, un gusto verte')

# def saludar(arg):
#     print(f'Hola {arg}, un gusto verte')

def saludar(arg):
    return (f'Hola {arg}, un gusto verte')
    


x = saludar('mario')
# print(x)

#LISTAS
frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana'] 
# Cuantas veces esta X en frutas
# print(frutas.count('manzana'))
# print(frutas.count('papaya'))
#retorna la posicion de X en frutas
# print(frutas.index('banana'))
#comienza desde la posicion dada (4) a buscar un elemento X(banana)
# print(frutas.index('banana',4))
#invierte el orden de la lista, el ultimo pasa a ser el primer elemento de la lista 
# print(frutas.reverse())
# print(frutas)
# print(frutas.reverse())
# print(frutas)
#agregamos un elemento a la lista
# print(frutas.append('grape'))
# print(frutas)
#ORDENA LA LISTA DE MENOR A MAYOR. ALFANUMERICO
# print(frutas.sort())
# print(frutas)
#POP CAPTURA AL ELEMENTO DE LA POSICION X QUE SE ENVIE Ó SI NO SE ASIGNA, CAPTURARA EL ULTIMO ELEMENTO
# precios = [600, 700, 100, 400, 300, 500]
# print(precios)
# capturado = precios.pop(2)
# print(capturado)
# print(precios)
#liberar el capturado
# precios.insert(0, 100)
# print(precios)
#se ordena la lista y se invierte
# precios.sort()
# precios.reverse()
# print(precios)
# copiaDePrecios = precios.copy()
# print(copiaDePrecios[0])
# copiaDePrecios.reverse()
# print(precios)
# print(copiaDePrecios)
# copiaDePrecios = precios.copy()
# print(copiaDePrecios)
# print(precios)

# del copiaDePrecios
# print(copiaDePrecios[::2])
# copiaDePrecios[0:2] = [1, 2]
# if(copiaDePrecios.index(1000)):
#     print('ganador')
# else:
#     print('perdedor')


# estudiantes = ["Jose", "Raul", "Marcelo"]
# estudiantes.extend(["Dario", "Natalia"])
# print (estudiantes)
# print(estudiantes.index("paul"))

# import fibo
# fibo.fib(1000)

# data = fibo.fib2(100)
# print(data)

# fibo.__name__

