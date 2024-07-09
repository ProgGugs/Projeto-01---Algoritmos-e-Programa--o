partidarobox = float(input("Digite a coordenada X do ponto de origem A do robô: "))
partidaroboy = float(input("Digite a coordenada Y do ponto de origem A do robô: "))
tempo = float(input("Digite por quanto tempo o robô irá caminhar: "))
subindo = partidaroboy
direita = partidarobox
while tempo != 0:
  subindo = subindo + 1
  tempo = tempo - 1
  if tempo == 0:
    break 
  else:
    direita = direita + 1
    tempo = tempo - 1
  if tempo == 0:
    break
  else: 
    direita = direita + 1
    tempo = tempo - 1
print ("Ao final da caminhada o robô estará no ponto","({}, {})".format(direita, subindo))