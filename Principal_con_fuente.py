
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
s = float(input("Ingrese la fuente o sumidero.                s="))

# Calculo de constantes necesarias
h = (b-a)/(N+1)
r = K/(h**2)
x = np.linspace(a,b,N+2)
largo = b-a
#g=len(x)
#print("Tamaño x",x)
# Impresion de las constantes 
print("\n-------------------------------------------------")
print("El ancho de la malla es: ",h)
print("La constante r es:       ",r)
print("El largo de la barra es: ",largo)
print("---------------------------------------------------\n")

# Llamado a funcion para crear arreglos
q = np.ones(N) * (-s*h**2/K)
b = fun.Vector_aux(N,Ta,Tb,q)

#Llamando a la función creación de matriz
A = fun.creacion_matriz_diagonal(N,-2)

# Llamar a la función solución del sistema
u = fun.sol_sistema(A, b, N)

# Ingresando las condiciones de frontera

# ---- Programa 2. Con Fuente o Sumidero -------
# Condiciones de Dirichlet  con Ta y Tb en las fronteras

u[0] += Ta
u[-1] += Tb

#Solución analitica para un medio estacionario sin fuente o sumidero q=0
#a1 = fun.sol_analitica(Ta,Tb,x,N,largo)

a1= fun.temperatura(x, Ta, Tb, s, largo, K, N)

grafica2 = fun.grafica_solucion(x, u, a1,"Solución de la Ecuación de Calor","Solución numérica", "Solución exacta","Solucion.png" )

