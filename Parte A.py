origemx = float(input("Eixo x origem:"))
origemy = float(input("Eixo y origem:"))
pontos = int(input("Quantidade de pontos:"))
lista = []
lista2 = []
lista3 = []
while pontos != 0:
  pontox = float(input("Cordenada x:"))
  pontoy = float(input("Cordenada y:"))
  if pontox > origemx and pontoy > origemy:
     print ("Primeiro quadrante")
     quadrante = "1º quadrante"
     lista3.append(quadrante)
  elif pontox < origemx and pontoy > origemy:
     print ("Segundo quadrante")
     quadrante = "2º quadrante"
     lista3.append(quadrante)
  elif pontox < origemx and pontoy < origemy:
     print ("Terceiro quadrante")
     quadrante = "3º quadrante"
     lista3.append(quadrante)
  elif pontox > origemx and pontoy < origemy:
     print ("Quarto quadrante")
     quadrante = "4º quadrante"
     lista3.append(quadrante)
  else:
     print ("Está sobre o eixo das coordenadas")
  print ("({}, {})".format(pontox, pontoy))
  distancia = ((pontox - origemx)**2 + (pontoy - 
  origemy)**2)**(1/2)
  lista.append(distancia)
  lista2.append("({}, {})".format(pontox, pontoy))
  pontos = pontos - 1
print (lista)
print ("O Ponto mais próximo é:", lista2[lista.index(min(lista))], "Distância de:", format(min(lista), ".2f"))
print ("O Ponto mais distante é:", lista2[lista.index(max(lista))], "Distância de:", format(max(lista), ".2f"))
print ("Quantidade de pontos no 1º quadrante:", lista3.count("1º quadrante"))
print ("Quantidade de pontos no 2º quadrante:", lista3.count("2º quadrante"))
print ("Quantidade de pontos no 3º quadrante:", lista3.count("3º quadrante"))
print ("Quantidade de pontos no 4º quadrante:", lista3.count("4º quadrante"))
