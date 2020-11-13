# PROGRAMA PARA LA RESOLUCIÓN DE LA ECUACIÓN DE CALOR SIN FUENTES O SUMIDEROS

import Funciones_Sin_Fuente as fun

# Programa principal
print()
print("+----------------------------------------------------+")
print("|      Solucion de la transferencia de calor         |")
print("+----------------------------------------------------+")

print('Opciones para la ejecución: \n'
	  '1.- Tomar datos de ejemplo de un archivo \n'
      '2.- Ingresar los datos manualmente.')

sel = int(input('Escoja una opción.\n'))

if sel == 1:
    val= fun.Lectura("Datos_Caso1.txt")
    a = val[0]
    b = val[1]
    N = int(val[2])
    Ta = val[3]
    Tb = val[4]
else:    
    # Datos de entrada
    a = float(input("Ingrese el comienzo de la barra.                a="))
    b = float(input("Ingrese el fin de la barra.                     b="))
    N = int(input("Ingresa el número de nodos que desea            N="))
    Ta = float(input("Ingrese la temperaruta al inicio.               Ta="))
    Tb = float(input("Ingrese la temperaruta al final.                Tb="))

# Cálculo de Constantes
h,x,lar = fun.Constantes(a,b,N)
print("\n-------------------------------------------------")
print("El ancho de la malla es: ",h)
print("El largo de la barra es: ",lar)
print("---------------------------------------------------\n")

# Creación de vector b
b = fun.Vector_aux(Ta,Tb,N)

# Creación de matriz diagonal
A = fun.Matriz_Diagonal(N,-2)

# Solucion del sistema
u = fun.Sol_Sitema(A,b,N,Ta,Tb)

# Solución analítica del problema
u_exa = fun.Sol_Analitica(Ta,Tb,N,lar)

error = fun.Error(u,u_exa)

print("\n--------------------------------------------")
print("El vector b es: ",b)
print("La matriz A es: \n",A)
print("La solución numérica es: ",u)
print("La solución analítica es: ",u_exa)
print("El error en la solución es: ",error)
print("\n--------------------------------------------\n")

#Graficando la solucion
fun.Graficas(x,u,u_exa)

