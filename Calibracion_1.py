#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 21:54:01 2020

@author: yosselin
"""
import Funciones_1 as fun
import numpy as np

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
K=1#Conductividad
N=30# Numero de nodos (lugares donde quiero saber la temperatura)
Ta=1 # Primera condicion de frontera (Temperatura en el primer nodo)
Tb=1 # Segunda condicion de frontera (Temperatura en el ultimo nodo)
#----- 

# Calculo de constantes necesarias
h = (b-a)/(N+1)
r = K/(h**2)
x = np.linspace(a,b,N+2)

B0 = fun.Vector_aux(N,Ta,Tb)

# ---- Calibración 1 ----
# Condiciones de Dirichlet
# Segunda derivada de u(x) = -f^2 u(x) con x [0,1]

#Formación de f
f0=(np.pi)**2

print(B0)

# Sistema matricial sumando en la f en la diagonal principal
A0 = fun.creacion_matriz_diagonal1(N,-2,f0,h) 
print(A0)
# Solución númerica del sistema
u0 =fun.sol_sistema(A0,B0,N)
u0[0]=1
u0[-1]=1
print('vector solucion',u0)

# Solución analítica
b1 = 1
a0 =fun.sol_analitica_cali1(x,N,b1,h)

#Grafica de la solución exacta y analítica 
grafica0 = fun.grafica_solucion(x,u0,"Calibración 1: Condiciones de Dirichlet","Solución numérica", "Solución exacta","Solucion_cali1.png" )
grafica0 = fun.grafica_solucion(x,a0,"Calibración 1: Condiciones de Dirichlet","Solución exacta", "Solución exacta","Solucion_cali1.png" )