Segmentos = int(input("Quantos segmentos há no seu jogo? "))
item = int(input("Quantas itens tem no segmento? "))
armas = int(input("Quantos armas tem no segmento? "))
subsegmentos=int(input("Quantos subsegmentos tem no segmento? "))

# Agora a multiplicação vai funcionar perfeitamente
totalsegmentos= Segmentos*subsegmentos
totalengrenagem = totalsegmentos * item
totalremedios = totalsegmentos * armas

# Adicionada a vírgula que faltava depois de totalengrenagem
print("Seu jogo possui", totalsegmentos, "segmentos com", totalengrenagem, "engrenagens e", totalremedios, "remedios.")e5u´p0r6pki0