from constants import *
import pygame
from helpers import screen

class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, position):
        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        comment_surface = font.render(self.text, True, (0, 0, 0))
        screen.blit(comment_surface, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + COMMENT_LINE_HEIGHT * position))
