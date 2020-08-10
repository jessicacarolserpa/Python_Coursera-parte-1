largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
caractere = "#"

def retangulo (largura, altura, caractere):
    linha = caractere * largura
    for i in range(altura):
        print(linha)

retangulo(caractere, altura, largura)
