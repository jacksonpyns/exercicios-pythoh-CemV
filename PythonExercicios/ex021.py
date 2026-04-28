import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('Digite algo para encerrar a música: ')
pygame.event.wait()