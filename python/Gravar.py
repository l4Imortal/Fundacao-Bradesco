arquivo = open("arquivo.txt", "w")

arquivo.write("Curso Python \n")
arquivo.write("Aula Pratica")
arquivo.close()

leitura = open("arquivo.txt", "r")
print(leitura.read())
leitura.close()