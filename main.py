import pygame
from personaje import Personaje
import constantes

pygame.init()

ancho = constantes.ANCHO_VENTANA
alto = constantes.ALTO_VENTANA

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mi juego en Pygame")

player = Personaje(50,50)

run = True

while run:

    player.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()