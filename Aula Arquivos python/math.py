import math
import os
import calculadora

#print(math.pow(2,3)+5)

#x=float(input("Digite o valor: "))
#y=float(input("Digite o valor: "))

#resultado = math.pow(x,y)
#print(resultado)


#print(math.ceil(resultado))
#print(math.trunc(resultado))

with open("texto.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Maçã\n")
        arquivo.write("Uva\n")

if os.path.exists("texto.txt"):
    os.remove("texto.txt")
else:
      print("O arquivo não existe")



print(calculadora.soma(10,30))
print(calculadora.subtracao(10,30))
print(calculadora.divisao(10,30))
print(calculadora.multiplicacao(10,30))


