#open("caminho","r")

# r - leitura
# a - append / incrementar
# w - escrita
# x - criar arquivo
# r+ - leitura + escrita


arquivo = open("arquivo_teste.txt","x")

lista = arquivo.readlines()

print(lista)

arquivo.write("\nNoava palavra")

arquivo.close()