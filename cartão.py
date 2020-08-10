meucartão = int(input("Digite o número do seu cartão de crédito:"))

cartãolido = 1
encontreimeucartãonalista = False

while cartãolido != 0 and not encontreimeucartãonalista:
     cartãolido = int(input("Digite o número do próximo cartãp de crédito:"))
     if cartãolido == meucartão:
         encontreimeucartãonalista = True

if encontreimeucartãonalista:
    print("Eba!!! Meu cartão está lá")
else:
     print("Xi!!! Meu cartão não está lá")
                
