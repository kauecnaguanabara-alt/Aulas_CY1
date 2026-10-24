
with open("listademercado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Maçã\n")
        arquivo.write("Uva\n")
        

def contar_linhas(lista_de_mercado):
    total_linhas=0
    with open("listademercado.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.strip():
                total_linhas+=1
    return total_linhas


quantidade=contar_linhas("listademercado.txt")
print(f"O arquivo tem {quantidade} linhas")











palavras = input("Digite seu texto: ")


from datetime import datetime

agora= datetime.now().strftime("%d-%m-%y %H:%M:%S")

with open("texto.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"[{agora}] Essa é a data de hoje\n")
    arquivo.write(f"{palavras}")

with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

assunto = input("Digite o nome ou assunto do relatório: ").strip().replace(" ", "_")
nome_arquivo = f"{assunto}.txt"
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write("Testando testando")
    print(conteudo)    


            