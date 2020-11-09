import Funciones as fun
import numpy as np
import matplotlib.pyplot as plt


# Programa principal.
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

def Evalua(x):
    return np.exp(x) - x - np.exp(1) + 4

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
#b = fun.Vector_aux(N,Ta,Tb)

#Llamando a la función creación de matriz
A = fun.creacion_matriz(N)
b = np.zeros(N)             
b = (1/r)*np.exp(x[1:N+1])         # Lado derecho

# Ingresando las condiciones de frontera
b[0] -= Ta    # Neumman
b[N-1] += h*Tb  # Dirichlet
A[-1,-1] = -1; A[0,1] = 1; # Ajuste de la matriz debido a Neumman

# Llamar a la función solución del sistema
u = fun.sol_sistema(A, b, N)

# Modificando condiciones de frontera
u[0] = Ta # Condicion de frontera dirichlet
u[-1] = -h*Tb + u[N] # Condicion de frontera de Neumman



# Impresion de los vectores y matrices
print("\n Matriz del sistema : \n", A)
print("\n Lado derecho del sistema : \n", b)
print("\n Vector solucion:")
for i in range(len(u)):
    print(u[i])

# Calcula el error con respecto a la solucion analitica

Error = np.sqrt(h) * np.linalg.norm(Evalua(x) - u)
print(" Error = %12.10g " % Error)

#Solución Analítica

ua = Evalua(x)

# Llamada de la función para Gráficar
grafica = fun.grafica_solucion(x, u,ua,"Calibración 2, Transferencia de Calor","Solución numérica", "Solución exacta","Solucion.png" )

# Llamada de la función para Gráficar
#grafica = fun.grafica_solucion(x, ua)
#plt.savefig("Solucion.png")

