#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Prueba import *
import numpy as np
import matplotlib.pyplot as plt

# Programa principal 


# Llamar a la función solución del sistema
u = sol_sistema(A, b)

# Ingresando las condiciones de frontera
u[0] = Ta
u[-1] = Tb

# Impresion de los vectores y matrices
print("\n Matriz del sistema : \n", A)
print("\n Lado derecho del sistema : \n", b)
print("\n Vector solucion:")
print("El vectro solución es:")
for i in range(len(u)):
    print(u[i])


#Llamada de la función para Gráficar
grafica=grafica_solucion(x, u)

