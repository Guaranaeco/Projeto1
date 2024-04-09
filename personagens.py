import random
escolha = 0
class Player:
    def __init__(self, nome, vida_max, vida, ataque, level, exp_level) -> None:
        self.nome = nome
        self.vida_max = vida_max
        self.vida = vida
        self.ataque = ataque
        self.level = level
        self.exp_level = exp_level
    
    def __str__(self) -> str:
        return('-- Status base --\n'
               f'Nome: {self.nome}\n'
               f'Vida: {self.vida}\n'
               f'Ataque: {self.ataque}')
    
    def battle(self, inimigo):
        inimigo.vida -= self.ataque
        print(f'Você ataca o inimigo! \n'
              f'Com um corte limpo, você causa {jogador.ataque} de dano!\n'
              f'Vida atual do inimigo {inimigo.vida}')
 
class Monstro:
    def __init__(self, nome, vida_max, vida, ataque, level, exp) -> None:
        self.nome = nome
        self.vida_max = vida_max
        self.vida = vida
        self.ataque = ataque
        self.level = level
        self.exp = exp


def menu():
    while True:
        print('1 - Atacar'
              '2 - Status')
        if escolha == 1:
            jogador.battle(monstro_escolhido)
            break
        elif escolha == 2:
            print(jogador)
            break
        else:
            print("Opção inválida!")

def heroi():
    print(arqueiro)
    print(barbaro)
    print(mago)
    

arqueiro = Player('Legolas', 20, 20, 8, 1, 20)
barbaro = Player('Conan', 30, 30, 5, 1, 20)
mago = Player('Donald', 15, 15, 11, 1, 20)

# Criação de instâncias de monstros
morcego = Monstro('morcego', 5, 5, 2, 1, 5)
esqueleto = Monstro('esqueleto', 20, 20, 5, 1, 10)
minotauro = Monstro('minotauro', 30, 30, 10, 1, 20)

# Lista de monstros com suas porcentagens de aparecimento
lista_itens = [[morcego, 0.01], [esqueleto, 0.50], [minotauro, 0.49]]
nomes, porcentagens = zip(*lista_itens)
monstro_escolhido = random.choices(nomes, weights=porcentagens, k=1)[0]

heroi()