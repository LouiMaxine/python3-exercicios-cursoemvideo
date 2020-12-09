#FUPQ abra e reproduza o áudio de um arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load('t.mp3')
pygame.mixer.music.play()
pygame.event.wait()