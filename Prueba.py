import numpy as np
import matplotlib.pyplot as plt

print()
print("+----------------------------------------------------+")
print("|      Solucion de la transferencia de calor         |")
print("+----------------------------------------------------+")
print("| Autores: Hernández Terán Oscar                     |")
print("|          Ángeles Yosselin                          |")
print("|          García Andrés                             |")
print("+----------------------------------------------------+")
print("|                 Datos de entrada                   |")
print("+----------------------------------------------------+")


# Datos de entrada
a = float(input("Ingrese el comienzo de la barra.                a="))
b = float(input("Ingrese el fin de la barra.                     b="))
K = float(input("Ingresa la conductividad térmica del material   k="))
N = int(input("Ingresa el número de nodos que desea            N="))
Ta = float(input("Ingrese la temperaruta al inicio.               Ta="))
Tb = float(input("Ingrese la temperaruta al final.                Tb="))

# Calculo de constantes necesarias
h = (b-a)/(N+1)
r = K/(h**2)
x = np.linspace(a,b,N+2)

# Impresion de las constantes 
print("-------------------------------")
print("El ancho de la malla es: ",h)
print("La constante r es:       ",r)
print("-------------------------------")


# Funcion para la creacion de los arreglos
def Arreglos(N,Ta,Tb):
    A = np.zeros((N,N))
    T = np.zeros(N)    
    b = np.zeros(N)
    b[0] = -Ta
    b[-1] = -Tb
    return A, T, b

# Llamado a la funcion
A, T, b = Arreglos(N,Ta,Tb)

# Llenado de la matriz 
A = np.zeros((N, N))
diagonal=-2
A[0,0] = diagonal; A[0,1] = 1
for i in range(1,N-1):
     A[i,i] = diagonal
     A[i,i+1] = 1
     A[i,i-1] = 1
A[N-1,N-2] = 1; A[N-1,N-1] = diagonal

# Vector solucion
u = np.zeros(N+2)

# Solucion del sistema
u[1:-1] = np.linalg.solve(A,b)

# Ingresando las condiciones de frontera
u[0] = Ta
u[-1] = Tb

print("\n Matriz del sistema : \n", A)
print("\n Lado derecho del sistema : \n", b)
print("\n Vector resultado: \n", u)


# Graficando las soluciones
plt.plot(x,u,'-bo')
plt.title("Solucion a la ecuacion de calor")
plt.xlabel("Distancia [m]")
plt.ylabel("Temperatura [C]")
plt.grid()
plt.show()








