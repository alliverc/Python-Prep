#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

var = 25
print(var)
# In[7]:

# 2) Imprimir el tipo de dato de la constante 8.5

constan = 8.5
print (type(constan))

# In[3]:



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

print (type(var))

# In[8]:





# 4) Crear una variable que contenga tu nombre
nombre = ("henry allyver")
# In[2]:




# 5) Crear una variable que contenga un número complejo
numeco = (4+5j)


# In[3]:





# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(numeco))

# In[4]:





# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales


# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
valor_true1 = True
valor_true_estring = "True"#esta es string, por las comillas
# In[3]:





# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(valor_true1))
print(type(valor_true_estring))

# In[5]:





# 10) Asignar a una variable, la suma de un número entero y otro decimal

suma = 7 + 8.99


# In[1]:





# 11) Realizar una operación de suma de números complejos

sumacom= 4+5j
suma2 =  99 + 78j
print(sumacom+suma2)

# In[2]:





# 12) Realizar una operación de suma de un número real y otro complejo
suma3 = 789.25 + 555j
print (suma3)
# In[4]:





# 13) Realizar una operación de multiplicación

n1 = 3
n2 = 45
multiplicacion = n1*n2
print (multiplicacion)

# In[5]:





# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

elevar = 2**8
print (elevar)




# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
cociente = 27/4
print(cociente)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
cociente = 27//4
print (cociente)





# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
cociente = 27%4
print (cociente)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
opera = 6*4+3
print (opera)




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

Mi_variable = "henry Allyver"
Mi_variable2 ="Fonseca Calderon"
print(Mi_variable+" "+Mi_variable2)





# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
print(2 == "2")#es false ya que el primer valor es entero y el segundo es de tipo string


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
a = 2
b = "2"
resultado = a == int(b)
print(resultado)




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
#a = float('3,8')#porque se esta con una coma y debe tener punto para hacer la conversion





# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

u = 3
u-=1
print (u)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
r =1 << 2#desplaza dos posiciones a la izquierda de indica que es numero 1
print (r)




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

#opera = 2 +"2"
#print (opera)#genera error por que el 2 de comillas es string 




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

texto_1 = "henry Fonseca"
texto_2 = 3
print(texto_1 * texto_2 + str(texto_2))
