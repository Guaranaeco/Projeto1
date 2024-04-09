import personagens
import random
import sys
import time

def palavra(texto, intervalo=0.05):
    for char in texto:
        if char == '\n':
            sys.stdout.write(char)
        else:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(intervalo)

palavra('Aventura teste começando...')
palavra(f'Em uma breve história, monstros aos redores da cidade estão atacando os viajantes, e você foi contratado para elimina-los e chegar até o lider deles, comece!\n')

palavra('Bem vindo! \nVocê está prestes a sair da cidade, qual direção deseja tomar?\n'
      '1 - Leste\n'
      '2 - Norte\n')
escolha = int(input('Opção desejada: '))

if escolha == 1:
    palavra('Você se aproxima do portão leste e sente cheiro de sangue...\n')
    palavra('O cheiro se intensifica conforme você anda... barulhos estranhos...\n')
    palavra(f'Você encontrou um {personagens.monstro_escolhido.nome}, o que fazer?\n')
    palavra('1 - Atacar\n'
            '2 - Fugir\n')
    escolha = int(input('Opção desejada: '))
    if escolha == 1:
        personagens.jogador.battle(personagens.monstro_escolhido)
    