# PROGRAMA PARA LA RESOLUCIÓN DE LA ECUACIÓN DE CALOR CON CONDICIONES DE 
# TIPO NEUMMAN

import numpy as np
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

a,b,N,Ta,Tb,k,S,f = fun.Ingreso(sel)

# Cálculo de Constantes
h,x,largo = fun.Constantes(a,b,N+1)
print("\n---------------------------------------------------")
print("El ancho de la malla es: ",h)
print("El largo de la barra es: ",largo)
print("---------------------------------------------------\n")


# Creación de vector b
B = fun.Vector_aux_Neumman(Ta,Tb,N,f,k,a,b)

# Creación de matriz diagonal
A = fun.Matriz_Neumman(N,-2)

# Solucion del sistema
u = fun.Sol_Sitema(A,B,N+1,Ta,Tb)

# Solución analítica del problema
u_exa = fun.Sol_Analitica_Neumman(x,Ta,Tb)
print(u_exa)

error = fun.Error(u,u_exa,N)

print("\n--------------------------------------------")
print("El vector b es: ",B)
print("La matriz A es: \n",A)
print("La solución numérica es: \n",u)
print("La solución analítica es: \n",u_exa)
print("El error en la solución es: \n",error)
print("\n--------------------------------------------\n")

# Graficando la solucion
fun.Graficas(x,u,u_exa)

# Guardando los datos
fun.Escritura(u,u_exa)
