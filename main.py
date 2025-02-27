import pygame
from helpers import * 
from buttons import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.image_post import * 
from classes.TextPost import *

def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    noa_kirel = ImagePost("yosi", "Israel", "Noa kirel",'Images/noa_kirel.jpg')
    ronaldo = ImagePost("Ori", "New york", "Ronaldo", 'Images/ronaldo.jpg')

    text_post = TextPost("Moshe", "Tel aviv", "Show",'Hello World my name is matan i live in ashdod', (235, 52, 232),(28, 19,28))

    posts = [noa_kirel, ronaldo, text_post]

    current_index = 0
    current_post = posts[current_index]

    
    # TODO: add a post here

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if mouse_in_button(like_button, pos):
                        current_post.add_like()
                        pass
                    elif mouse_in_button(comment_button, pos):
                        comment = read_comment_from_user()
                        current_post.add_comment(comment)
                        pass
                    elif mouse_in_button(click_post_button, pos):
                        current_index = (current_index + 1) % len(posts)
                        current_post = posts[current_index ]
                        current_post.reset_comments_display_index()
                        

                    elif mouse_in_button(view_more_comments_button, pos):
                        current_post.view_more_comments()

                    
                    # If the mouse is pressed within the button, then run the function
                    
        

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()

    
main()
