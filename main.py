import random

display_messages = [
    'Seja Feliz :)',
    'Fique Tranquilo, tudo vai acabar bem!'
]

while True:
    resposta = input ('Deseja Receber um Conselho? S/N: ?')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()