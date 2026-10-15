import time
from random import randrange
import ordenacao
import threading

def testeInsertion(arr):
    insertionSort = ordenacao.ordenacao()
    
    #abrindo um thread para ele realizar o teste1
    inicio = time.perf_counter()
    resultado = insertionSort.insertion_sort(arr)
    fim = time.perf_counter()
    
    #pegando a diferenca entre quando comecou a iniciar e terminou
    tempoTot = (fim - inicio)
    return {"tempo":tempoTot, "quantidadeOperacoes": resultado[1], "arr":resultado[0]}

def testeMerge(arr):
    insertionSort = ordenacao.ordenacao()
    
    #abrindo um thread para ele realizar o teste1
    inicio = time.perf_counter()
    resultado = insertionSort.merge_sort(arr)
    fim = time.perf_counter()
    
    #pegando a diferenca entre quando comecou a iniciar e terminou
    tempoTot = (fim - inicio)
    return {"tempo":tempoTot, "quantidadeOperacoes": resultado[1], "arr":resultado[0]}

#Gerando Objeto com arrays para ser ordenado
nEle = [5, 10, 20, 30, 50, 75, 100, 200, 500, 1000]
objArr = {}
arrVazio = []

for i in nEle:
    objArr[i] = []
    for j in range(i):
        objArr[i].append(randrange(0, i)) 
    
arrInvertido = objArr[1000].copy()
arrInvertido.sort(reverse=True)

#TestesInsertion
rep = 10
mediaTempo = 0

#teste casos dificeis


#teste nos elementos


