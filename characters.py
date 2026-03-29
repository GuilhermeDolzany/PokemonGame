import random
import time
from pokemon import *

NAMES = ["João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego", "Patrícia", "Marcelo", "Gustavo", "Gerônimo",
         "Gary"]


def get_random_pokemon():
    choices = [
        FirePokemon("Charmander"), FirePokemon("Flareon"), FirePokemon("Charmeleon"),
        ElectricPokemon("Pikachu"), ElectricPokemon("Raichu"),
        WaterPokemon("Squirtle"), WaterPokemon("Magikarp"),
    ]
    return random.choice(choices)


class Character:
    def __init__(self, name=None, pokemons=None, money=100):
        self.name = name if name else random.choice(NAMES)
        self.pokemons = pokemons if pokemons is not None else []
        self.money = money

    def __str__(self):
        return self.name

    def show_pokemons(self):
        if self.pokemons:
            print(f"\n🎒 POKEDEX DE {self.name.upper()}:")
            for index, pokemon in enumerate(self.pokemons):
                print(f"  {index} » {pokemon}")
            print("-" * 30)
        else:
            print(f"\n[ ! ] {self} não tem nenhum pokemon no momento.")

    def choose_pokemon(self):
        if self.pokemons:
            available_pokemons = [p for p in self.pokemons if p.health > 0]
            if not available_pokemons:
                return None

            chosen_pokemon = random.choice(available_pokemons)
            print(f" {self} enviou {chosen_pokemon.name} para a batalha!")
            return chosen_pokemon
        return None

    def show_money(self):
        print(f"💰 Saldo Atual: $ {self.money}")

    def earn_money(self, amount):
        self.money += amount
        print(f"🎉 VITÓRIA! Você ganhou $ {amount}!")
        self.show_money()

    def heal_all_pokemons(self):
        for pokemon in self.pokemons:
            pokemon.heal()
        print(f"\n[ + ] Enfermeira Joy curou todos os seus Pokemons!")
        print("[ + ] Eles estão prontos para a próxima aventura.\n")

    def battle(self, enemy):
        print("\n" + "═" * 40)
        print(f"⚔️  BATALHA INICIADA: {self} VS {enemy}!")
        print("═" * 40)
        time.sleep(1)

        enemy_pokemon = enemy.choose_pokemon()
        my_pokemon = self.choose_pokemon()

        if not my_pokemon:
            print(f"\n[ ! ] {self} não tem pokemons saudáveis para lutar! Você fugiu.")
            return

        if not enemy_pokemon:
            print(f"\n[ ! ] {enemy} não tem pokemons. Você venceu por W.O.!")
            return

        time.sleep(1)

        while my_pokemon.health > 0 and enemy_pokemon.health > 0:
            print("\n" + "-" * 40)
            print(f"TURNO DE BATALHA")
            print(f"» Seu {my_pokemon.name}: {my_pokemon.health} HP")
            print(f"» Inimigo {enemy_pokemon.name}: {enemy_pokemon.health} HP")
            print("-" * 40)
            time.sleep(1.5)

            # Seu ataque
            win = my_pokemon.attack(enemy_pokemon)
            if win:
                print("\n" + "★" * 40)
                print(f"🏆 {self.name.upper()} VENCEU A BATALHA!")
                print("★" * 40)
                self.earn_money(enemy_pokemon.level * 100)
                break

            time.sleep(1.5)

            # Ataque inimigo
            enemy_win = enemy_pokemon.attack(my_pokemon)
            if enemy_win:
                print("\n" + "☠️" * 15)
                print(f"❌ {self.name.upper()} PERDEU A BATALHA...")
                print("☠️" * 15)
                break

            time.sleep(1.5)

        print("\nRetornando os pokemons para as pokebolas...")
        time.sleep(2)


class Player(Character):
    type = "player"

    def catch(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"✨ GOTCHA! {pokemon.name} foi capturado com sucesso!")

    def choose_pokemon(self):
        self.show_pokemons()
        if self.pokemons:
            available_indices = [i for i, p in enumerate(self.pokemons) if p.health > 0]
            if not available_indices:
                print("[ ! ] Todos os seus pokemons estão desmaiados!")
                return None

            while True:
                choice = input("\n👉 Escolha o seu Pokemon pelo número (ou aperte Enter para cancelar): ")
                if choice == "": return None

                try:
                    choice = int(choice)
                    if choice in available_indices:
                        chosen_pokemon = self.pokemons[choice]
                        print(f"\n➡️  {chosen_pokemon.name}, EU ESCOLHO VOCÊ!!!")
                        return chosen_pokemon
                    else:
                        print("[ ! ] Escolha inválida ou o pokemon está desmaiado.")
                except ValueError:
                    print("[ ! ] Por favor, digite um número válido.")
        return None

    def explore(self):
        print("\n🚶 Você está caminhando pela grama alta...")
        time.sleep(2)

        if random.random() <= 0.4:
            wild_pokemon = get_random_pokemon()
            print(f"\n⚠️  ATENÇÃO! Um {wild_pokemon.name} selvagem apareceu! (Lvl {wild_pokemon.level})")

            choice = input("Deseja jogar uma Pokebola? (s/n): ").lower()
            if choice == "s":
                print("\nLançando Pokebola...")
                time.sleep(1)
                print("Tic...")
                time.sleep(1)
                print("Tac...")
                time.sleep(1)

                capture_chance = 0.5 + (0.01 * (50 - wild_pokemon.level))
                if random.random() <= capture_chance:
                    self.catch(wild_pokemon)
                else:
                    print(f"💨 Puff! {wild_pokemon.name} escapou da pokebola e fugiu para a floresta!")
            else:
                print("Você recuou silenciosamente.")
        else:
            print("Tudo tranquilo por aqui. Nenhum pokemon à vista.")


class Enemy(Character):
    type = "enemy"

    def __init__(self, name=None, pokemons=None):
        if not pokemons:
            random_pokemons = [get_random_pokemon() for _ in range(random.randint(1, 3))]
            super().__init__(name=name, pokemons=random_pokemons)
        else:
            super().__init__(name=name, pokemons=pokemons)