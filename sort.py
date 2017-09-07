#!/usr/bin/python 2.7.10
# coding: utf-8

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        #                                                                   #
        #                   MESTRADO EM CIENCIAS DA COMPUTACAO              #
        #           DISCIPLINA DE ANÁLISE E PROJETO DE ALGORITMOS           #
        #                   Thiago Giroto Milani    -   02/2017             #
        #                                                                   #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

##### BLIBLIOTECAS #####
import time
from random import randint
import os
import sys

sys.setrecursionlimit(2**30)

################################################################################################################################################################

##### CRIA ARQUIVOS DO INSERTION SORT #####
os.system('touch lista_insertionsort_ordem.txt')
os.system('touch tempo_insertionsort_ordem.txt')

##### CRIA ARQUIVOS DO SELECT SORT #####
os.system('touch lista_selectsort_ordem.txt')
os.system('touch tempo_selectsort_ordem.txt')

##### CRIA ARQUIVOS DO MERGE SORT #####
os.system('touch lista_mergesort_ordem.txt')
os.system('touch tempo_mergesort_ordem.txt')

##### CRIA ARQUIVOS DO QUICK SORT #####
os.system('touch lista_quicksort_inverso.txt')
os.system('touch tempo_quicksort_inverso.txt')

##### CRIA ARQUIVOS DO HEAP SORT #####
os.system('touch lista_heapsort_ordem.txt')
os.system('touch tempo_heapsort_ordem.txt')

################################################################################################################################################################

##### ALGORITMO DE INSERTION SORT #####
def insertionSort(A):
    resp={}
    ini = time.time()
    for i in range(1,len(A)):
        x = A[i]
        j = i-1
        while j>=0 and x<A[j]:
            A[j+1] = A[j]
            j=j-1
        A[j+1] = x
    fim = time.time()
    resp['tempo']=fim-ini
    resp['lista']=A
    return resp

################################################################################################################################################################

##### ALGORITMO DE SELECT SORT #####
def selectionSort (lista):
    resp={}
    ini = time.time()
    for i in range(0,len(lista)):
        menor=i
        for k in range(i,len(lista)):
            if lista[k]<lista[menor]:
                menor=k
        lista[menor],lista[i]=lista[i],lista[menor]
    fim = time.time()
    resp['tempo']=fim-ini
    resp['lista']=lista
    return resp
################################################################################################################################################################

##### ALGORITIMO DE MERGE SORT #####
def mergesort(alist):
    resp={}
    ini = time.time()
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    fim = time.time()
    resp['tempo']=fim-ini
    resp['lista']=alist
    return resp

################################################################################################################################################################

##### ALGORITMO QUICK SORT #####

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


def quicksort(myList, start, end):
    resp={}
    ini = time.time()
    if start < end: 
        split = partition(myList, start, end)
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    fim = time.time()
    resp['tempo']=fim-ini
    resp['lista']=myList
    return resp

################################################################################################################################################################

##### ALGORITMO DE HEAP SORT #####
def heapsort(lst):
    resp={}
    ini = time.time()
    for start in range((len(lst)-2)/2, -1, -1):
        siftdown(lst, start, len(lst)-1)
    for end in range(len(lst)-1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1)
    fim = time.time()
    resp['tempo']=fim-ini
    resp['lista']=lst
    return resp

def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break

################################################################################################################################################################

##### CRIA LISTA COM N ELEMENTOS ALEATORIOS #####

N = 50000
A=[]
for i in range(1,N):
    A.append(randint(1,N))

################################################################################################################################################################

##### CRIA LISTA COM N ELEMENTOS ORDENADOS #####
"""
N = 5000
A = range (N)
"""
################################################################################################################################################################

##### CRIA LISTA COM N ELEMENTOS INVERSAMENTE ORDENADOS #####
"""
N = 5000
B = range (N)
A=[]
for i in reversed(B):
    A.append (B[i])
"""
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

##### CHAMA A FUNCAO INSERTIONSORT #####

C = insertionSort(list (A))
print ('INSERTIONSORT = '+str(C['lista'])+str(C['tempo']))
w_lista = open('lista_insertionsort_ordem.txt','a')
w_tempo = open('tempo_insertionsort_ordem.txt','a')
w_lista.write (str(C['lista']))
w_lista.write ('\n')
w_tempo.write (str(C['tempo']))
w_tempo.write ('\n')
w_lista.close()
w_tempo.close()

##### CHAMA A FUNCAO SELECTIONSORT #####

C = selectionSort(list (A))
print ('SELECTIONSORT = '+str(C['lista'])+str(C['tempo']))
w_lista = open('lista_selectsort_ordem.txt','a')
w_tempo = open('tempo_selectsort_ordem.txt','a')
w_lista.write (str(C['lista']))
w_lista.write ('\n')
w_tempo.write (str(C['tempo']))
w_tempo.write ('\n')
w_lista.close()
w_tempo.close()

##### CHAMA A FUNCAO MERGESORT #####

C = mergesort(list (A))
print ('MERGSORT = '+str(C['lista'])+str(C['tempo']))
w_lista = open('lista_mergesort_ordem.txt','a')
w_tempo = open('tempo_mergesort_ordem.txt','a')
w_lista.write (str(C['lista']))
w_lista.write ('\n')
w_tempo.write (str(C['tempo']))
w_tempo.write ('\n')
w_lista.close()
w_tempo.close()

##### CHAMA A FUNCAO QUICKSORT #####

C = quicksort(A, 0 ,len(A) -1)
print ('QUICKSORT = '+str(C['lista'])+str(C['tempo']))
w_lista = open('lista_quicksort_inverso.txt','a')
w_tempo = open('tempo_quicksort_inverso.txt','a')
w_lista.write (str(C['lista']))
w_lista.write ('\n')
w_tempo.write (str(C['tempo']))
w_tempo.write ('\n')
w_lista.close()
w_tempo.close()

##### CHAMA A FUNCAO HEAPSORT #####

C = heapsort(list (A))
print ('HEAPSORT = '+str(C['lista'])+str(C['tempo']))
w_lista = open('lista_heapsort_ordem.txt','a')
w_tempo = open('tempo_heapsort_ordem.txt','a')
w_lista.write (str(C['lista']))
w_lista.write ('\n')
w_tempo.write (str(C['tempo']))
w_tempo.write ('\n')
w_lista.close()
w_tempo.close()
