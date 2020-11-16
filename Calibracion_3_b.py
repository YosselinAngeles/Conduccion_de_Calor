#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:24:22 2020

@author: yosselin
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