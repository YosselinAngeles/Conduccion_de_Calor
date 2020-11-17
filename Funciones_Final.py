# PROGRAMA QUE CONTIENE LAS FUNCIONES PARA EL CÁLCULO DE LA SOLUCIÓN
# DE LA ECUACIÓN DE CALOR

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
    S : float
        Valor de la fuente
    k : float
        Valor de la conductividad térmica
        

    """
    if sel == 1:
        val= np.loadtxt("Datos_Caso1.txt")
        a = val[0]
        b = val[1]
        N = int(val[2])
        Ta = val[3]
        Tb = val[4]
        k = val[5]
        S = val[6]
        f = val[7]
        return a,b,N,Ta,Tb,k,S,f
    else:    
        # Datos de entrada
        a = float(input("Ingrese el comienzo de la barra.                a="))
        b = float(input("Ingrese el fin de la barra.                     b="))
        N = int(input("Ingresa el número de nodos que desea            N="))
        Ta = float(input("Ingrese la temperaruta al inicio.               Ta="))
        Tb = float(input("Ingrese la temperaruta al final.                Tb="))
        k = float(input("Ingrese la conductividad térmica.               k="))
        S = float(input("Ingrese las funetes o sumideros.                S="))
        f = float(input("Ingrese el valor de f:                          f="))
        return a,b,N,Ta,Tb,k,S,f

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

def Vector_aux(Ta,Tb,N,q):
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
    q : float
        Vector con la información de las fuentes
    Returns
    -------
    b : float
        Vector con las condiciones a la frontera

    """
    b = np.zeros(N)
    b[0] = -Ta
    b[-1] = -Tb
    return b + q

def Vector_aux_Neumman(Ta,Tb,N,f,k,a,b):
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
    q : float
        Vector con la información de las fuentes
    Returns
    -------
    b : float
        Vector con las condiciones a la frontera

    """
    h = (b-a)/(N+1)
    x = np.linspace(a,b,N+1)
    q = np.ones(N+1)*f*(h**2)/k
    for i in range(N+1):
        q[i] += np.exp(x[i])
    b = np.zeros(N+1)
    b[0] = -Ta
    b[-1] = -h*Tb
    return -q+b

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

def Matriz_Diagonal1(N,diagonal,f0,h,r):
    """
    Esta funcion crea una matriz cuadrada de tamaño N y
    cambia los valores de la diagonal, ayudando así a la
    resolución de la ecuación de Poison 1D por condiciones 
    de Dirichelet (Calibración 1)
    
    Parameters
    ----------
    N : Entero (int)
        Número de nodos.

    Returns
    -------
    A : Real(float)
        Matriz(N,N).

    """
    A = np.zeros((N,N))
    i=N
    A[0,0] =((diagonal)+((f0**2)*(h**2))); A[0,1] =1
    for i in range(1,N-1):
        A[i,i] = ((diagonal)+((f0**2)*(h**2)))
        A[i,i+1] =1
        A[i,i-1] = 1
    A[N-1,N-2] =1; A[N-1,N-1] =((diagonal)+((f0**2)*(h**2)))
    return A

def Matriz_Neumman(N,cons):
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
    A = np.zeros((N+1,N+1))

    A[0,0] = cons; A[0,1] = 1
    for i in range(1,N):
        A[i,i] = cons
        A[i,i+1] = 1
        A[i,i-1] = 1
    A[N,N-1] = 1; A[N,N] = cons
    return A

def Matriz_Diago3(N,diagonal,h,K):
    """
    Esta funcion crea una matriz cuadrada de tamaño N y
    cambia los valores de la diagonal, ayudando así a la
    resolución de la ecuación de Poison 1D por condiciones 
    de Dirichelet (Calibración 1)
    
    Parameters
    ----------
    N : Entero (int)
        Número de nodos.
    k : float
        Valor de la conductividad térmica
    h : float
        Distancia entre cada nodo

    Returns
    -------
    A : Real(float)
        Matriz(N,N).

    """
    A=np.zeros((N,N),dtype=np.float64)
    
    i=2
    A[0,0] =(diagonal*(((K[i+1]+K[i])/2.+(K[i-1]+K[i])/2.))); A[0,1] = (1.*((K[i+1])+K[i])/2.)
    for i in range(1,N-1):
        A[i,i] = (diagonal*(((K[i+1]+K[i])/2.+(K[i-1]+K[i])/2.)))
        A[i,i+1] = (1.*(K[i+1]+K[i])/2.)
        A[i,i-1] = (1.*(K[i-1]+K[i])/2.)
    A[N-1,N-2] = (1.*(K[i-1]+K[i])/2.); A[N-1,N-1] = (diagonal*(((K[i+1]+K[i])/2.+(K[i-1]+K[i])/2.)))
    
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
    
def Graficas_Cali3(x,u,u_exa):
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
    ax1.plot(x, u, '-bo', label = 'Conductividad')
    ax1.set_title('Conductividad Térmica')
    ax1.set(xlabel = 'Dominio [m]', ylabel = 'C.T.[k]')
    ax1.grid()
    ax1.legend()
    
    ax2.plot(x, u_exa, '-ro', label = 'Solución numérica')
    ax2.grid()
    ax2.set_title('Conductividad Constante')
    ax2.set(xlabel = 'Dominio [m]', ylabel = 'C.T.[k]')
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

def Sol_Analitica_F(a, b, Ta, Tb, S, k, N):
    """
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
    S : float
        Valor de la fuente
    k : float
        Valor de la conductividad térmica
        
    Returns
    -------
    sol : float
        Vector que contine la solución analica del problema
    """
    x = np.linspace(a,b,N+2)
    m = (Tb-Ta)/(b-a)
    sol = np.zeros(N+2)
    for i in range(N+2):
        aux = x[i]
        sol[i] = (m + (S/(2*k))*((b-a)-aux))*aux + Ta        
    return sol

     
def Sol_Analitica_Cali1(x,N,b,h):  
    """
    Esta función genera la solución analítica para la calibración
    tipo 1.
    """

    f=np.pi/2
      
    return ((1-np.cos(f)/np.sin(f))*np.sin(f*x))+b*(np.cos(f*x))
       
def Sol_Analitica_Neumman(x,Ta,Tb):
    """
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    Ta : float
        Temperatura en la frontera del inicio.
    Tb : float
        Temperatura en la frontera del final.

    Returns
    -------
    sol : TYPE
        DESCRIPTION.

    """
    sol =  np.exp(x) - x - np.exp(1) + 4
    sol[0] = Ta
    sol[-1] = Tb
    return sol

def Error(u,u_exa,N):
    """
    Esta función genera un vector que contiene la diferencia entre los 
    valores de las soluciones y devuelve la suma de este.    

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
    """
    Esta función genera un archivo .txt de dos columnas con los datos de
    las soluciones numérica y analítica
    Parameters
    ----------
    u : float
        Vector que contiene la solución numérica del problema
    u_exa : float
        Vector que contiene la solución analítica del problema

    Returns
    -------
    None.
    """
    
    serie1 = ps.Series(u)
    serie2 = ps.Series(u_exa)
    tabla = ps.DataFrame(serie1,columns = ['Solución analítica'])
    tabla['Solución numérica'] = serie2
    np.savetxt('Solución1.txt',tabla,fmt='%f', header = 'Soluciones del problema')
    
    
