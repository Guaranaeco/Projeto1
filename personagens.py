from random import randint, choices
escolha = 0

# Declarando classe principal do jogador
class Player:
    def __init__(self, nome, vida_max, vida, ataque, level, exp, exp_max) -> None:
        self.nome = nome
        self.vida_max = vida_max
        self.vida = vida
        self.ataque = ataque
        self.level = level
        self.exp = exp
        self.exp_max = exp_max
    
    # Status do jogador
    def __str__(self) -> str:
        return('-- Status base --\n'
          f'{cor(96,'Nome')}: {self.nome}\n'
               f'{cor(96,'Vida')}: {self.vida}/{self.vida_max}\n'
               f'{cor(96,'Ataque')}: {self.ataque}\n'
               f'{cor(96,'Level')} {self.level}\n'
               f'{cor(96,'EXP')}: {self.exp}/{self.exp_max}')
    
    # Método de batalha do jogador
    def battle(self, inimigo):
        dano = randint(int(self.ataque * 0.60), int(self.ataque * 1.20))
        inimigo.vida -= dano
        print(inimigo.nome)
        print(f'Você ataca o inimigo! \n'
              f'Com um corte limpo, você causa {dano} de dano!\n'
              f'Vida atual do inimigo {inimigo.vida}')
 
 # Declarando classe principal dos monstros
class Monstro:
    def __init__(self, nome, vida_max, vida, ataque, level, exp) -> None:
        self.nome = nome
        self.vida_max = vida_max
        self.vida = vida
        self.ataque = ataque
        self.level = level
        self.exp = exp

    # Método de batalha do monstro
    def battle(self, jogador):
        jogador.vida -= self.ataque
        print(f'Monstro ataca o jogador! \n'
              f'Com um corte limpo, você causa {self.ataque} de dano!\n'
              f'Vida atual do {jogador.nome} {jogador.vida}')

# Função para colorir texto.
def cor(cor, text):
    return f'\033[{cor}m{text}\033[m'


# Menu do jogador a cada jogada.
def menu():
    while True:
        print('1 - Atacar'
              '2 - Status')
        if escolha == 1:
            heroi.battle(monstro_escolhido)
            break
        elif escolha == 2:
            print(heroi)
            break
        else:
            print("Opção inválida!")

# Escolhendo personagem para a campanha
def heroi():
    print(arqueiro)
    print(barbaro)
    print(mago)
    escolha = int(input('Escolha seu herói: '))
    if escolha == 1:
        return arqueiro
    elif escolha == 2:
        return barbaro
    elif escolha == 3:
        return mago


# Instâncias de classes
arqueiro = Player('Legolas', 20, 20, 8, 1, 0, 20)
barbaro = Player('Conan', 30, 30, 5, 1, 0, 20)
mago = Player('Donald', 15, 15, 11, 1, 0, 20)

# Instâncias de monstros
morcego = Monstro('morcego', 5, 5, 2, 1, 5)
esqueleto = Monstro('esqueleto', 20, 20, 5, 1, 10)
minotauro = Monstro('minotauro', 30, 30, 10, 1, 20)

# Lista de monstros com suas porcentagens de aparecimento (Até o momento)
lista_itens = [[Monstro('morcego', 5, 5, 2, 1, 5), 0.33], [Monstro('esqueleto', 20, 20, 5, 1, 10), 0.33], [Monstro('minotauro', 30, 30, 10, 1, 20), 0.33]]
nomes, porcentagens = zip(*lista_itens)
monstro_escolhido = choices(nomes, weights=porcentagens, k=1)[0]


# TESTANDO

'''print(f'Você achou um {monstro_escolhido.nome}')
print('---------------')
print(jogador.battle(monstro_escolhido))
print('---------------')
print(monstro_escolhido.battle(jogador))
'''
# Imprimindo os status lado a lado
print(arqueiro)
for player in [barbaro, mago]:
    print(f'{player.nome}', end='  ')
    print(f'{player.vida}', end='  ')
    print(f'{player.vida_max}', end='  ')
    print(f'{player.ataque}', end='  ')
    print(f'{player.nome}', end='  ')