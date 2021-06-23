import random
import math
import operator

def crear_cromosomas(n_cromosomas, lista_cromosomas):
    while n_cromosomas > 0:
        nuevo_cromosoma = []
        n = random.randint(0, 255)
        print(n)
        n_bin = "{0:08b}".format(n)
        nuevo_cromosoma[:0] = n_bin
        for i in range(0, len(nuevo_cromosoma)):
            nuevo_cromosoma[i] = int(nuevo_cromosoma[i])
        lista_cromosomas.append(nuevo_cromosoma)
        n_cromosomas -= 1
    return lista_cromosomas


def evaluacion(funcion, evaluacion_ordenada,lista_cromosomas):
    print("######Evaluando individuos######")
    if len(evaluacion_ordenada) > 0:
        evaluacion_ordenada.clear()
    if funcion == 0:
        pos = 0
        cromosomas_evaluados = {}
        for lista in lista_cromosomas:
            decimal = lista_a_decimal(lista)
            print(decimal)
            n_evaluado = math.pow(decimal, 2)
            cromosomas_evaluados[pos] = n_evaluado
            pos += 1
        evaluacion_ordenada = sorted(
            cromosomas_evaluados.items(), key=operator.itemgetter(1))
    elif funcion == 1:
        pos = 0
        cromosomas_evaluados = {}
        for lista in lista_cromosomas:
            decimal = lista_a_decimal(lista)
            rad = (decimal * math.pi) / 180
            n_evaluado = math.sin(rad) * 40
            cromosomas_evaluados[pos] = n_evaluado
            pos += 1
        evaluacion_ordenada = sorted(
            cromosomas_evaluados.items(), key=operator.itemgetter(1))
    elif funcion == 2:
        pos = 0
        cromosomas_evaluados = {}
        for lista in lista_cromosomas:
            decimal = lista_a_decimal(lista)
            rad = (decimal * math.pi) / 180
            n_evaluado = math.cos(rad) + decimal
            cromosomas_evaluados[pos] = n_evaluado
            pos += 1
        evaluacion_ordenada = sorted(
            cromosomas_evaluados.items(), key=operator.itemgetter(1))
    elif funcion == 3:
        pos = 0
        cromosomas_evaluados = {}
        for lista in lista_cromosomas:
            decimal = lista_a_decimal(lista)
            n_evaluado = (1000 / abs(50 - decimal)) + decimal
            cromosomas_evaluados[pos] = n_evaluado
            pos += 1
        evaluacion_ordenada = sorted(
            cromosomas_evaluados.items(), key=operator.itemgetter(1))
    elif funcion == 4:
        pos = 0
        cromosomas_evaluados = {}
        for lista in lista_cromosomas:
            decimal = lista_a_decimal(lista)
            n_evaluado = (1000 / abs(30 - decimal)) + \
                          (1000 / abs(50 - decimal)) + \
                           (1000 / abs(80 - decimal)) + decimal
            cromosomas_evaluados[pos] = n_evaluado
            pos += 1
        print(cromosomas_evaluados)
        evaluacion_ordenada = sorted(
            cromosomas_evaluados.items(), key=operator.itemgetter(1))
        print(evaluacion_ordenada)
    return evaluacion_ordenada


def seleccionar(evaluacion_ordenada, lista_cromosomas, maxOmin):
    print("######Seleccionando individuos######")
    tamaño = len(lista_cromosomas)
    pos = 0
    if(maxOmin == 1):
        while pos < tamaño / 2:
            print(evaluacion_ordenada[0][0])
            if evaluacion_ordenada[0][0] > (len(lista_cromosomas) - 1):
                lista_cromosomas.pop(evaluacion_ordenada[0][0] - pos)
            else:
                lista_cromosomas.pop(evaluacion_ordenada[0][0])
            evaluacion_ordenada.pop(0)
            pos += 1
            print(lista_cromosomas)
            print(evaluacion_ordenada)
    elif(maxOmin == 2):
        while pos < tamaño / 2:
            print(evaluacion_ordenada[-1][0])
            if evaluacion_ordenada[-1][0] > (len(lista_cromosomas) - 1):
                lista_cromosomas.pop(evaluacion_ordenada[-1][0] - pos)
            else:
                lista_cromosomas.pop(evaluacion_ordenada[-1][0])
            evaluacion_ordenada.pop(-1)
            pos += 1
            print(lista_cromosomas)
            print(evaluacion_ordenada)
    return lista_cromosomas


def lista_a_decimal(lista):
    n_bin = ''.join([str(elem) for elem in lista])
    numero = int(n_bin, 2)
    return numero


def cruzamiento(lista_cromosomas, intervalo, n_cromosomas, cont, largo):
    print("#######CRUZAMIENTO#######")
    if (cont+1)<largo:
        nuevo_cromosoma=[]
        pos=0
        while pos<intervalo:
            nuevo_cromosoma.append(lista_cromosomas[cont][pos])
            pos += 1
        while pos<(len(lista_cromosomas[0])):
            nuevo_cromosoma.append(lista_cromosomas[cont+1][pos])
            pos += 1
        print(nuevo_cromosoma)
        lista_cromosomas.append(nuevo_cromosoma)
        print(lista_cromosomas)
        nuevo_cromosoma.clear()
        pos=0
        while pos<intervalo:
            nuevo_cromosoma.append(lista_cromosomas[cont+1][pos])
            pos+=1
        while pos<(len(lista_cromosomas[0])):
            nuevo_cromosoma.append(lista_cromosomas[cont][pos])
            pos+=1
        print(nuevo_cromosoma)
        nuevo_cromosoma=mutacion(nuevo_cromosoma)
        lista_cromosomas.append(nuevo_cromosoma)
        print(lista_cromosomas)
        cruzamiento(lista_cromosomas,intervalo,n_cromosomas,cont+2,largo)
        
def mutacion(cromosoma):
    pos = random.randint(0,7)
    if cromosoma[pos] == 0:
        cromosoma[pos] = 1
    elif cromosoma[pos] == 1:
        cromosoma[pos] = 0
    return cromosoma

def init(funcion,modo,cromo,gens,x):
    lista_cromosomas = []
    func = funcion
    n_cromosomas = 8
    evaluacion_ordenada = []
    maxOmin = modo
    intervalo = x
    n_gen = gens
    lista_cromosomas=crear_cromosomas(n_cromosomas, lista_cromosomas)
    print(lista_cromosomas)
    for i in range(0,n_gen):
        evaluacion_ordenada=evaluacion(modo, evaluacion_ordenada,lista_cromosomas)
        lista_cromosomas=seleccionar(evaluacion_ordenada,lista_cromosomas,maxOmin)
        print(lista_cromosomas)
        cruzamiento(lista_cromosomas,intervalo,n_cromosomas,0,len(lista_cromosomas))
