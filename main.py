import personagens
print('Aventura teste começando...')
print(f'Em uma breve história, monstros aos redores da cidade estão atacando os viajantes, e você foi contratado para elimina-los e chegar até o lider deles, comece!\n')


print(f'Bem vindo! {personagens.jogador.nome}\nVocê está prestes a sair da cidade, qual direção deseja tomar?\n'
      '1 - Leste\n'
      '2 - Norte\n')
escolha = int(input('Opção desejada: '))

if escolha == 1:
    print('Você se aproxima do portão leste e sente cheiro de sangue...\n')
    print('O cheiro se intensifica conforme você anda... barulhos estranhos...\n')
    print(f'Você encontrou um {personagens.monstro_escolhido.nome}, o que fazer?\n')
    print('1 - Atacar\n'
            '2 - Fugir\n')
    escolha = int(input('Opção desejada: '))
    if escolha == 1:
        personagens.jogador.battle(personagens.monstro_escolhido)
    