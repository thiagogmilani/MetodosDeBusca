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
distancia       = {}
nodes           = {}

if __name__ == "__main__":
    with open("coordenadas.txt") as arquivo:
        linhas = arquivo.readline()
        while (linhas != ""):
            # PEGA NODE VIZINHOS DO NODE ATUAL
            vizinhos = linhas.split(";")[1]
            # SEPARA CADA TUPLA DE DISTANCIA DO NODE
            lista_vizinhos = vizinhos.split(",")
            tupla_viz = []
            for i in range(len(lista_vizinhos)):
                vizinho = str(lista_vizinhos[i]).rstrip("\n")
                #PEGA O NODE E A DISTANCIA DO NO ATUAL
                tupla_viz.append([vizinho.split(" ")[0], int(vizinho.split(" ")[1])])
                                    
                nodes[linhas.split(";")[0]] = tupla_viz                     
            linhas = arquivo.readline()
            
    with open("distancias.txt") as arquivo:
        linhas = arquivo.readline().rstrip("\n")
        while (linhas != ""):
            distancia[linhas.split(";")[0]] = float(linhas.split(";")[1])
            linhas = arquivo.readline().rstrip("\n")

    # ALTERA AS COORDENADAS COM O VALOR DA FUNCAO 
    for i in nodes:
        for j in nodes[i]:
            j[1] =  j[1] + distancia[j[0]]

    pilha = []
    caminho = []
    #INICIA O NODE
    pilha.append("i")
    while pilha[0][0] != "f":
        print("Pilha ",pilha,"\n")
        # REMOVE O ULTIMO ELEMENTO DA PILHA
        caminho.append(pilha.pop(0)[0])
        print("Expandindo a pilha ",caminho[-1][0])
        if nodes.get(caminho[-1][0]) == None:
            caminho.pop(-1)
            print("Fim do Caminho")
        else:
            for i in range(len(nodes.get(caminho[-1][0]))):
                #SELECIONA A PILHA DE VIZINHOS
                pilha.append(nodes.get(caminho[-1][0])[i])
            pilha = sorted(pilha, key=lambda pilha: pilha[1])
       
    caminho.append(pilha[0][0])  
    print("\nCaminho até F: ",caminho)   

            
        
        
