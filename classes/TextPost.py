import pygame

from classes.Post import Post
from constants import *
from helpers import screen, from_text_to_array, center_text


class TextPost(Post):
    def __init__(self, username, location, description, text, text_color, background_color):
        super().__init__(username, location, description)
        self.text = from_text_to_array(text)#
        self.text_color = text_color
        self.background_color = background_color


    def display(self):
        pygame.draw.rect(screen, self.background_color, pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))
        counter = 0
        for text in self.text:
            text_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold = False)
            text_to_display = text_font.render(text, True, self.text_color)
            text_position = center_text(len(self.text), text_to_display, counter)#
            counter += 1
            screen.blit(text_to_display, text_position)
        super().display()
           