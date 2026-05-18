import pygame


pygame.init()


janela = pygame.display.set_mode([1000, 600])
pygame.display.set_caption('Ping Pong')


BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)


raquete1_x, raquete1_y = 50, 225
raquete2_x, raquete2_y = 950, 225
bola_x, bola_y = 250, 250


velocidade_raquete = 1.7
velocidade_bola_x, velocidade_bola_y = 0.7, 0.4


raquete_largura, raquete_altura = 20, 100
bola_largura, bola_altura = 20, 20


placar1 = 0
placar2 = 0
font = pygame.font.SysFont(None, 50)

# Função para desenhar elementos
def desenhar():
    # Limpa a tela
    janela.fill(PRETO)
        
        
    # INSERIR A FORMAÇÃO DOS PERSONAGENS -  RAQUETE E BOLA 

    pygame.draw.rect(janela, BRANCO, (raquete1_x, raquete1_y, raquete_largura, raquete_altura))
    pygame.draw.rect(janela, BRANCO, (raquete2_x, raquete2_y, raquete_largura, raquete_altura))
    pygame.draw.ellipse(janela, BRANCO, (bola_x, bola_y, bola_largura, bola_altura))

    # PLACAR

    placar_texto = font.render(f'{placar1} - {placar2}', True, BRANCO)
    janela.blit(placar_texto, (500,20))


# EXPLICAÇÃO DO CÓDIGO


LOOP = True

while LOOP:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            LOOP = False

    # Movimentação das raquetes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y < 500 - raquete_altura:
        raquete1_y += velocidade_raquete
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 500 - raquete_altura:
        raquete2_y += velocidade_raquete

 
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    if bola_y <= 0 or bola_y >= 500 - bola_altura:
        velocidade_bola_y = -velocidade_bola_y

   
    if (raquete1_x < bola_x < raquete1_x + raquete_largura) and (raquete1_y < bola_y < raquete1_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x
    if (raquete2_x < bola_x < raquete2_x + raquete_largura) and (raquete2_y < bola_y < raquete2_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x

 
    if bola_x <= 30:  
        placar2 += 1
        bola_x, bola_y = 500, 300 
        velocidade_bola_x = -velocidade_bola_x  
    if bola_x >= 980 - bola_largura:  
        placar1 += 1
        bola_x, bola_y = 500, 300  
        velocidade_bola_x = -velocidade_bola_x  

   
    desenhar()

  
    pygame.display.update()


pygame.quit()
