#Aprendendo a usar def
def linhas(nome):
    print()
    print("-"* 26)
    print(" "*10 +  "ola "+ nome + " "*13)
    print("-"* 26)
    print()


def boletim(materia):
    import random

    a = random.randint(0,10)
    b = random.randint(0,10)
    s = (a + b) / 2 
    print(materia, s)

def resumo(nome):
    from Funções import linhas
    from Funções import boletim

    linhas(nome)
    boletim("Portugues: ")
    boletim("Matematica: ")
    boletim("Historia: ")
    boletim("Geografia: ")
    print()


#Curso em Video: Exercicio 96
def area_quadrado(base):
    area = base ** 2
    print("A area do quado é {}".format(area))
    

#Curso em Video: Exercicio 98
def contador(contagem):
    for c in range(contagem):
        print(c)


#Organizando Valores Lista
def ordenar_lista(lista):
    b = sorted(lista)
    print(b)


#Contador
def contador(i,f,p):

    """
        A função Contador faz uma contagem na tela, onde:

        I -> representa o inicio da contagem.
        F -> representa o final da contagem.
        P -> representa o passo da contagem.
        retur -> sem retorno
    """

    c = i
    print("-"*20)
    while c <= f:
        print("{}".format(c), end='...')
        c += p
    print("FIM...")
    print("-"*20)


#Dobrar valores da lista
def dobra(lista):
    
    indice = 0
    while indice < len(lista):
        lista[indice] = lista[indice] * 2
        indice +=1
    print(lista)


#Calculadora area Terrenos: Exercico 96
def terreno():
    print()
    print("-"*20)
    largura = float(input("Digite a largura do terreno: "))
    comprimento = float(input("Digite a comprimento do terreno: "))
    area_terreno = largura * comprimento
    print("A area do terreno avaliado equivale a: {}".format(area_terreno))
    print("-"*20)
    print()


#Adaptar texto: Exercicio 97
def adaptar(lista):
    quantidade_caracteres = lista
    print("~"*len(lista))
    print(lista)
    print("~"*len(lista))
