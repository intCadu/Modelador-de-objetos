# 1. Crie uma classe Animal que tenha os atributos nome e idade e o método emitir_som(). 
# Crie também as classes Cachorro, Gato e Pato que herdem da classe Animal e sobrescrevam 
# o método emitir_som() para retornar “au au”, “miau” e “quack” respectivamente. 
# Crie alguns objetos dessas classes e teste o método emitir_som() em cada um.


# class Animal:
#     def __init__(self,name,idade):
#         self.name = name
#         self.idade = idade
        

#     def emitir_son(self):
#         print("rosnar")


# class Cachorro(Animal):
#     def __init__(self, name, idade):
#         super().__init__(name, idade)
#     def emitir_son(self):
#         print("Au, Au")

# class Gato(Animal):
#     def __init__(self, name, idade):
#         super().__init__(name, idade)
#     def emitir_son(self):
#         print("Miau")
   
       

# class Pato(Animal):
#     def __init__(self, name, idade):
#         super().__init__(name, idade)
#     def emitir_son(self):
#         print ("Quack")

# cachorro1 = Cachorro("Vira-Lata", 5)
# gato1 = Gato("Persa", 6)
# pato1 = Pato("Marreco",2)


# cachorro1.emitir_son()
# gato1.emitir_son()
# pato1.emitir_son()


# 2. Crie uma classe Veiculo que tenha os atributos modelo, cor e ano e o método ligar(). 
# Crie também as classes Carro, Moto e Bicicleta que herdem da classe Veiculo e sobrescrevam o método ligar() para imprimir 
# “O carro está ligado”, “A moto está ligada” e “A bicicleta está pronta” respectivamente. 
# Crie alguns objetos dessas classes e teste o método ligar() em cada um.


class Veiculo:
    def __init__(self, modelo, cor, ano, ligado):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.ligado = ligado
    
    def ligar(self):
        if self.ligado == "ON":
            print(f"O {self.modelo} está ligado!")
        else:
            print(f"O {self.modelo} está desligado!")

class Carro(Veiculo):
    def __init__(self, modelo, cor, ano, ligado):
        super().__init__(modelo, cor, ano, ligado)
    def ligar(self):
        if self.ligado == "ON":
            print(f"O {self.modelo} está ligado!")
        else:
            print(f"O {self.modelo} está desligado!")

class Moto(Veiculo):
    def __init__(self, modelo, cor, ano, ligado):
        super().__init__(modelo, cor, ano, ligado)
    def ligar(self):
        if self.ligado == "ON":
            print(f"O {self.modelo} está ligado!")
        else:
            print(f"O {self.modelo} está desligado!")

class Bicicleta(Veiculo):
    def __init__(self, modelo, cor, ano, ligado):
        super().__init__(modelo, cor, ano, ligado)
    def ligar(self):
        if self.ligado == "ON":
            print(f"O {self.modelo} está ligado!")
        else:
            print(f"O {self.modelo} está desligado!")

carro1 = Carro("UNO", "Preto", "1995", "ON")
moto1 = Moto("FAN", "Vermelho", "2013", "OFF")
bicicleta1 = Bicicleta("CALOI", "Azul", "2018", "ON")
        
