class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
       print (f"Olá eu sou {self.nome}!")
        
    def apresentar_idade(self):
       print (f"Minha idade é {self.idade}!")

pessoa = Pessoa("João", 30)
pessoa.apresentar()
pessoa.apresentar_idade()

# class Circulo():
#     def __init__(self, raio):
#         self.raio = raio

#     def calcular_area(self):
#         area =  3.14 * (self.raio ** 2)
#         return area
#     def calculo(self):
#         circunferencia = 3.14 * self.raio
#         return circunferencia    

# circulo = Circulo(13)
# print(circulo.calcular_area())
# print(f"{circulo.calculo():.2f}")

# class contaBancária:
#     def __init__(self, name, saldo):
#         self.name = name
#         self.saldo = saldo
#     def depósito(self):
