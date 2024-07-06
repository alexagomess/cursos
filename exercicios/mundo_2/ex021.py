#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3

import pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(13)
