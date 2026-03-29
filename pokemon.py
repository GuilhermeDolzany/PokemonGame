import random


class Pokemon:
    def __init__(self, species, level=None, name=None):
        self.species = species
        self.level = level if level else random.randint(1, 100)
        self.name = name if name else species

        self.max_health = self.level * 10
        self.health = self.max_health
        self.attack_power = self.level * 5

    def __str__(self):
        return f"{self.name} (Lvl {self.level}) | HP: [{self.health}/{self.max_health}]"

    def attack(self, target_pokemon):
        attack_multiplier = random.uniform(0.8, 1.3)
        effective_attack = int(self.attack_power * attack_multiplier)

        target_pokemon.health -= effective_attack

        print(f"💥 DANO! {target_pokemon.name} perdeu {effective_attack} de HP!")

        if target_pokemon.health <= 0:
            target_pokemon.health = 0
            print(f"☠️  {target_pokemon.name} desmaiou e não pode mais lutar!")
            return True
        return False

    def heal(self):
        self.health = self.max_health


class ElectricPokemon(Pokemon):
    type = "eletrico"

    def attack(self, target_pokemon):
        print(f"⚡ {self.name} usa [Choque do Trovão] em {target_pokemon.name}!")
        return super().attack(target_pokemon)


class FirePokemon(Pokemon):
    type = "fogo"

    def attack(self, target_pokemon):
        print(f"🔥 {self.name} usa [Lança-Chamas] em {target_pokemon.name}!")
        return super().attack(target_pokemon)


class WaterPokemon(Pokemon):
    type = "água"

    def attack(self, target_pokemon):
        print(f"💧 {self.name} usa [Jato de Água] em {target_pokemon.name}!")
        return super().attack(target_pokemon)