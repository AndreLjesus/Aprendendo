import random

nome = ["Quazar", "Star", "Fr", "Quick", "masT","ARP"]
sobrenome = ["ZzZ", "m4pl", "strsr", "pool", "Hells"]
tamanho = 3
nome_completo = nome + sobrenome

nome_usuario = "".join(random.sample(nome_completo, tamanho))
print(nome_usuario)
