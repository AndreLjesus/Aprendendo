from Funções import *


#Teste aprendendo a usar def
while True:
    nome = input("Digite seu nome: ")
    resumo(nome)

    if nome == "pedro":
        break



#Curso em Video: Exercicio 96
base = float(input("Digite a base do quadrado: "))
area_quadrado(base)



#Curso em Video: Exercicio 98
contagem = int(input("Digite um valor inteiro maior que 0: "))
contador(contagem)


#Organizando Valores Lista
lista = []
for c in range(0,5):
    a = int(input("Digite um valor: "))
    lista.append(a)

ordenar_lista(lista)
