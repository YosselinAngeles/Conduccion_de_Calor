import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# ------------------------------------------------------------
# Funcion para la creacion de los arreglos
def Vector_aux(N,Ta,Tb,q):
    """
    Esta funcion genera un vector auxiliar, y se asignan los valores
    a la frontera.
    
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
                - Arreglo b
    """  
    b = np.zeros(N)
    b[0] = -Ta
    b[-1] = -Tb
    return b + q

# -------------------------------------------------
#Solución exacta de problema

def sol_analitica(Ta,Tb,x,N,largo):  
    a1=[]
    for i in range(N+2):
        a1.append(((Tb-Ta)/largo)*x[i]+Ta)
          #a.append(((Tb-Ta)/largo)*x[i]+Ta)
    return a1

# -------------------------------------------------
#Solución exacta de problema

def sol_analitica_cali1(x,N,b,h):  
    for i in range(N+2):
        #f=h*(x[i]*np.pi)**2
        
        f=2.9
        i=i+1
    return ((1-np.cos(f)/np.sin(f))*np.sin(f*x))+b*(np.cos(f*x))
# ---------------------------------------------------
#Solución exacta de problema

def sol_analitica_cali2(x,N):         
    return np.exp(x) - x - (np.exp(1)) + 4.
# -------------------------------------------------
# -------------------------------------------------
# Llenado de la matriz 
def creacion_matriz_diagonal(N,diagonal):
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
    A = np.zeros((N, N))
   
    A[0,0] = diagonal; A[0,1] = 1
    for i in range(1,N-1):
        A[i,i] = diagonal
        A[i,i+1] = 1
        A[i,i-1] = 1
    A[N-1,N-2] = 1; A[N-1,N-1] = diagonal
    return A
# -------------------------------------------------

def creacion_matriz_diagonal1(N,diagonal,f0):
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
    A = np.zeros((N, N))
   
    A[0,0] = diagonal-f0[0]; A[0,1] = 1
    for i in range(1,N-1):
        A[i,i] = diagonal-f0[i]
        A[i,i+1] = 1
        A[i,i-1] = 1
    A[N-1,N-2] = 1; A[N-1,N-1] = diagonal-f0[N-1]
    return A



# -------------------------------------------------

# Llenado de la matriz 
def creacion_matriz(N,diagonal,x):
    """
    Esta funcion crea una matriz cuadrada de tamaño N y
    cambia los valores de la diagonal    
    
    Parameters
    ----------
    N : Entero (int)
        Número de nodos.
    Returns
    -------
    A : Real(float)
        Matriz(N,N).
    """
    k1=[]
    k2=[]
    for i in range(N):
        k1.append( np.abs(np.sin(4.*np.pi*((x[i+1]+x[i])/2)))) #derecha
        k2.append( np.abs(np.sin(4.*np.pi*((x[i-1]+x[i])/2)))) #izquierda
    print("k1 ",k1)
    print()
    print("k2",k2, end='\n')
    A = np.zeros((N, N))
    
    A[0,0] = diagonal ; A[0,1] = k1[0]
    for i in range(1,N-1):
        A[i,i] = diagonal
        A[i,i+1] = k1[i]
        A[i,i-1] = k2[i]
        A[N-1,N-2] = k2[i]
   #A[N,N] = k1[0]
    return A
# -------------------------------------------------
# -------------------------------------------------
# Vector solucion
def vector_sol(N):
    """
    Esta funcion genera un vector de tamaño N+2 que contendrá 
    las soluciones y sus condiciones de frontera
                                                
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
# --------------------------------------------------
# --------------------------------------------------
# Solucion del sistema
def sol_sistema(A,b,N):
    """
    Esta funcion resuelve la ecuacion matricial y guarda los valores
    en el vector solucion
    
    Parameters
    ----------
    A : Real(float)
        Matriz cuadrada de tamaño N, con la diagonal editada.
    b : Real(float)
        Vector auxiliar de tamaño N, con las condiciones en la frontera.
    Returns
    -------
    u : Real(float)
        Vector solución del problema.
    """
    u = vector_sol(N)
    u[1:-1] = np.linalg.solve(A,b)
    return u

#---------------------------------------------------
# Graficando las soluciones
def grafica_solucion(x,u,a1,Gtitle,Ntitle,Etitle,filename):
    """
    Esta función genera las gráficas de la solución del problema.
    Parameters
    ----------
    x : Real(float)
        Vector que corresponde a las distancias de la barra.
    u : Real(float)
        Vector solución del problema.
    Gtitle: string 
             Nombre del grafico.
    Ntitle: string
                Etiqueta para la solución aproximacimada.
    Etitle: string
                Etiqueta para la solución exacta. 
    filename: string
                Nombre de la imagen para ser almacenada.
    Returns
    -------
    None.
    """
    plt.plot(x,u,'o',label=Ntitle)
    plt.plot(x,a1,'--',label=Etitle)
    plt.title(Gtitle)
    plt.xlabel("Distancia [m]")
    plt.ylabel("Temperatura [°C]")
    plt.grid(linestyle='--',linewidth=0.8)
    plt.legend()
    plt.savefig(filename)
    plt.show()
    return()
# ---------------------------------------------------
# Función de lectura
#def lectura()
#datos=[]

#with open("ModeloConRuido.dat") as mcr:
 #   for linea in mcr:
  #      datos.append(linea.split())

#n=np.shape(datos)
#datosf=np.zeros((n[0]-2,n[1]),dtype=np.float32)

#for i in range(n[0]-2):
 #   for j in range(n[1]):
  #      datosf[i,j]=float(datos[i+1][j])

#for i in range(n[0]-2):
 #   datosf[i,3]=(float(datos[i][3])+float(datos[i+1][3])+float(datos[i+2][3]))/3.


# ---------------------------------------------------
# Funcion de escritura de los datos
def escritura(largo,Ta,Tb,N):
    f = open("Archivo.txt", "w", encoding="utf8")
    f.write("--------------------------------------")
    f.write("ARCHIVO GENERADO CON LAS SOLUCIONES DE LA ECUACION DE CALOR")
    f.write("--------------------------------------\n")
    f.write("Longitud de la barra: " + str(largo) + "\n")
    f.write("Temperatura en los extremos: " + str(Ta) +  " y " + str(Tb) +  "\n")
    f.write("El numero de nodos es: " +  str(N) + "\n")
    f.write("Los resultados son los siguentes: \n")
    f.close()
