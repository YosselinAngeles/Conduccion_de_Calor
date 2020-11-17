import Funciones_2_Tipo_IV as fun
import numpy as np
import Funciones_Final as Fun

# Programa principal
print()
print("+----------------------------------------------------+")
print("|      Solucion de la transferencia de calor         |")
print("+----------------------------------------------------+")

print('Opciones para la ejecución: \n'
	  '1.- Tomar datos de ejemplo de un archivo \n'
      '2.- Ingresar los datos manualmente.')

sel = int(input('Escoja una opción.\n'))

a,b,N,Ta,Tb,k,S,f = Fun.Ingreso(sel)

# Cálculo de Constantes
h,x,largo = Fun.Constantes(a,b,N)
x = np.linspace(a,b,N+3)
print("\n-------------------------------------------------")
print("El ancho de la malla es: ",h)
print("El largo de la barra es: ",largo)
print("---------------------------------------------------\n")

A = Fun.Matriz_Diagonal2(N,-2) 
A[0,0]=-1; A[0,1]=1  
g=len(A)
l=len(A[0])




f = np.zeros(N+1)   
f = h*h*np.exp(x[1:N+2])         # Lado derecho (columana de 1 y 0)

f[0] += -h*Ta   # Neumman
f[N] -= Tb

print("La matriz del sistem es: ", A)
u = Fun.sol_sistema(A,f,N)

C=len(x)
u[0] = -h*Ta + u[1]# Condicion de frontera de Neumman
u[N+2] = Tb


# Solución análitica
u_exa = Fun.sol_analitica_cali2(x,N+1)


# Error entre la solución numerica y la exacta
Error1 = np.sqrt(h) * np.linalg.norm(Fun.sol_analitica_cali2(x,N) - u)
print(" Error calibración 2 = %12.10g " % Error1)

Fun.Graficas(x,u,u_exa,'ECUACIÓN DE CALOR. CALIBRACIÓN 2 TIPO IV')



