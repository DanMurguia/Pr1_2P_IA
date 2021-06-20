import random
import math
import operator

lista_cromosomas =[]
n_cromosomas = 5
evaluacion_ordenada = []

def crear_cromosomas(n_cromosomas):
    while n_cromosomas > 0 :
        nuevo_cromosoma =[]
        n = random.randint(0,255)
        n_bin = "{0:08b}".format(n)
        nuevo_cromosoma[:0] = n_bin
        for i in range(0,len(nuevo_cromosoma)):
            nuevo_cromosoma[i] = int(nuevo_cromosoma[i])
        lista_cromosomas.append(nuevo_cromosoma)
        n_cromosomas -= 1

def evaluacion(funcion, evaluacion_ordenada):
    if len(evaluacion_ordenada) > 0:
        evaluacion_ordenada.clear()
    if funcion == 0:
        pos = 0
        cromosomas_evaluados = {}
        for lista in lista_cromosomas:
            decimal = lista_a_decimal(lista)
            n_evaluado = math.pow(decimal,2)
            cromosomas_evaluados[pos] = n_evaluado
            pos += 1
        print(cromosomas_evaluados)
        evaluacion_ordenada = sorted(cromosomas_evaluados.items()
                                      , key=operator.itemgetter(1))
        print(evaluacion_ordenada)
            
    '''elif funcion == 1:
    elif funcion == 2:
    elif funcion == 3:
    elif funcion == 4:'''


def lista_a_decimal(lista):
    n_bin = ''.join([str(elem) for elem in lista])
    numero = int(n_bin,2)
    return numero

if __name__ == '__main__':
    crear_cromosomas(n_cromosomas)
    evaluacion(0, evaluacion_ordenada)
    