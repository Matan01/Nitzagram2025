from constants import *
import pygame
from helpers import screen

class Comment:
    def _init_(self, text, index):
        self.text = text
        self.index = index

    def display(self, position):
        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        comment_surface = font.render(self.text, True, (0, 0, 0))
        screen.blit(comment_surface, (50, 100 + position * 30))
