# PROGRAMA PARA LA RESOLUCIÓN DE LA ECUACIÓN DE CALOR CON FUENTES O SUMIDEROS

import numpy as np
import matplotlib.pyplot as plt
import Funciones_Final as fun

# Programa principal
print()
print("+----------------------------------------------------+")
print("|      Solucion de la transferencia de calor         |")
print("+----------------------------------------------------+")

print('Opciones para la ejecución: \n'
	  '1.- Tomar datos de ejemplo de un archivo \n'
      '2.- Ingresar los datos manualmente.')

sel = int(input('Escoja una opción.\n'))

a,b,N,Ta,Tb,k,S = fun.Ingreso(sel,"Datos_Caso1.txt")

# Cálculo de Constantes
h,x,largo = fun.Constantes(a,b,N)
print("\n-------------------------------------------------")
print("El ancho de la malla es: ",h)
print("El largo de la barra es: ",largo)
print("---------------------------------------------------\n")

# Vector que contiene las fuentes
q = np.ones(N) * (-S*h**2/k)
# Creación de vector b
B = fun.Vector_aux(Ta,Tb,N,q)

# Creación de matriz diagonal
A = fun.Matriz_Diagonal(N,-2)

# Solucion del sistema
u = fun.Sol_Sitema(A,B,N,Ta,Tb)

# Solución analítica del problema
u_exa = fun.Sol_Analitica_F(a, b, Ta, Tb, S, k, N)

error = fun.Error(u,u_exa,N)

print("\n--------------------------------------------")
print("El vector b es: ",B)
print("La matriz A es: \n",A)
print("La solución numérica es: \n",u)
print("La solución analítica es: \n",u_exa)
print("El error en la solución es: \n",error)
print("\n--------------------------------------------\n")

# Graficando la solucion
fun.Graficas(x,u,u_exa,'ECUACIÓN DE CALOR CON FUENTES.')

# Guardando los datos
fun.Escritura(u,u_exa,)


