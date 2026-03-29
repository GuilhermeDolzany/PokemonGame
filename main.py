import pickle
import os
import time

from pokemon import *
from characters import *

SAVE_FILE = "database.db"


def clear_screen():
    # Limpa o terminal no Windows (cls) ou Linux/Mac (clear)
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_starter_pokemon(player):
    clear_screen()
    print(" Professor Carvalho: ")
    print(f" 'Olá {player.name}, chegou a hora de escolher o parceiro da sua jornada!'\n")

    pikachu = ElectricPokemon("Pikachu", level=1)
    charmander = FirePokemon("Charmander", level=1)
    squirtle = WaterPokemon("Squirtle", level=1)

    print("📜 OPÇÕES DE INICIAIS:")
    print(f"  1 » {pikachu}")
    print(f"  2 » {charmander}")
    print(f"  3 » {squirtle}\n")

    while True:
        choice = input("👉 Digite o número do seu Pokemon: ")

        if choice == "1":
            player.catch(pikachu); break
        elif choice == "2":
            player.catch(charmander); break
        elif choice == "3":
            player.catch(squirtle); break
        else:
            print("[ ! ] Escolha inválida. Tente novamente.")

    time.sleep(2)


def save_game(player):
    try:
        with open(SAVE_FILE, "wb") as file:
            pickle.dump(player, file)
            time.sleep(1)
    except Exception as error:
        print("\n[ ! ] Erro crítico ao salvar o jogo:", error)
        time.sleep(2)


def load_game():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "rb") as file:
                player = pickle.load(file)
                print("✅ Carregamento concluído com sucesso!")
                time.sleep(1)
                return player
        except Exception:
            print("[ ! ] Save corrompido ou erro ao carregar. Iniciando novo jogo...")
            time.sleep(2)
    return None


if __name__ == "__main__":
    clear_screen()
    print("════════════════════════════════════════")
    print("        🔴 POKEMON RPG TERMINAL ⚪      ")
    print("════════════════════════════════════════\n")
    time.sleep(1)

    player = load_game()

    if not player:
        name = input("👉 Para começar, digite o seu nome: ")
        player = Player(name)

        clear_screen()
        print(f"🌍 Bem-vindo ao mundo Pokemon, {player.name}!")
        print("Sua missão é capturar criaturas, treinar e se tornar o Campeão.\n")
        time.sleep(2)

        choose_starter_pokemon(player)

        clear_screen()
        print(" Professor Carvalho: ")
        print(" 'Seu rival, Gary, quer testar suas habilidades!'")
        time.sleep(2)

        gary = Enemy(name="Gary", pokemons=[WaterPokemon("Squirtle", level=1)])
        player.battle(gary)
        save_game(player)

    # LOOP PRINCIPAL DO JOGO
    while True:
        clear_screen()
        print("════════════════════════════════════════")
        print(f" MENU PRINCIPAL | Treinador: {player.name}")
        print("════════════════════════════════════════")
        print(" [ 1 ] 🚶 Explorar a grama alta")
        print(" [ 2 ] ⚔️  Lutar com um treinador aleatório")
        print(" [ 3 ] 🎒 Ver minha Pokedex")
        print(" [ 4 ] 🏥 Ir ao Centro Pokemon (Curar)")
        print(" [ 0 ] 💾 Salvar e Sair")
        print("════════════════════════════════════════")

        choice = input("\n👉 O que deseja fazer? ")

        if choice == "0":
            save_game(player)
            print("\nFechando o jogo... Até a próxima!")
            break

        elif choice == "1":
            clear_screen()
            player.explore()
            input("\n[ Pressione ENTER para continuar ]")
            save_game(player)

        elif choice == "2":
            clear_screen()
            random_enemy = Enemy()
            player.battle(random_enemy)
            input("\n[ Pressione ENTER para continuar ]")
            save_game(player)

        elif choice == "3":
            clear_screen()
            player.show_pokemons()
            player.show_money()
            input("\n[ Pressione ENTER para voltar ao menu ]")

        elif choice == "4":
            clear_screen()
            print("🏥 CENTRO POKEMON")
            time.sleep(1)
            player.heal_all_pokemons()
            input("\n[ Pressione ENTER para voltar ao menu ]")

        else:
            print("\n[ ! ] Opção inválida.")
            time.sleep(1)