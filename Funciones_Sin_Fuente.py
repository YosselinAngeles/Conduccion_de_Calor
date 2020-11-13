# PROGRAMA QUE CONTIENE LAS FUNCIONES PARA EL CÁLCULO DE LA SOLUCIÓN
# DE LA ECUACIÓN DE Calor

import numpy as np
import matplotlib.pyplot as plt

def Lectura(Nombre):
    """
    Esta función permite leer los datos necesarios para el programa
    a partir de un archivo .txt sin encabezado.

    Parameters
    ----------
    Nombre : String
        Nombre con ruta(si aplica) del archivo,

    Returns
    -------
    val : Vector float
        Vector que contiene los valores de los datos

    """
    val = np.loadtxt(Nombre)
    return val

def Constantes(a,b,N):
    """
    Esta función calcula las constantes que requiere el programa

    Parameters
    ----------
    a : float
        Valor al inicio del dominio.
    b : float
        Valor al final del dominio.
    N : Integer
        Número de nodos

    Returns
    -------
    h : float
        Distancia entre cada nodo
    x : float
        Vector con el cual se graficará
    lar : float
        Distancia total del dominio

    """
    h = (b-a)/(N+1)
    x = np.linspace(a,b,N+2)
    lar = b-a
    return h,x,lar

def Vector_aux(Ta,Tb,N):
    """
    Esta función genera un vector el cual se utiliza en la resolución del 
    problema.

    Parameters
    ----------
    Ta : float
        Temperatura en la frontera del inicio.
    Tb : float
        Temperatura en la frontera del final.
    N : Integer
        Número de nodos.

    Returns
    -------
    b : float
        Vector con las condiciones a la frontera

    """
    b = np.zeros(N)
    b[0] = -Ta
    b[-1] = -Tb
    return b

def Matriz_Diagonal(N,cons):
    """
    Esta función genera la matriz diagonal necesaria en la resolución del 
    problema.    

    Parameters
    ----------
    N : Integer
        Número de nodos.
    cons : Integer
        Valor en la diagonal

    Returns
    -------
    A : float
        Matriz diagonal

    """
    A = np.zeros((N,N))

    A[0,0] = cons; A[0,1] = 1
    for i in range(1,N-1):
        A[i,i] = cons
        A[i,i+1] = 1
        A[i,i-1] = 1
    A[N-1,N-2] = 1; A[N-1,N-1] = cons
    return A

def Sol_Sitema(A,b,N,Ta,Tb):
    """
    

    Parameters
    ----------
    A : float
        Matriz diagonal
    b : float
        Vector con las condiciones a la frontera
    N : Integer
        Número de nodos.
    Ta : float
        Temperatura en la frontera del inicio.
    Tb : float
        Temperatura en la frontera del final.

    Returns
    -------
    u : float
        Vector que contiene las soluciones del problema
    """
    u = np.zeros(N+2)
    u[1:-1] = np.linalg.solve(A,b)
    u[0] = Ta
    u[-1] = Tb
    return u

def Graficas(x,u,u_exa):
    """
    Esta función genera las gráficas de la solución analítica y numérica

    Parameters
    ----------
    x : float
        Vector con el cual se graficará
    u : float
        Vector que contiene la solución numérica del problema
    u_exa : float
        Vector que contiene la solución analítica del problema

    Returns
    -------
    None.

    """
    plt.plot(x,u,'-bo', label = 'Solución numérica')
    plt.plot(x,u_exa,'-.ro', label = 'Solución analítica')
    plt.xlabel('Dominio [m]')
    plt.ylabel('Temperatura [C]')
    plt.legend()
    plt.grid()
    plt.show()
    
def Sol_Analitica(Ta,Tb,N,largo):  
    """
    Esta funcion genera un vector que contiene la solución analítica
    del problema

    Parameters
    ----------
    Ta : float
        Temperatura en la frontera del inicio.
    Tb : float
        Temperatura en la frontera del final.
    x : float
        Vector con el cual se graficará
    N : Integer
        Número de nodos.
    largo : float
        Distancia total del dominio

    Returns
    -------
    a1 : TYPE
        DESCRIPTION.

    """
    x = np.linspace(0,1,N+2)
    a=[]
    for i in range(N+2):
        a.append(((Tb-Ta)/largo)*x[i]+Ta)
    return a

def Error(u,u_exa):
    """
    

    Parameters
    ----------
    u : float
        Vector que contiene la solución numérica del problema
    u_exa : float
        Vector que contiene la solución analítica del problema

    Returns
    -------
    error: float
        Diferencia entre los valores obtenidos numérica y analíticamente.

    """
    error = np.zeros(len(u))
    for i in range(len(u)):
        error[i] = u[i] - u_exa[i]
    return sum(error)
    
    

