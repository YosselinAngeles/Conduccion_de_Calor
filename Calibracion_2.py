
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
q = np.ones(N) * s
b = fun.Vector_aux(N,Ta,Tb,-1*q)

#Llamando a la función creación de matriz
A = fun.creacion_matriz_diagonal(N,-2)

# Llamar a la función solución del sistema
u = fun.sol_sistema(A, b, N)

# Ingresando las condiciones de frontera

# ---- Programa 1 -------
# Condiciones de Dirichlet  con Ta y Tb en las fronteras
# u[0]=Ta
# u[n]=Tb
u[0] = Ta
u[-1] = Tb

#Solución analitica para un medio estacionario sin fuente o sumidero q=0
a1 = fun.sol_analitica(Ta,Tb,x,N,largo)


# ---- Calibración ----- 




# --- Calibración 2 -----
# Condiciones de Neuman
# du/dn = 0
# u(1) = 3
A1 = fun.creacion_matriz_diagonal(N,-2) #Siatema matricial para ec. de Poisson 1D
f = np.zeros(N)   
f = h*h*np.exp(x[1:N+1])         # Lado derecho (columana de 1 y 0)

f[0] += h*Ta    # Neumman
f[N-1] -= Tb
A1[0,0] = -1; A1[0,1] = 1; # Ajuste de la matriz debido a Neumman

u1 = fun.sol_sistema(A1,f,N)

u1[0]= -h*Ta + u1[1] # Condicion de frontera de Neumman
u1[-1] = Tb 

# Solución análitica
a2=fun.sol_analitica_cali2(x,N)

# Error entre la solución numerica y la exacta
Error1 = np.sqrt(h) * np.linalg.norm(fun.sol_analitica_cali2(x,N) - u1)
print(" Error calibración 2 = %12.10g " % Error1)



# Llamada de la función para Gráficar


grafica1 = fun.grafica_solucion(x,u1,a2,"Calibración 2: Condiciones de Neumman","Solución numérica", "Solución exacta","Solucion_cali2.png" )
# Llamado a la funcion de escritura
#Problema 1
archivo = fun.escritura(largo,Ta,Tb,N)
#Calibración 1

#Calibración 2
