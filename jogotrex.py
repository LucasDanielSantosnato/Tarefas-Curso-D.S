import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 900
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo do T-Rex")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Carrega a imagem do T-Rex
trex_imagem = pygame.image.load('trex.png')
TAMANHO_TREX = trex_imagem.get_rect().size
POSICAO_TREX = [150, ALTURA - TAMANHO_TREX[1] - 10]
VELOCIDADE_PULO = -50  # Velocidade do pulo
GRAVIDADE = 0.2  # Diminuição da gravidade
trex_rect = pygame.Rect(POSICAO_TREX[0], POSICAO_TREX[1], TAMANHO_TREX[0], TAMANHO_TREX[1])

# Parâmetros dos obstáculos
OBSTACULO_LARGURA = 30
OBSTACULO_ALTURA = 80
OBSTACULO_VELOCIDADE = 6
obstaculos = []

# Configurações do jogo
FPS = 60
clock = pygame.time.Clock()
pulo = False
pulo_vivo = False
score = 0


def criar_obstaculo():
    # Obstáculos fixos na parte inferior da tela
    altura = ALTURA - OBSTACULO_ALTURA - 0
    return pygame.Rect(LARGURA, altura, OBSTACULO_LARGURA, OBSTACULO_ALTURA)


def desenhar_tela():
    TELA.fill(PRETO)
    TELA.blit(trex_imagem, trex_rect.topleft)
    for obs in obstaculos:
        pygame.draw.rect(TELA, BRANCO, obs)
    pygame.display.flip()


def main():
    global pulo, pulo_vivo, trex_rect, obstaculos, score

    # Loop principal do jogo
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not pulo_vivo:
                    pulo = True
                    pulo_vivo = True

        # Movimento do T-Rex
        if pulo:
            trex_rect.y += VELOCIDADE_PULO
            if trex_rect.y <= ALTURA - TAMANHO_TREX[1] - 200:
                pulo = False
        else:
            if trex_rect.y < ALTURA - TAMANHO_TREX[1] - 10:
                trex_rect.y += GRAVIDADE

        # Atualiza obstáculos
        for obs in obstaculos:
            obs.x -= OBSTACULO_VELOCIDADE
        if len(obstaculos) == 0 or obstaculos[-1].x < LARGURA - 500:
            obstaculos.append(criar_obstaculo())
        if obstaculos[0].x < -OBSTACULO_LARGURA:
            obstaculos.pop(0)
            score += 1

        # Verifica colisões
        for obs in obstaculos:
            if trex_rect.colliderect(obs):
                print(f"Game Over! Score: {score}")
                pygame.quit()
                return

        # Desenha na tela
        desenhar_tela()

        # Atualiza a tela
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
