#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:24:22 2020

@author: yosselin
"""
"""
import Funciones_3 as fun
import numpy as np
import random

# Datos de entrada
#a = float(input("Ingrese el comienzo de la barra.                a="))
#b = float(input("Ingrese el fin de la barra.                     b="))
#K = float(input("Ingresa la conductividad térmica del material   k="))
#N = int(input("Ingresa el número de nodos que desea            N="))
#Ta = float(input("Ingrese la temperaruta al inicio.               Ta="))
#Tb = float(input("Ingrese la temperaruta al final.                Tb="))

#----- Parametros de entrada ----
a=0  #Inicio de la barra
b=1  #Fin de la barra


N=50 # Numero de nodos (lugares donde quiero saber la temperatura)
Ta=2 # Primera condicion de frontera (Temperatura en el primer nodo)
Tb=1 # Segunda condicion de frontera (Temperatura en el ultimo nodo)
#----- 

# Calculo de constantes necesarias
#h= 0.0196078
h = (b-a)/(N+1)

x = np.linspace(a,b,N+2)
K=np.zeros(N+2)
for i in range(0,N+2):
   K[i]=(random.random())
l=len(K)
print("aleatorea",K)


# ---- Calibración 3 ----
# Matriz con diferencias finitas
A = fun.creacion_matriz_diagonal(N,-1,h,K) #Siatema matricial para ec. de Poisson 1D
#print("\n Matriz del sistema : \n", A)

# Condiciones de Dirichlet
f = np.zeros(N)   

for i in range(1,N-1):
    f[0]=(-1*(K[i-1]+K[i])/2.)
    f[-1] =(-1*(K[i+1]+K[i])/2.)
print("f: ",f)
print()
print("A[0]",A[0,0])
u1 = fun.sol_sistema(A,f,N)

#u1[0]=Ta*(-1*(K[i-1]+K[i])/2)
#u1[-1] =Tb *(-1*(K[i+1]+K[i])/2)
u1[0]=Ta
u1[-1]=Tb
print("Solución: ",u1)

# Error entre la solución numerica y la exacta
#Error1 = np.sqrt(h) * np.linalg.norm(fun.sol_analitica_cali2(x,N) - u1)
#print(" Error calibración 2 = %12.10g " % Error1)

#Grafica de la solución exacta y analítica 
grafica0 = fun.grafica_solucion(x,K,"K(x)","Solución numérica", "Conductividad","Solucion_cali3k_b.png" )
grafica1 = fun.grafica_solucion(x,u1,"Calibración 3: Conductividad aleatoria","Solución numérica", "Solución Numerica","Solucion_cali3_b.png" )

"""
# PROGRAMA PARA LA RESOLUCIÓN DE LA ECUACIÓN DE CALOR SIN FUENTES O SUMIDEROS

import Funciones_Final as fun
import numpy as np
import random

# Programa principal
print()
print("+----------------------------------------------------+")
print("|      Solucion de la transferencia de calor         |")
print("+----------------------------------------------------+")

print('Opciones para la ejecución: \n'
	  '1.- Tomar datos de ejemplo de un archivo \n'
      '2.- Ingresar los datos manualmente.')

sel = int(input('Escoja una opción.\n'))

a,b,N,Ta,Tb,k,S,f = fun.Ingreso(sel)

# Cálculo de Constantes
h,x,lar = fun.Constantes(a,b,N)
print("\n-------------------------------------------------")
print("El ancho de la malla es: ",h)
print("El largo de la barra es: ",lar)
print("---------------------------------------------------\n")

# Creación de matriz diagonal


K=np.zeros(N+2)
for i in range(0,N+2):
   K[i]=(random.random())
l=len(K)

A= fun.Matriz_Diago3(N,-1,h,K)

B = np.zeros(N)   

for i in range(1,N-1):
    B[0]=(-1*(K[i-1]+K[i])/2.)
    B[-1] =(-1*(K[i+1]+K[i])/2.)
    
# Solucion del sistema
u = fun.Sol_Sitema(A,B,N,Ta,Tb)

# Solución analítica del problema
u_exa = fun.Sol_Analitica(a,b,Ta,Tb,N)

error = fun.Error(u,u_exa,N)

print("\n--------------------------------------------")
print("El vector b es: ",B)
print("La matriz A es: \n",A)
print("La solución numérica es: \n",u)
print("La solución analítica es: \n",u_exa)
print("El error en la solución es: \n",error)
print("\n--------------------------------------------\n")

# Graficando la solucion
fun.Graficas_Cali3(x,K,u)

# Guardando los datos
fun.Escritura(u,u_exa)