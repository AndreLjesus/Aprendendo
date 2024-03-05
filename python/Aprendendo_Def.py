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

