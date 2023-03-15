import random

class Pokemon:
    def __init__(self, name, type, power, level):
        self.name = name
        self.type = type
        self.power = power
        self.level = level
    def battle(self, oponente):
        print(f"Entrou {self.name} VS {oponente.name}")
    
        if self.type == "Fire":
            match oponente.type:
                case "Water":
                    if ((self.power/2) * self.level) < (oponente.power * oponente.level):
                        print(f"Seu {oponente.name} venceu a batalha!!")
                    else:
                        print(f"Seu {oponente.name} perdeu a batalha!!")
                case "Grass":
                    if (self.power * self.level) > ((oponente.power/2) * oponente.level):
                        print(f"Seu {oponente.name} perdeu a batalha!!")
                    else:
                        print(f"Seu {oponente.name} venceu a batalha!!")
                case "Fire":
                    if (self.power * self.level) == (oponente.power * oponente.level):
                        print("A batalha foi considerada empate!!")
                    elif (self.power * self.level) > (oponente.power * oponente.level):
                        print(f"Seu {oponente.name} perdeu a batalha!!")
                    elif (self.power * self.level) < (oponente.power * oponente.level):
                        print(f"Seu {oponente.name} venceu a batalha!!")
        
        if self.type == "Water":
            match oponente.type:
                case "Grass":
                    if ((self.power/2) * self.level) < (oponente.power * oponente.level):
                        print(f"Seu {oponente.name} venceu a batalha!!")
                    else:
                        print(f"Seu {oponente.name} perdeu a batalha!!")
                case "Fire":
                    if (self.power * self.level) > ((oponente.power/2) * oponente.level):
                        print(f"Seu {oponente.name} perdeu a batalha!!")
                    else:
                        print(f"Seu {oponente.name} venceu a batalha!!")
                case "Water":
                    if (self.power * self.level) == (oponente.power * oponente.level):
                        print("A batalha foi considerada empate!!")
                    elif (self.power * self.level) > (oponente.power * oponente.level):
                        print(f"Seu {oponente.name} perdeu a batalha!!")
                    elif (self.power * self.level) < (oponente.power * oponente.level):
                        print(f"Seu {oponente.name} venceu a batalha!!")
        
        if self.type == "Grass":
            match oponente.type:
                case "Fire":
                    if ((self.power/2) * self.level) < (oponente.power * oponente.level):
                        print(f"Seu {oponente.name} venceu a batalha!!")
                    else:
                        print(f"Seu {oponente.name} perdeu a batalha!!")
                case "Water":
                    if (self.power * self.level) > ((oponente.power/2) * oponente.level):
                        print(f"Seu {oponente.name} perdeu a batalha!!")
                    else:
                        print(f"Seu {oponente.name} venceu a batalha!!")
                case "Water":
                    if (self.power * self.level) == (oponente.power * oponente.level):
                        print("A batalha foi considerada empate!!")
                    elif (self.power * self.level) > (oponente.power * oponente.level):
                        print(f"Seu {oponente.name} perdeu a batalha!!")
                    elif (self.power * self.level) < (oponente.power * oponente.level):
                        print(f"Seu {oponente.name} venceu a batalha!!")
                                                                        
                    
pokemon1 = Pokemon("Charmander","Fire", 30, 20)
pokemon2 = Pokemon("Squirtle","Water", 30, 20)
pokemon3 = Pokemon("Bulbassaur","Grass", 30, 20)

lista_pokemon = [pokemon1,pokemon2,pokemon3]

print("Escolha o pokemon que deseja iniciar!")
print('''Escolha entre: 
  Squirtle 
  Bulbassaur 
  Charmander ''')

str_pokemon = input("Escolha seu pokemon inicial:")
match str_pokemon.upper():
    case "Charmander":
        str_pokemon = pokemon1
    case "Squirtle":
        str_pokemon = pokemon2
    case "Bulbassaur":
        str_pokemon = pokemon3
    case _:
        print("O Pokemon escolhido é inválido! Escolha um inicial válido.")



random.choice(lista_pokemon).battle(str_pokemon)