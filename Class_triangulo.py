class Triangulo:
    def __init__(self,LadoA,LadoB,LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC
    
    def perimetro(self):
        soma = self.LadoA + self.LadoB + self.LadoC
        return soma


    def Maior(self):
        lista = [self.LadoA,self.LadoB,self.LadoC]
        return max(lista)


Lado1 = int(input("Digite o valor do Primeiro Lado:"))


Triangulo1 = Triangulo(Lado1,Lado2,Lado3)

print(Triangulo1.perimetro())