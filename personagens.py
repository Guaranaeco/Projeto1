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
        while True:
            print('1. Ataque\n'
                  '2. Fugir\n')
            escolha = int(input('Escolha: '))
            if escolha == 1:
                dano = randint(int(self.ataque * 0.60), int(self.ataque * 1.20))
                inimigo.vida -= dano
                if inimigo.vida > 0:
                    print(f'Você ataca o inimigo! {inimigo.nome} \n'
                        f'Com um corte limpo, você causa {dano} de dano!\n'
                        f'Vida atual do inimigo {cor(96,inimigo.vida)}')
                if inimigo.vida <= 0:
                    inimigo.vida = 0
                    print(f'Vida atual do inimigo {cor(96, inimigo.vida)}')
                    print(f'Você matou o {inimigo.nome}')
                    self.exp += inimigo.exp
                    print(f'Você recebeu {self.exp} de exp')
                    if self.exp >= self.exp_max:
                        sobra_xp = self.exp - self.exp_max
                        self.level += 1
                        print('Parabéns, você upou!')
                        self.ataque += 3
                        self.vida += 10
                        self.vida_max += 10
                        self.exp_max = int(self.exp_max * 1.50)
                        self.exp = sobra_xp
            elif escolha == 2:
                    fugir = randint(0, 10)
                    print(fugir)
                    if fugir > 8:
                        print('Você fugiu!')
                        break
                    else:
                        print(f'Você tenta fugir... mas o {inimigo.nome} te ataca pelas costas')
                        self.vida -= inimigo.ataque 
                        print(f'Você sofreu {inimigo.ataque} de dano!\nVida:{self.vida}')


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



# Instâncias de classes
arqueiro = Player('Legolas', 20, 20, 8, 1, 0, 20)
barbaro = Player('Conan', 30, 30, 5, 1, 0, 20)
mago = Player('Donald', 15, 15, 11, 1, 0, 20)


# Lista de monstros com suas porcentagens de aparecimento (Até o momento)
def monstro_aleatorio():
    lista_itens = [[Monstro('morcego', 5, 5, 2, 1, 22), 0.50], [Monstro('esqueleto', 20, 20, 5, 1, 22), 0.40], [Monstro('minotauro', 30, 30, 10, 1, 22), 0.10]]
    nomes, porcentagens = zip(*lista_itens)
    return choices(nomes, weights=porcentagens, k=1)[0]


