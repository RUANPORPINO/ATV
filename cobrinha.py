import pygame
import random
import sys

pygame.init()


largura = 600
altura = 400
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_capition('Jogo da Cobrinha')


verde = (0,255,0)
vermelho = (255,0,0)
preto = (0,0,0)

tamanho_celula = 20
velocidade = 15
relogio = pygame.time.Clock()

def gerar_comida():
    x_comida = random.randrange(0, largura, tamanho_celula)
    y_comida = random.randrange(0, altura, tamanho_celula)
    return x_comida, y_comida


def desenhar_cobrinha(cobra):
    for parte in cobra:
        pygame.draw.rect(tela,verde,(parte[0], parte[1], tamaho_celula, tamanho_celula))

def jogo():
    x = largura // 2
    y = altura // 2
    x_velocidade = 0
    y_velocidade = 0
    cobra = [(x,y)]
    comprimento_cobra = 1

    x_comida, y_comida = gerar_comida()

    while True:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_velocidade == 0:
                    x_velocidade = -tamanho_celula
                    y_velocidade = 0
                elif evento.key == pygame.K_RIGHT and x_velocidade == 0:
                    x_velocidade = tamanho_celula
                    y_velocidade = 0
                elif evento.key == pygame.K_UP and y_velocidade == 0:
                    y_velocidade = -tamanho_celula
                    x_velocidade = 0
                elif evento.key == pygame.K_DOWN and y_velocidade == 0:
                    y_velocidade = tamanho_celula
                    x_velocidade = 0

    x += x_velocidade
    y += y_velocidade