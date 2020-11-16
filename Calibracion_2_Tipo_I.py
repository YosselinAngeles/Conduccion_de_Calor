
import Funciones_2_Tipo_I as fun
import numpy as np
import matplotlib.pyplot as plt

# Programa principal 
print()
print("+----------------------------------------------------+")
print("|      Solucion de la transferencia de calor         |")
print("+----------------------------------------------------+")


# Datos de entrada
#a = float(input("Ingrese el comienzo de la barra.                a="))
#b = float(input("Ingrese el fin de la barra.                     b="))
#K = float(input("Ingresa la conductividad térmica del material   k="))
#N = int(input("Ingresa el número de nodos que desea            N="))
#Ta = float(input("Ingrese la temperaruta al inicio.               Ta="))
#Tb = float(input("Ingrese la temperaruta al final.                Tb="))
#s = float(input("Ingrese la fuente o sumidero.                s="))

#----- Parametros de entrada ----
a=0  #Inicio de la barra
b=1  #Fin de la barra
K=1#Conductividad
N=6# Numero de nodos (lugares donde quiero saber la temperatura)
Ta=0 # Primera condicion de frontera (Temperatura en el primer nodo)
Tb=1 # Segunda condicion de frontera (Temperatura en el ultimo nodo)
#----- 

# Calculo de constantes necesarias
h = (b-a)/(N+1)
r = K/(h**2)
x = np.linspace(a,b,N+3)
largo = b-a
#g=len(x)
#print("Tamaño x",x)
# Impresion de las constantes 
print("\n-------------------------------------------------")
print("El ancho de la malla es: ",h)
print("La constante r es:       ",r)
print("El largo de la barra es: ",largo)
print("---------------------------------------------------\n")


# ---- Calibración ----- 

# --- Calibración 2 -----
# Condiciones de Neuman
# du/dn = 0
# u(1) = 3
A2 = fun.creacion_matriz_diagonal2(N,-2) #Siatema matricial para ec. de Poisson 1D
A2[N,N]=1
A2[N,N-1]=-1

print("La matriz del sistem es: ", A2)

f = np.zeros(N+1)   
f = h*h*np.exp(x[1:N+2])         # Lado derecho (columana de 1 y 0)

f[0] -= Ta    # Neumman
f[N-1] = -h*Tb
#A1[0,0] = -1; A1[0,1] = 1; # Ajuste de la matriz debido a Neumman

u2 = fun.sol_sistema(A2,f,N)

u2[0]= Ta # Condicion de frontera de Neumman
u2[-1] = Tb 

print("La solución del sistema es: ", u2)

# Solución análitica
a2=fun.sol_analitica_cali2(x,N+1)

print("La solución analítica es: ", a2)

# Error entre la solución numerica y la exacta
Error1 = np.sqrt(h) * np.linalg.norm(fun.sol_analitica_cali2(x,N) - u2)
print(" Error calibración 2 = %12.10g " % Error1)



# Llamada de la función para Gráficar


grafica1 = fun.grafica_solucion(x,u2,a2,"Calibración 2: Condiciones de Neumman","Solución numérica", "Solución exacta","Solucion_cali2.png" )

# Llamado a la funcion de escritura
archivo = fun.escritura(largo,Ta,Tb,N)


#Calibración 2

