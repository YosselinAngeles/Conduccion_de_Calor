# PROGRAMA QUE CONTIENE LAS FUNCIONES PARA EL CÁLCULO DE LA SOLUCIÓN
# DE LA ECUACIÓN DE Calor

import numpy as np
import matplotlib.pyplot as plt
import pandas as ps
plt.style.use('seaborn-dark')

def Ingreso(sel):
    """
    Esta función permite seleccionar al usuario la manera 
    en la que se ingresarán los datos

    Parameters
    ----------
    sel : Integer
        Valor de selección ingresado por el usuario

    Returns
    -------
    a : float
        Valor al inicio del dominio.
    b : float
        Valor al final del dominio.
    N : Integer
        Número de nodos
    Ta : float
        Temperatura en la frontera del inicio.
    Tb : float
        Temperatura en la frontera del final.

    """
    if sel == 1:
        val= np.loadtxt("Datos_Caso1.txt")
        a = val[0]
        b = val[1]
        N = int(val[2])
        Ta = val[3]
        Tb = val[4]
        return a,b,N,Ta,Tb
    else:    
        # Datos de entrada
        a = float(input("Ingrese el comienzo de la barra.                a="))
        b = float(input("Ingrese el fin de la barra.                     b="))
        N = int(input("Ingresa el número de nodos que desea            N="))
        Ta = float(input("Ingrese la temperaruta al inicio.               Ta="))
        Tb = float(input("Ingrese la temperaruta al final.                Tb="))
        return a,b,N,Ta,Tb

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
    Esta función resuelve el sistema matricial para el problema

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
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.suptitle('SOLUCIONES DEL PROBLEMA')
    ax1.plot(x, u, '-bo', label = 'Solución')
    ax1.set_title('Solución numérica')
    ax1.set(xlabel = 'Dominio [m]', ylabel = 'Temperatura [C]')
    ax1.grid()
    ax1.legend()
    
    ax2.plot(x, u_exa, '-ro', label = 'Solución')
    ax2.grid()
    ax2.set_title('Solución analítica')
    ax2.set(xlabel = 'Dominio [m]', ylabel = 'Temperatura [C]')
    ax2.legend()
    plt.show()
    
def Sol_Analitica(a,b,Ta,Tb,N):  
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
    x = np.linspace(a,b,N+2)
    m = (Tb-Ta)/(b-a)
    sol = np.zeros(N+2)
    for i in range(N+2):
        aux = x[i]
        sol[i] = m*(aux-a) + Ta
    return sol

def Error(u,u_exa,N):
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
    error = np.zeros(N+2)
    for i in range(N+2):
        error[i] = u[i] - u_exa[i]
    return sum(error)
    
def Escritura(u,u_exa):
    serie1 = ps.Series(u)
    serie2 = ps.Series(u_exa)
    tabla = ps.DataFrame(serie1,columns = ['Solución analítica'])
    tabla['Solución numérica'] = serie2
    np.savetxt('Solución1.txt',tabla,fmt='%f', header = 'Soluciones del problema')
    
    
