# class Animal:
#     def comer(self):
#         print("O Animal está comendo")

#     def andar(self):
#         print("O Animal está andando na jaula")


# class Felino(Animal):
#     def lamber(self):
#         print("O Felino está lambendo seu pelo")

#     def comer(self):
#         print("O Felino está comendo")


# animal = Animal()
# animal.comer()  # O Animal está comendo
# felino = Felino()
# felino.comer()  # O Felino está comendo


class Animal:
    def comer(self):
        print("O Animal está comendo")

    def andar(self):
        print("O Animal está andando na jaula")


class Felino(Animal):
    def lamber(self):
        print("O Felino está lambendo seu pêlo")


class Leao(Felino):
    def rugir(self):
        print("O Leão está rugindo alto !!!")


class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()


renatinho = Pessoa()
animal = Animal()
felino = Felino()
leao = Leao()

renatinho.observa(animal)  # O Animal está comendo
renatinho.observa(felino)  # O Animal está comendo
renatinho.observa(leao)  # O Animal está comendo
