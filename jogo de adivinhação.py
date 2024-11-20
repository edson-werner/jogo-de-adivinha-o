from random import randint
import pygame
from time import sleep
cont = 0
tentativas = 1
cores = {'azul':'\033[1;34m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'vazio':'\033[m'}
print(f'{cores['azul']}Sejá bem vindo: \nVamos jogar???{cores['vazio']} ')

print('Precione ENTER para continuar!')
pygame.init()
pygame.mixer.music.load('abertura.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
input()
pygame.quit()

print(f'{cores['azul']}Defina a dificuldade:{cores['vazio']}')
print(f'{cores['verde']}Facíl, de 0 a 5:Digite 1{cores['vazio']}')
print(f'{cores['amarelo']}Médio, de 0 a 10:Digite 2{cores['vazio']}')
print(f'{cores['vermelho']}Difícil, de 0 a 20:Digite 3{cores['vazio']}')
dificuldade = input('Qual dificuldade você escolheu:')

print('Vou pensar em um número e você tenta acertar:\n')

while True:
    if cont == 0 or resposta == numero_computador:
        cont += 1
        if dificuldade == '1':
            numero_computador = randint(0, 5)
        elif dificuldade == '2':
            numero_computador = randint(0, 10)
        elif dificuldade == '3':
            numero_computador = randint(0, 20)
        else:
            print('ERRO  \nDigite apenas as opções acima !')

    resposta = int(input('Digite o numero que você acha que eu pensei:'))
    

    print('procesando...', end="", flush=True)
    sleep(1)
    print("\r           \r", end="", flush=True)

    if resposta == numero_computador:
        print(f'{cores['verde']}Parabêns, você acertou com {tentativas}!!! {cores['vazio']}')
        print('Precione ENTER para tentar novamente!')
        pygame.init()
        pygame.mixer.music.load('ganhador.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.7)
        input()

    else:
        tentativas += 1
        if resposta < numero_computador:
            dica = "o numero é maior"
        else:
            dica = "o numero é menor"
        print(f'{cores['vermelho']}Você errou!!!{cores['vazio']}\nO número verdadeiro é {dica}')
        print("aperte ENTER para tentar novamente")
        pygame.init()
        pygame.mixer.music.load('perder.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.9)
        input()

