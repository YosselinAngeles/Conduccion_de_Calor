

import numpy as np
import matplotlib.pyplot as plt

print()
print("+----------------------------------------------------+")
print("|      Solucion de la transferencia de calor         |")
print("+----------------------------------------------------+")
<<<<<<< 732325926b47ff0b0285de687fa5ef8223627b5b


=======
>>>>>>> Agregar programa principal y programa de modulos

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
print("\n-------------------------------------------------")
print("El ancho de la malla es: ",h)
print("La constante r es:       ",r)
print("---------------------------------------------------\n")

# ------------------------------------------------------------
# ------------------------------------------------------------

# Funcion para la creacion de los arreglos
def Arreglos(N,Ta,Tb):
    """

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
                - Arreglo A
                - Arreglo b
                - Vector T

    """
    A = np.zeros((N,N))
    T = np.zeros(N)    
    b = np.zeros(N)
    b[0] = -Ta
    b[-1] = -Tb
    return A, T, b

A, T, b = Arreglos(N,Ta,Tb)

<<<<<<< 732325926b47ff0b0285de687fa5ef8223627b5b
=======

>>>>>>> Agregar programa principal y programa de modulos
# -------------------------------------------------
# -------------------------------------------------

# Llenado de la matriz 
def creacion_matriz(N):
    """
    

    Parameters
    ----------
    N : Entero (int)
        Número de nodos.

    Returns
    -------
    A : Real(float)
        Matriz(N,N).

    """
    A = np.zeros((N, N))
    diagonal=-2
    A[0,0] = diagonal; A[0,1] = 1
    for i in range(1,N-1):
        A[i,i] = diagonal
        A[i,i+1] = 1
        A[i,i-1] = 1
    A[N-1,N-2] = 1; A[N-1,N-1] = diagonal
    return A
<<<<<<< 732325926b47ff0b0285de687fa5ef8223627b5b
#Llamando a la función creación de matriz
A = creacion_matriz(N)

=======

#Llamando a la función creación de matriz
A = creacion_matriz(N)
>>>>>>> Agregar programa principal y programa de modulos
# -------------------------------------------------
# -------------------------------------------------

# Vector solucion
def vector_sol(N):
    """
    

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
<<<<<<< 732325926b47ff0b0285de687fa5ef8223627b5b
#Lamada de la función vector_sol
u = vector_sol(N)

=======

#Lamada de la función vector_sol

u = vector_sol(N)
>>>>>>> Agregar programa principal y programa de modulos
# --------------------------------------------------
# --------------------------------------------------

# Solucion del sistema
def sol_sistema(A,b):
    """
    

<<<<<<< 732325926b47ff0b0285de687fa5ef8223627b5b

# --------------------------------------------------
# --------------------------------------------------1

# Ingresando las condiciones de frontera
u[0] = Ta
u[-1] = Tb
=======
    Parameters
    ----------
    A : Reasl float
        Arreglo matricial (N,N).
    b : REAL
        Arreglo.
>>>>>>> Agregar programa principal y programa de modulos

    Returns
    -------
    u : Real
        Solución del sistema.

    """
    u[1:-1] = np.linalg.solve(A,b)
    return u

<<<<<<< 732325926b47ff0b0285de687fa5ef8223627b5b
# Graficando las soluciones
plt.plot(x,u,'o')
plt.title("Solucion a la ecuacion de calor")
plt.xlabel("Distancia [m]")
plt.ylabel("Temperatura [C]")
plt.grid()
plt.show()
=======

# --------------------------------------------------
# --------------------------------------------------
>>>>>>> Agregar programa principal y programa de modulos


#---------------------------------------------------
#---------------------------------------------------


# Graficando las soluciones
def grafica_solucion(x,u):
    
    plt.plot(x,u,'C3-o')
    plt.title("Solucion a la ecuacion de calor")
    plt.xlabel("Distancia [m]")
    plt.ylabel("Temperatura [C]")
    plt.grid(linestyle='--',linewidth=0.8)
    plt.show()
    return()


# ---------------------------------------------------





