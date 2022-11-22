# Programa que mostra profissões que não existem (provavelmente)

import random

p_palavra = ['Ceifador', 'Pungilista', 'Barbeador', 'Cabeleireiro', 'Jogador', 'Artista', 'Sapateador', 'Instrutor', 'Telefonista', 'Açougueiro', 'Maquiador', 'Motorista']
prep = ' de '
u_palavra = ['bolas', 'camarão', 'gorila', 'barbante', 'queijo', 'sapato', 'garrafa', 'janela']

print(random.choice(p_palavra) + prep + random.choice(u_palavra))