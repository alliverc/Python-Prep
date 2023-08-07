#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

num = 4

if num >0:
    print("el numero es mayor a cero-> ",num)
elif num<0:
    print("el numero es menor a cero-> ",num)
else:
    print("el numero es ",  num)
print("************************************************")





# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
var1 = "5"
var2 = 4

if type(var1)== type (var2):
    print (f"son del  mismo tipo las variables{type(var1),type(var2)}")
else:
    print(f"las variables no son del mismo tipo{type(var1),type(var2)}")
print("************************************************")




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
num = 21
for i in range (1,num):
    #print(i)
    if i%2 == 0:
        print("par",i)
    else:
        print("impar",i)  
print("************************************************")
    





# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(0,6,1):
    num2 =i**3
    print(f"{i}->elevado a la potencia de 3-> es = {num2}")
print("************************************************")




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
num2 = 5
for i in range (1,num2):
    continue
print(i)
print("************************************************")






# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
n = 5
if (type(n) == int):
    if (n > 0):
        factorial = n
        while (n > 2):
            n = n - 1
            factorial = factorial * n
        print('El factorial es', factorial)
    else:
        print('La variable no es mayor a cero')
else:
    print('La variable no es un entero')

    
print("************************************************")




# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
num = 5
i=1
while i<=num:
    print("ciclo dentro de while")
    for i in range(1,num):
        print("coclo dentro de for")
    if num == num:
        break 

print("************************************************")

# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
d = 5
for x in range (d):
    while x <=d:
        print("ciclo while denro de for")
        break
print("************************************************")
    
# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
primos = 30
conta = 0
conta2 =0
primo = False

if primos <0 and primos>30:
    print ("la informacion ingresada no es valida")
else:
    i = 0
    while i < primos:
        if i%2==0:
            primo = False
            #print ("son pares",i)
            conta = conta +1 
        else:
            print ("Son primos",i)
            conta2 = conta2 +1
        i = i+1
    print (f"Total numeros pares {conta}")
    print (f"Total numeros primos {conta2}")
print("************************************************")


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

primos = 30
conta = 0
conta2 =0
primo = False

if primos <0 and primos>30:
    print ("la informacion ingresada no es valida")
else:
    i = 0
    while i < primos:
        if i%2==0:
            print ("son pares",i)
            conta = conta +1 
            break
        else:
            print ("Son primos",i)
            conta2 = conta2 +1
        i = i+1
    print (f"Total numeros pares {conta}")
    print (f"Total numeros primos {conta2}")
print("************************************************")




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
primos = 30
conta_pares = 0
conta_primos = 0

if primos < 0 or primos > 30:
    print("La información ingresada no es válida. Debe ser un número entre 0 y 30.")
else:
    for num in range(2, primos + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break

        if es_primo:
            print(f"Es primo: {num}")
            conta_primos += 1
        elif num % 2 == 0:
            print(f"Es par: {num}")
            conta_pares += 1

    print(f"Total números pares: {conta_pares}")
    print(f"Total números primos: {conta_primos}")

print("************************************************")




# In[57]:

primos = 50
conta_pares = 0
conta_primos = 0

if primos < 0 or primos > 30:
    print("La información ingresada no es válida. Debe ser un número entre 0 y 30.")
else:
    for num in range(2, primos + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break

        if es_primo:
            print(f"Es primo: {num}")
            conta_primos += 1
        elif num % 2 == 0:
            print(f"Es par: {num}")
            conta_pares += 1

    print(f"Total números pares: {conta_pares}")
    print(f"Total números primos: {conta_primos}")

print("************************************************")


# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# In[58]:

primos = 50
conta_pares = 0
conta_primos = 0

if primos < 0 or primos > 30:
    print("La información ingresada no es válida. Debe ser un número entre 0 y 30.")
else:
    for num in range(2, primos + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break

        if es_primo:
            print(f"Es primo: {num}")
            conta_primos += 1
        elif num % 2 == 0:
            print(f"Es par: {num}")
            conta_pares += 1

    print(f"Total números pares: {conta_pares}")
    print(f"Total números primos: {conta_primos}")
print("************************************************")


# In[59]:
primos = 50
conta_pares = 0
conta_primos = 0

if primos < 0 or primos > 30:
    print("La información ingresada no es válida. Debe ser un número entre 0 y 30.")
else:
    for num in range(2, primos + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break

        if es_primo:
            print(f"Es primo: {num}")
            conta_primos += 1
        elif num % 2 == 0:
            print(f"Es par: {num}")
            conta_pares += 1

    print(f"Total números pares: {conta_pares}")
    print(f"Total números primos: {conta_primos}")

print("************************************************")

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
num1 = 100
num2 = 300
x = 100
while  num1>=x or x<=num2:
  if x%3==0 and x%4==0:
    print("es divisible por 12 = ",x)
  #print("ingreso",x)
  x = x+1

print("************************************************")






# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1



# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

n = 100
while(n<=300):
    if (n % 6 == 0):
        print('El número es: ', str(n))
        break
    n += 1
