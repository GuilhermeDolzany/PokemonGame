# Pokemon RPG - Terminal Game

Um jogo de RPG em formato de texto (text-based) jogavel diretamente no terminal. Este projeto simula as mecanicas principais de uma jornada Pokemon, permitindo ao jogador explorar a grama alta, batalhar contra outros treinadores, capturar novas criaturas, ganhar experiencia e salvar o progresso da aventura.

## Inspiracao

Este jogo foi inspirado na franquia classica de jogos Pokemon (desenvolvida pela Game Freak / Nintendo). O objetivo do projeto foi capturar a essencia de escolher um companheiro inicial, gerenciar recursos (Vida, Dinheiro e Experiencia) e enfrentar batalhas em turnos, traduzindo essa experiencia visual para um ambiente puramente textual e logico.

## Conceitos Aplicados

Este projeto foi construido em Python e serve como uma excelente demonstracao de conceitos fundamentais de programacao:

* **Programacao Orientada a Objetos (POO):** Uso extensivo de classes, heranca e polimorfismo. Existe uma classe base `Pokemon` que e estendida por classes especificas como `FirePokemon` e `WaterPokemon`, cada uma com seus proprios comportamentos.
* **Persistencia de Dados:** Implementacao de um sistema de "Save" usando a biblioteca nativa `pickle` do Python, permitindo que os dados do jogador (dinheiro, inventario de pokemons, status e niveis) sejam salvos em um arquivo local e carregados em sessoes futuras.
* **Controle de Fluxo e Aleatoriedade:** Uso estruturado de loops para gerenciar os turnos das batalhas e o menu principal. O modulo `random` e usado para calcular variacoes de dano, chances de captura e encontros com pokemons selvagens.
* **Manipulacao de Terminal:** Uso de comandos do sistema operacional (`os.system`) e pausas de tempo (`time.sleep`) para limpar a tela e criar uma interface dinamica, simulando o ritmo de um jogo real.

## Como Executar o Jogo

### Pre-requisitos
* Ter o Python 3.x instalado em sua maquina.

### Passos para instalacao

1. Faca o clone deste repositorio:
   ```bash
   git clone [https://github.com/GuilhermeDolzany/PokemonGame.git](https://github.com/GuilhermeDolzany/PokemonGame.git)

2. Navegue ate o diretorio do projeto:

  cd PokemonGame

Execute o arquivo principal:

3. Execute o arquivo principal:

  python main.py

Nota: Dependendo do seu sistema, o comando pode ser python3 main.py)

Aviso para usuarios de IDEs (como PyCharm): Para que o recurso de limpar a tela funcione perfeitamente, e recomendado rodar o jogo pelo terminal integrado da IDE ou habilitar a opcao "Emulate terminal in output console" nas configuracoes de execucao.

### Como Jogar
Ao iniciar o jogo pela primeira vez, voce devera inserir seu nome e escolher seu Pokemon inicial. Apos uma batalha de introducao contra seu rival, voce tera acesso ao menu principal:

1 - Explorar: Caminhe pela grama alta. Voce tem a chance de encontrar pokemons selvagens e tentar captura-los com pokebolas.

2 - Batalhar: Enfrente o time de um treinador aleatorio. Vencer batalhas garante dinheiro e Pontos de Experiencia (XP) para o seu pokemon.

3 - Ver Pokedex: Verifique os pokemons que voce possui, seus niveis, HP atual e o progresso da barra de XP.

4 - Centro Pokemon: Cure completamente todos os pokemons do seu time.

0 - Salvar e Sair: Salva seu progresso atual no arquivo local database.db e fecha o jogo.

Sistema de Evolucao (Niveis)
Ao derrotar pokemons inimigos, seu pokemon ganha XP baseado no nivel do adversario. Ao acumular XP suficiente, o pokemon sobe de nivel, recuperando toda a vida e aumentando seu HP Maximo e Poder de Ataque.

Possiveis Melhorias (Roadmap)
Como este e um projeto base, ha muito espaco para expansao. Algumas ideias para atualizacoes futuras incluem:

Sistema de Tipos e Fraquezas: Implementar vantagens elementais (ex: ataques de Agua causam o dobro de dano em pokemons de Fogo).

Inventario de Itens: Criar uma loja onde o jogador possa comprar Pocoes (para usar durante as batalhas) e diferentes tipos de Pokebolas.

Sistema de Ginasios: Adicionar "Chefoes" fixos com times tematicos mais dificeis de derrotar.

Expansao da Pokedex: Adicionar mais especies de pokemons e criar uma lista de ataques variaveis para cada um.
