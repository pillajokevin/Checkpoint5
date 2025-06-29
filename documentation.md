# Checkpoint 5 

Hola! Mi nombre es kevin, y esta guia esta hecha para ayudar a entender algunos conceptos basicos y fundamentales del lenguaje Python.
## Preguntas a exponer ##

### ** Que es una condicional **
Una condicional en Python permite ejecutar diferentes bloques de codigo dependiendo de si una condicion se cumple o no. 
Es como tomar decisiones en tu programa .

### ** Para que sirve**
Sirve para que el programa pueda responder a diferentes situaciones. Por ejemplo, si un usuario tiene mas de 18 anos,
nos mostrara "Bienvenidos" , y si no , nos mostrara "Acceso denegado" 

### La sintaxis  basicas  son  :

** If : La usamos cuando la condicion se cumple  como en el siguente ejemplo.**

```python 
#Condicional Simple if

if condicion:
    #codigo si cumple la condicion 

Ejemplo :

edad = 20 # Aqui nosotros colocamos la edad de el usuario o la nuestra 

if edad >= 18: # Esta es la condicion 
    print("Eres mayor de edad") # Esto nos imprimira en la terminal si la persona es mayor de edad 
```

#Condicional con elif 
** Se usa cuando quieres comprobar otra condicion diferente si la condicion if no se cumple.
Puedes usar varios elif para evaluar diferentes opciones  **

```python
x = 15

if x < 5:
    print("Es mayor que 5 ")
elif x == 15:
    print("Es igual a 15")

```
En este ejemplo, el 'if' no se cumple (Por que 15 no es menor de 5 )
pero el "elif" si se cumple 'x == 15' , asi que se ejecuta ese bloque

### Condicional con else 
 Else : Lo usamos cuando la condicion de el 'if' y de 'elif' no se cumplen.
El bloque else se ejecuta solo si todas las condiciones anteriores ( if y elif ) son falsas.
El bloque else no lleva condicion.
Es una buena manera de manejar casos alternativos y evitar errores si no se cumple otras condiciones. 


```python
nota = 49 #Esta es la nota que hemos sacado

if nota >= 90: # Aqui ponemos una codicional if  
    print("Excelente")
elif nota >= 50:
    print("Aprovado")
else:
    print("Suspendido")
```
En este ejemplo que tenemos aqui , es como colocariamos la nota de una persona.
El progama revisa la nota que hemos sacado  y lo compara con las condicionales que le hemos dado y como ninguna de 
las codicionales ("if" y "elif") se cumplen salta a ("else") y  nos imprime que esta (Suspendido). 
Esto nos ayuda a que nuestro programa no de error si alguna condicion no cumple. 


### Cuales son los diferentes tipos de bucles en Python y  por que son utiles

Los bucles en python permiten reptir un bloque de codigo varias veces. Son muy utiles para automatizar
tareas repetitivas sin tener que escribir el mismo codigo muchas veces. 

**Para que sirve**

Los bucles sirven para recorrer listas, ejecutar tareas multiples veces, hacer calculos repetitivos, 
procesar datos, entre otros. Son fundamentales para trabajar con colecciones de datos y repetir acciones
en base a una conidcion. 

**Tipos de bucles**

1. Bucle For

El bucle "For" se utiliza para recorrer elementos de una secuencia como una lista una cadena o un rango 
de numeros.

```python

# Recorriendo una lista 
frutas = ['manzana','banana','peras']

for fruta in frutas:
    print(fruta)
```

2. Bucle While 

El bucle "While" se ejecuta mientras una condicion sea verdadera.
En cuanto la condicion deja de cumplirse, el bucle se detiene.


```python

contador = 0 # Se crea una variable llamada contador con un valor 0.

while contador < 5: # El bucle dice 'Mientras contador sea menor que 5 , sigue ejecutando'
    print("Contador:", contador) # Muestra el valor actual de contador
    contador += 1 # Suma 1 a contador en cada vuelta   "Esto evita que el bucle se repita para siempre "
```

por que son utiles ?

Evitamos repetir codigo manualmente:
- En lugar de escribir print(..) cinco veces, el bucle lo hace por nosotros

Se adaptan a diferentes situaciones 
- Puedes usarlos con numeros, entradas del usuario, archivos, etc..

Automatizan tareas 
- Son ideales para tareas que deben repetirse hasta que pase algo (por ejemplo, que usuario escriba'salir').



### Que es una lista por compresion en Python

Una lista por comprension (list comprehension) es una forma rapida y concisa de crear listas en python.
Permite generar una nueva lista aplicando una operacion a cada elemento de una secuencia o iterando sobre ella.

Es como decirle a python  : "Hazme una nueva lista, usando los elementos de otra lista, pero aplicando una transformacion o filtro"

**Para que sirve?**

Sirve para simplificar y acortar el codigo cuando necesitemos crear listas a partir de otras listas o secuencias.
Es muy util cuando queremos aplicar condiciones, transformaciones o filtros a los elementos
de una lista.

En lugar de usar varios renglones con un bucle "for", podemos hacerlo en una sola linea mas clara y legible.


**Sintaxis basica**

```python
[expresion for elemento in iterable if condicion]
```
- Expresion: Lo que quieres anadir a la  nueva lista.
- Elemento: La variable que representa cada valor del iterable.
- Iterable: La secuencia sobre la que estas iterando (como una lista o rango).
- Condicional(opcional): Puedes anadir una condicion para filtrar los valores.

**Ejemplos sencillos**

```python
# Crear una lista con los numeros del 0 al 4

lista = [x for x in range(5)]
print(lista)

# Resultado: [0,1,2,3,4]


# Multipliclar todos los numeros por 10 
numeros = [1,2,3] 
resultado = [n * 10 for n in numeros]
print(resultado)

# Resultado: [10,20,30] , Toma cada numero y lo multiplica por 10


#Convertir letras a mayusculas 
letras =['a','b','c']
mayusculas = [letra.upper() for letra in letras]
print(mayusculas)

# Resultado: ['A','B','C']  Usamos ".upper()" para convertir las letras en mayusculas


#Creamos una lista con solo los numeros mayores que 3 

num = [1,2,3,4,5,6]
mayores = [n for n in num if n >3]
print(mayores)

# Resultado : [4,5,6] , Filtramos y guardamos solo los numeros mayores a 3 
```


### Que es un argumento en Python?

En python, un argumento es un valor que se pasa a una funcion cuando la llamas. Son los 
datos que una funcion necesita para hacer su trabajo.

Por ejemplo, si tienes una funcion que suma dos numeros, los numeros que le pasas para
sumar son los argumentos.

**Para que sirve?**

Sirve para que las funciones sean mas flexibles y reutilizables. En lugar de escribir una funcion 
diferente para cada situacion, puedes usar arguementos para personalizar lo que hace la funcion 
segun los valores que le pases.

Asi, una sola funcion puede trabajar con diferentes datos.

**Sintaxis basica**

```Python

def nombre_funcion(argumento1, argumento2):
    #Codigo que usa los argumentos
    return resultado 

    #Al llamar a la funcion, debes pasarle los valores
```

**Ejemplos**

```Python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Kevin")
# Resultado: Hola, Kevin!
# En este ejemplo, "Kevin" es un argumento que se pasa a la funcion saludar.

def sumar (a, b):
    return a + b
resultado = sumar(5, 3) # Aqui usamos el argumento 5 y 3 y lo pasamos a la funcion Sumar.
    
print(resultado)
# Resultado : 8

```

### Que es una funcion Lambda en Python?

Una funcion __lambda__ en Python es una forma rapida de crear funciones __pequenas y anonimas__ , es decir,
funciones que no necesitan tener un nombre.

Se utiliza cuando necesitas una funcion simple para usar una sola vez o como argumento en otra funcion.


**Para que sirve?**

Sirve para __ahorrar codigo__ y hacerlo mas compacto y facil de leer, especialmente cuando necesitas pasar funciones 
como argumentos a otras funciones (como en __map , filter, sorted, etc__.).

Es muy util cuando necesitas realizar operaciones rapidas sin necesidad de definir una funcion completa con __def__.



**Sintaxis basica**

Funciones lambda en Python

Las funciones "lambda" son una forma __rapida y anonima__ de crear funciones pequenas en una sola linea.
```Python

lambda argumentos: expresion
```
Caracteristicas:

No se usa __def , return__ ni nombre.

Se puede guardar en una variable si quieres reutilizarla.

Muy util para funciones __cortas y temporales__.


**Ejemplos**

**Funcion lambda asignada a una variable**
```Python
sum = lambda a, b: a + b 
print(sum(3, 4 ))

# Resultado: 7
# Esta funcion lambda recibe dos argumentos a y b , y devuelve la suma.

# Es lo mismo que  escribir:

def sum(a, b):
    return a + b 
```

**Funcion lambda como argumento**
```Python

num = [1, 2, 3, 4, 5] # Esto son los datos que le damos
cuadrados = list(map(lambda x: x ** 2, num)) # Aqui aplicamos lamp dentro de map y colocamos la formula para que eleve al cuadrado. 
print(cuadrados)
# Resultado: [1, 4, 9, 16, 25]
# Explicacion : Aqui estamos usando lambda dentro de map() para aplicar una operacion a cada
# elemento de la lista . Cada numero x se eleva al cuadrado (x ** 2 )
```
Las funciones lambda son ideales cuando necesitamos una funvion rapida, pequena y que solo usaras una vez, por ejemplo en 
funciones como __map(), filter(), o sorted()__.



### Que es un paquete pip en pyhton?

Un paquete pip es una herramienta que se utiliza para instalar, actualizar y gestionar bibliotecas y paquetes adicionales en Python.
Pip es el gestor de paquetes oficial de Python, y permite a los desarolladores intalar facilemtne las bibliotecas que necesiten 
para trabajar en sus proyectos.


**Para que sirven**

Sirve para descargar, instalar y gestionar librerias que no estan incluidas de manera predeterminada en la instalacion estandar de Python.
Gracias a pip, es posible acceder a miles de paquetes disponibles en el Python Package Index(PyPI), el repositorio oficial de paquetes
de Python.

**Sintaxis basica**

Instalacion de un paquete :

- pip install nombre_paquete # Esto intala el paquete

Ademas con pip puedes actualizar un paquete:

- pip install --upgrade nombre_paquete

Desinstalar un paquete : 

- pip uninstall nombre_paquete 

Listar los paquetes instalados:

- pip list 


Si deseas instalar una libreria popular como NumPy para trabajar con algebra lineal, puedes hacerlo usando pip.

Lo instalariamos asi:

pip install numpy 

Una vez insatalado podemos usar la libreria en nuestro codigo de python.

```Python 

import numpy as np

# Crear una matriz 2 x 2 con numpy

matriz = np.array([[1, 2],[3, 4]])

print(matriz)
```
