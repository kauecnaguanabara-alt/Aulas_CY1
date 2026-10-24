Segmentos = int(input("Quantos segmentos há no seu jogo? "))
engrenagens = int(input("Quantas engrenagens tem no segmento? "))
remedios = int(input("Quantos remedios tem no segmento? "))

# Agora a multiplicação vai funcionar perfeitamente
totalengrenagem = Segmentos * engrenagens
totalremedios = Segmentos * remedios

# Adicionada a vírgula que faltava depois de totalengrenagem
print("Seu jogo possui", Segmentos, "segmentos com", totalengrenagem, "engrenagens e", totalremedios, "remedios.")