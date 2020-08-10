numeros = []
numeros.append(int(input("Primeiro numero:")))
numeros.append(int(input("Segundo numero:")))
numeros.append(int(input("Terceiro numero:")))

if(numeros[2] < numeros[1]) or (numeros[1] < numeros[0]):
   print("não está em ordem crescente")
else:
   print("crescente")





