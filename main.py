import random
from messages import display_messages
import time

print("Iniciando o Projeto!")
time.sleep(3)

while True:
    resposta = input ('Deseja Receber um Conselho? S/N: ?')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()