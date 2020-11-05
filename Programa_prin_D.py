#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Funciones_D as fun
import numpy as np
import matplotlib.pyplot as plt

# Programa principal 
print()
print("+----------------------------------------------------+")
print("|      Solucion de la transferencia de calor         |")
print("+----------------------------------------------------+")


# Datos de entrada
a = float(input("Ingrese el comienzo de la barra.                a="))
b = float(input("Ingrese el fin de la barra.                     b="))
K = float(input("Ingresa la conductividad térmica del material   k="))
N = int(input("Ingresa el número de nodos que desea            N="))
Ta = float(input("Ingrese la temperaruta al inicio.               Ta="))
Tb = float(input("Ingrese la temperaruta al final.                Tb="))
s = float(input("Ingrese la fuente o sumidero.                    s="))

# Calculo de constantes necesarias
h = (b-a)/(N+1)
r = K/(h**2)
x = np.linspace(a,b,N+2)
largo = b-a

# Impresion de las constantes 
print("\n-------------------------------------------------")
print("El ancho de la malla es: ",h)
print("La constante r es:       ",r)
print("El largo de la barra es: ",largo)
print("---------------------------------------------------\n")

# Llamado a funcion para crear arreglos
q = np.ones(N) * s
b = fun.Vector_aux(N,Ta,Tb,-1*q)

#Llamando a la función creación de matriz
A = fun.creacion_matriz(N)

# Llamar a la función solución del sistema
u = fun.sol_sistema(A, b, N)

# Ingresando las condiciones de frontera
u[0] = Ta
u[-1] = Tb

# Impresion de los vectores y matrices
print("\n Matriz del sistema : \n", A)
print("\n Lado derecho del sistema : \n", b)
print("\n Vector solucion:")
print("El vector solución es:")
for i in range(len(u)):
    print(u[i])

#Solución analitica para un medio estacionario sin fuente o sumidero q=0
a1 = fun.sol_analitica(Ta,Tb,x,N,largo)
print('vector a1',a1)
# Llamada de la función para Gráficar
if (s==0):
    grafica = fun.grafica_solucion(x, u,a1)
    plt.savefig("Solucion.png")
else:
    di = np.zeros(N)
    N = fun.Dirichlet()
# Llamado a la funcion de escritura
archivo = fun.escritura(largo,Ta,Tb,N)