#!/usr/bin/python 3.6
# coding: utf-8
#
#                    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                    #                                                                   #
#                    #                    MESTRADO EM CIENCIAS DA COMPUTACAO             #
#                    #                   DISCIPLINA DE INTELIGÊNCIA ARTIFICIAL           #
#                    #                   Thiago Giroto Milani    -    02/2017            #
#                    #                          tmilani@rc.unesp.br                      #
#                    #                                                                   #
#                    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
nodes = {}

if __name__ == "__main__":
    with open("coordenadas.txt") as arquivo:
        linha = arquivo.readline()
        while (linha != ""):
            # PEGA NODE VIZINHOS DO NODE ATUAL
            vizinhos = linha.split(";")[1]
            # SEPARA CADA TUPLA DE DISTANCIA DO NODE
            lista_vizinhos = vizinhos.split(",")
            tupla_viz = []
            for i in range(len(lista_vizinhos)):
                vizinho = str(lista_vizinhos[i]).rstrip("\n")
                #PEGA O NODE E A DISTANCIA DO NO ATUAL
                tupla_viz.append((vizinho.split(" ")[0],vizinho.split(" ")[1]))                      
                nodes[linha.split(";")[0]] = tupla_viz                     
            linha = arquivo.readline()
 
    pilha = []
    caminho = []
    #INICIA O NODE
    pilha.append("i") 
    while pilha[0] != "f":
        print("Pilha ",pilha,"\n")
        # REMOVE O ULTIMO ELEMENTO DA PILHA
        caminho.append(pilha.pop(0))
        print("Expandindo a pilha ",caminho[-1])
        if nodes.get(caminho[-1]) == None:
            caminho.pop(-1)
            print("Fim do Caminho")
        for i in range(len(nodes.get(caminho[-1]))-1,-1,-1):
            #SELECIONA A PILHA DE VIZINHOS
            pilha.insert(0,nodes.get(caminho[-1])[i][0])
        
    caminho.append(pilha[0])  
    print("\nCaminho até F: ",caminho)   
            

            
        
        
