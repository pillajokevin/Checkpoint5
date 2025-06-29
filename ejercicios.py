#Ejercicios 

# Tenemos que  realizar los siguientes ejercicios 

# 1- Crear un bucle For de Python

# Creamos una lista de numeros 
numeros = [1, 2, 3, 4, 5]

# Usamos un bucle for para imprimir cada numero

for numero in numeros:
    print(numero)


# 2- Crear una funcion Python llamada suma que tome 3 argumentos y devuelva la suma de los 3 

# Definimos la funcion suma 
def suma(a, b, c):
    return a + b + c

resultado = suma(3, 5, 7)
print(f'El resultado de la suma es: {resultado}')

# 3- Cree una funcion lambda con la misma funcion de suma que acaba de crear.

# Creamos una funcion lambda que sume 3 numeros.

suma_lambda = lambda a, b, c: a + b + c

resultado_lambda = suma_lambda(3, 7,  8)
print(f'El resultado de la suma con lambda es: {resultado_lambda}')


# 4- Utilizando la siguiente lista y variable , determine si el valor de la variable coinciden 
# o no con un valor de la lista. *Sugerencias, si es necesario, utilice  un bulce for in y el operador in.

# Definimos los valores 
nombre = 'Enrique'
lista_nombres = ['Jessica', 'Paul', 'George', 'Henry', 'Adan']

# Usaremos un bucle for y el operador 'in' para vereficar si el nombre esta en la lista 

if nombre in lista_nombres: 
    print(f'{nombre} esta en la lista.')
else:
    print(f'{nombre} no esta en la lista.')