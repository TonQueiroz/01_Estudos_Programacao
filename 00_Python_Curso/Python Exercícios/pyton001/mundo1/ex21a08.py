#Programa para Reproduzir um audio mp3

import pygame

pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
input('Digite enter para pausar')
pygame.event.wait()

pygame.mixer.music.pause()
print('fim')