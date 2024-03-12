'''1

def Mayor_tres(a,b,c):

    lista=[a,b,c]
    lista.sort(reverse=True)

    if lista[0] == lista[1]:
        return -1
    
    else: 
        return lista[0]
    


num1 = int(input("Ingresar primer numero: "))
num2 = int(input("Ingresar segundo numero: "))
num3 = int(input("Ingresar tercer numero: "))

mayor = Mayor_tres(num1, num2, num3)

if mayor == -1 :
    print("No existe un numero mayor unico")

else:
    print("El mayor de los tres numeros ingresados es: ", mayor)
'''



'''2

def Fecha_valida(dia, mes, año):

    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    val = False

    if mes<1 or mes>12:
        return False
    
    elif mes==2 and dia==29:
        for i in range(4, año+1, 4):
            if i==año:
                val=True
        
        if val==True:
            return True
        else:
            return False
        
    elif dia<1 or dia>meses[mes-1]:
        return False
    

    else: 
        return True 
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""

dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

valido = Fecha_valida(dia, mes, año)

if valido == True:
    print("Fecha valida")

else:
    print("Fecha invalida")

'''



'''3

def VueltoAEntregar(total, recibido):

    CantBilletes = [0, 0, 0, 0, 0, 0, 0]
    ValorBilletes= [500, 100, 50, 20, 10, 5, 1]

    if recibido<total:
        while(recibido<total):
            print("Error, dinero insuficiente")
            recibido = int(input("Ingrese valor actualizado:"))
    
    else:
        vuelto = recibido - total
        rest = 0 

        CantBilletes[0]= vuelto//500
        rest = vuelto % 500
        CantBilletes[1]= rest//100
        rest = rest % 100
        CantBilletes[2]= rest//50
        rest = rest % 50
        CantBilletes[3]= rest//20
        rest = rest % 20
        CantBilletes[4]= rest//10
        rest = rest % 10
        CantBilletes[5]= rest//5
        rest = rest % 5
        CantBilletes[6]= rest//1

        print(" ")
        print("Vuelto: ", end="")
        for i in range(7):
             
             if CantBilletes[i] > 0:
                 print("-",CantBilletes[i]," billete/s de", ValorBilletes[i])
                 print("        ", end="")
             



total = int(input("Ingresar el total de la compra: "))
recibido = int(input("Ingresar el valor recibido: "))

VueltoAEntregar(total, recibido)

'''



'''4

def funcion1(a):

    for i in range(1, a+1, 1):
        print("**********", end="")
        print("                        ", end="")
        funcion2(i)


def funcion2(b):

    cant = b*2
    cont = 1

    while(cont != cant):
        print("*", end="")
        cont = cont + 1

    print("*")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

filas = int(input("Ingresar numero de filas: "))
funcion1(filas)
'''



'''5

cuadrado = lambda x : x ** 2
num = int(input("Ingrese su numero: "))

print(cuadrado(num))
'''



'''6

ParOImpar = lambda x : x % 2

numero = int(input("Ingrese su numero: "))
ParOImpar = ParOImpar(numero)

if ParOImpar == 0:
    print("Su numero es par")
else: print("Su numero es impar")

'''



'''7


def cuadrados(N):

    cuadrados = []

    for i in range(1, N+1, 1):

        cuadrados.insert(i-1, i*i)

    long = len(cuadrados) - 10 

    if len(cuadrados) <= 10:
        print(cuadrados)

    else:
        for i in range(len(cuadrados)-10, len(cuadrados), 1):
            print(cuadrados[i])

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""            

rango = int(input("Ingresar rango (desde 1 hasta N): "))
cuadrados(rango)

'''


'''8

ListaOr = []

ele = input("Ingrese un elemento de la lista(Ingrese 'SIGUIENTE' para continuar): ")

cont = 0

while ele != "SIGUIENTE":

    ListaOr.insert(cont, ele)    
    ele = input("Ingrese un elemento de la lista(Ingrese 'SIGUIENTE' para continuar): ")
    cont = cont + 1



Eliminar = []
ele1 = input("Ingresar elemento a eliminar (ingrese 'SIGUIENTE' para continuar): ")

if ListaOr.count(ele1) == 0 and ele1 != "SIGUIENTE":
    while (ListaOr.count(ele1)) == 0 and ele1 != "SIGUIENTE":
        ele1 = input("Ese elemento no se encuentra en la lista, ingrese uno distinto (ingrese 'SIGUIENTE' para continuar): ")


cont=0

while ele1 != "SIGUIENTE":

    Eliminar.insert(cont, ele1)
    ele1 = input("Ingresar elemento a eliminar (ingrese 'SIGUIENTE' para continuar): ")

    if ListaOr.count(ele1) == 0 and ele1 != "SIGUIENTE":
        while ((ListaOr.count(ele1)) == 0) and ele1 != "SIGUIENTE":
            ele1 = input("Ese elemento no se encuentra en la lista, ingrese uno distinto (ingrese 'SIGUIENTE' para continuar): ")

    cont = cont + 1



    ListaFinal = list(ListaOr)

    for i in range(0, len(Eliminar), 1):

        ListaFinal.remove(Eliminar[i])

    

print("Lista original:", ListaOr)
print("Elementos a eliminar:", Eliminar)
print("Lista final: ", ListaFinal)

'''



'''
9

def ascendente(a):

    ListaMenMay = list(a)
    ListaMenMay.sort()

    if ListaMenMay == a:
        return True
    
    else:
        return False

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


LisAsc = []

elemento = input("Ingrese un elemento de la lista (Ingrese 'FINALIZAR' para continuar): ")

cont = 0

while elemento != "FINALIZAR":

    LisAsc.insert(cont, elemento)    
    elemento = input("Ingrese un elemento de la lista (Ingrese 'FINALIZAR' para continuar): ")
    cont = cont + 1


TOrF = ascendente(LisAsc)
print(TOrF)

'''




'''10

def Capicua(cadena):

    cadena.lower = list(cadena)
    CadenaAlReves= list(cadena.lower)
    CadenaAlReves.reverse()

    if cadena == CadenaAlReves: 
        print("Es capicua") 
    
    else:
        print("No es capicua")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

cadena = input("Ingrese su cadena de caracteres: ")
Capicua(cadena)

'''



'''11

CadenaCar = input("Ingresar cadena de caracteres: ")

CadenaCentrada = CadenaCar.center(80)

print(CadenaCentrada)

'''


'''12

def FechaCompleta(Fecha):

    Mes = ""

    if Fecha[1] == 1:
        Mes = "Enero" 
    elif Fecha[1] == 2:
        Mes = "Febrero"
    elif Fecha[1] == 3:
        Mes = "Marzo"
    elif Fecha[1] == 4:
        Mes = "Abril"
    elif Fecha[1] == 5:
        Mes = "Mayo"
    elif Fecha[1] == 6:
        Mes = "Junio"
    elif Fecha[1] == 7:
        Mes = "Julio"
    elif Fecha[1] == 8:
        Mes = "Agosto"
    elif Fecha[1] == 9:
        Mes = "Septiembre"
    elif Fecha[1] == 10:
        Mes = "Octubre"
    elif Fecha[1] == 11:
        Mes = "Noviembre"
    elif Fecha[1] == 12:
        Mes = "Diciembre"
        

    resultado = str(Fecha[0]) + " de " + str(Mes) + " de " + str(Fecha[2])
        
    return resultado

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



Dia = int(input("Ingresar dia de naciemiento: "))
Mes = int(input("Ingresar mes de naciemiento: "))
Año = int(input("Ingresar año de naciemiento: "))

FechaEnt = (Dia, Mes, Año)

Fecha = FechaCompleta(FechaEnt)

print(Fecha)
'''


13

texto = input("Ingresar texto: ")

lista = texto.split(" ")

conj = set(lista)

print("")

print(conj)

print("")

lista = list(conj)

lista.sort(key=len)

print(lista)


#14 no se entendio el ejercicio


'''15

def eli_subcadena(cadena):

    inicio = int(input("Ingresar posicion de inicio para eliminar: "))

    cant = int(input("Ingresar cantidad de caracteres a eliminar desde la posicion indicada: "))

    final = inicio + cant

    p1 = cadena[0:inicio-1]
    p2 = cadena[final-1:13]
 
    return  p1 + p2



cadena = input("Ingresar texto: ")

subcadena = eli_subcadena(cadena)

print(subcadena)
'''


