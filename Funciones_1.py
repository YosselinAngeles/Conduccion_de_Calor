#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:24:13 2020

@author: yosselin
"""

import numpy as np
import matplotlib.pyplot as plt

def Vector_aux(N,Ta,Tb):
    """
    Esta funcion genera un vector auxiliar, y se asignan los valores
    a la frontera.
    
    Parameters
    ----------
    N : Entero (int)
        Numero de nodos.
    Ta : Real (float)
        Temperatura al inicio.
    Tb : Real (float)
        Temperatura al final.
    Returns  
    -------
    Variables de salida:
                - Arreglo b
    """  
    b = np.zeros(N)
    b[0] = Ta
    b[-1] = Tb
    return b 
# -------------------------------------------------

def creacion_matriz_diagonal1(N,diagonal,f0,h,r):
    """
    Esta funcion crea una matriz cuadrada de tamaño N y
    cambia los valores de la diagonal, ayudando así a la
    resolución de la ecuación de Poison 1D por condiciones 
    de Dirichelet (Calibración 1)
    
    Parameters
    ----------
    N : Entero (int)
        Número de nodos.

    Returns
    -------
    A : Real(float)
        Matriz(N,N).

    """
    A = np.zeros((N,N))
    i=N
    A[0,0] =((diagonal)+((f0)*(h**2))); A[0,1] =1
    for i in range(1,N-1):
        A[i,i] = ((diagonal)+((f0)*(h**2)))
        A[i,i+1] =1
        A[i,i-1] = 1
    A[N-1,N-2] =1; A[N-1,N-1] =((diagonal)+((f0)*(h**2)))
    return A
#--------------------------------

# Solucion del sistema
def sol_sistema(A,b,N):
    """
    Esta funcion resuelve la ecuacion matricial y guarda los valores
    en el vector solucion
    
    Parameters
    ----------
    A : Real(float)
        Matriz cuadrada de tamaño N, con la diagonal editada.
    b : Real(float)
        Vector auxiliar de tamaño N, con las condiciones en la frontera.
    Returns
    -------
    u : Real(float)
        Vector solución del problema.
    """
    
    
    u = vector_sol(N)
    u[1:-1] = np.linalg.solve(A,b)
    return u

# -------------------------------------------------
# Vector solucion
def vector_sol(N):
    """
    Esta funcion genera un vector de tamaño N+2 que contendrá 
    las soluciones y sus condiciones de frontera
                                                
    Parameters
    ----------
    N : Entera (int)
        Número de nodos.
    Returns
    -------
    u : Real (float)
        arreglo solución.
    """
    u = np.zeros(N+2)
    return u
# --------------------------------------------------



#Solución exacta de problema

def sol_analitica_cali1(x,N,b,h):  

    f=np.pi
      
    return ((1-np.cos(f)/np.sin(f))*np.sin(f*x))+b*(np.cos(f*x))

#---------------------------------------------------
# Graficando las soluciones
def grafica_solucion(x,u,a,Gtitle,Ntitle,Etitle,filename):
    """
    Esta función genera las gráficas de la solución del problema.
    Parameters
    ----------
    x : Real(float)
        Vector que corresponde a las distancias de la barra.
    u : Real(float)
        Vector solución del problema.
    Gtitle: string 
             Nombre del grafico.
    Ntitle: string
                Etiqueta para la solución aproximacimada.
    Etitle: string
                Etiqueta para la solución exacta. 
    filename: string
                Nombre de la imagen para ser almacenada.
    Returns
    -------
    None.
    """
    plt.plot(x,u,'o',color='gray',label=Ntitle)
    plt.plot(x,a,'--',color='black',label=Etitle)
    plt.title(Gtitle)
    plt.xlabel("Distancia [m]")
    plt.ylabel("Temperatura [°C]")
    plt.grid(linestyle='--',linewidth=0.8)
    plt.legend()
    plt.savefig(filename)
    plt.show()
    return()
# ---------------------------------------------------
# Función de lectura
#def lectura(archivo):
 #   datos=[]

  #  with open("ModeloConRuido.dat") as mcr:
   #     for linea in mcr:
    #        datos.append(linea.split())

 #       n=np.shape(datos)
  #      datosf=np.zeros((n[0]-2,n[1]),dtype=np.float32)

   # for i in range(n[0]-2):
    #    for j in range(n[1]):
     #       datosf[i,j]=float(datos[i+1][j])

    #for i in range(n[0]-2):
     #   datosf[i,3]=(float(datos[i][3])+float(datos[i+1][3])+float(datos[i+2][3]))/3.


# ---------------------------------------------------
# Funcion de escritura de los datos
def escritura(largo,Ta,Tb,N):
    """
    

    Parameters
    ----------
    largo : Entero (int)
        Tamaño de la barra.
    Ta : entero (int)
        Temperatura.
    Tb : Entero (int)
        Temperatura.
    N : Entero (int)
        Numero de nodos.

    Archivo de salida .txt
    -------
    None.

    """
    f = open("Archivo.txt", "w", encoding="utf8")
    f.write("--------------------------------------")
    f.write("ARCHIVO GENERADO CON LAS SOLUCIONES DE LA ECUACION DE CALOR")
    f.write("--------------------------------------\n")
    f.write("Longitud de la barra: " + str(largo) + "\n")
    f.write("Temperatura en los extremos: " + str(Ta) +  " y " + str(Tb) +  "\n")
    f.write("El numero de nodos es: " +  str(N) + "\n")
    f.write("Los resultados son los siguentes: \n")
    f.close()
