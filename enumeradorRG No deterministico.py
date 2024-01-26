import itertools

print("--Enumerador de Gramáticas Regulares--")

LETRAS_MIN = ['\u03B5','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

LETRAS_MAY = ['S','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','T','U','V','W','X','Y','Z']

E = int(input("Introduza el tamaño del Alfabeto: "))#Variable para el tamaño del alfabeto

NUM_RG = int(input("Introduzca el numero de RG: "))#Numero de Gramatica Regular que se busca

rangos = [1]#Vector donde luego se cargaran 

#funcion para calcular el factorial de un numero
def factorial(numero):
    factorial = 1
    i = 1
    while (i <= numero):
        factorial = factorial * i
        i = i + 1
    return(factorial)

#Es la formula que halle para enumerar las gramaticas regulares, no tiene la potencia de Vn porque asi puedo usar la funcion en la conversion
def formula_enumeracion(E,Vn):
    sum = 0 #Acumulador para la sumatoria
    for x in range(1,(E+(E*Vn)+1)+1):
        res = (factorial((E+(E*Vn)+1)))/(factorial(x)*factorial((((E+(E*Vn)+1))-x)))
        sum = sum + res
    return(sum)#Ese mas 1 es dudosisimo

#Calcula como serán los rangos en base al tamaño del alfabeto
def crear_rangos(E):        
    Rg = 0#Sera el numero del limite superior del rango dependiendo de la formula (E*(1+x)+1)**x
    for i in range(1, 5):#Mejorar rango de creacion, comparar el Numero de RG con la formula
        Vn = (formula_enumeracion(E,i))**i #Formula para hallar el rango
        Rg = Vn + Rg #Acumulador para sumar rango a rango y crear el limite superior
        rangos.append(int(Rg))#Se agrega el limite superior al rango
        
        if i != 4:
            rangos.append(int(Rg+1))#Se agrega el limite inferior al rango
    print(rangos)

VNINF = 0#Variable global del limite inferior del rango elegido
VNSUP = 0#Variable global del limite superior del rango elegido
#Con esta funcion se encuentra el tamaño del alfabeto no terminal
def encontrar_Vn():
    Vn = 1#Es el numero de letras en el alfabeto no terminal
    global VNINF #Se hace accesible la variable dentro de la funcion
    global VNSUP
    for x in range(0, len(rangos), 2):#Se itera saltando de a 2 para utilizar unicamente los limites inferiores de los rangos.
        if NUM_RG >= rangos[x] and NUM_RG <= rangos[x+1]:#Se compara el numero de RG con los limites inferior y superior de cada rango.
            VNINF = x #Se guarda el rango inferior en una variable global para hacer calculos posteriores 
            VNSUP = x+1
            return (Vn)#Retornamos el numero de letras no terminales
        Vn = Vn + 1#Si nuestro numero de RG no esta en el rango que comparamos le sumamos una letra más para ir al siguiente rango
'''
#Convierte decimales a cualquier base exista hasta 36
def dec_to_base(num,base):  #Maximum base - 36
    base_num = ""
    if num == 0:
        return('0')
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base

    base_num = base_num[::-1]  #To reverse the string
    return base_num
'''

def dec_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

NUMERO_BASE = 0
VECTOR = []#Tendrá las combinaciones posibles para la cantidad de elementos Terminales y No terminales
#Primero encuentra la cantidad de Simbolos No terminales, luego hace la resta y conversion a la base que requiere el rango
def calculo_base():
    global NUMERO_BASE
    global VECTOR
    Vn = encontrar_Vn()
    print("Cant de Vn> ", Vn)
    Rel = NUM_RG - rangos[VNINF]
    #tamano = rangos[VNSUP] - rangos[VNINF]
    #print(Rel)
    #print(tamano - Rel)
    base = formula_enumeracion(E,Vn)
    #base = (E+(E*Vn)+1)
    print(base)
    NUMERO_BASE = dec_to_base(Rel,base)
    resta = Vn - len(NUMERO_BASE)
    for x in range(resta):
        NUMERO_BASE.insert(0,0)
    #print(NUMERO_BASE)
    #Agregar los números a la matriz de base nueva con las combinaciones posibles
    for i in range(E+1):
        VECTOR.append(LETRAS_MIN[i])
    for j in range(Vn):
        for k in range(E):
            VECTOR.append(LETRAS_MIN[1+k]+LETRAS_MAY[j])
            
def subconjuntos(arr):
    """Genera todos los subconjuntos de un arreglo dado."""
    res = [[]]

    for num in arr:
        res += [current + [num] for current in res]

    return res

def ordenar_lexicograficamente(subsets):
    """Ordena los subconjuntos de forma lexicográfica."""
    for i in range(len(subsets)):
        subsets[i].sort()
    return sorted(subsets, key=lambda x: ((len(x) > 0 and x[0] != '\u03B5', len(x), x)))





def crear_producciones():
    for i in range(len(NUMERO_BASE)):
        print(LETRAS_MAY[i],"->" ,subconjuntos_ordenados[NUMERO_BASE[i]+1])

crear_rangos(E)

calculo_base()
print(VECTOR)

todos_los_subconjuntos = subconjuntos(VECTOR)
subconjuntos_ordenados = ordenar_lexicograficamente(todos_los_subconjuntos)
crear_producciones()

print("Fin de la ejecucion.")