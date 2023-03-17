class Singleton:

    total = 0

    def __init__(self, nome="Teste"):
        if Singleton.total > 0:
            raise Exception("Não é possível criar mais de um objeto")
        else:
            self.nome = nome
            Singleton.total += 1

    def __str__(self):
        return self.nome
    
a1 = Singleton("A1")
print(a1)

a2 = Singleton("A2")
print(a2)