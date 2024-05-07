import pygame
import random
import time
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
window_width, window_height = 1440, 800
WIN = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bug Collector_TM_IS2200")
pygame.mixer.init()

# Load background image
BackGround = pygame.image.load("PageSTART.png")
GRAY = (200, 200, 200)
font = pygame.font.Font(None, 32)

# Draw Graph on screen
def draw(surface, text, x1=19, y1=17, color=GRAY):
    surface.blit(BackGround, (0, 0))

    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x1, y1))

    for x in range(0, window_width, 30):
        pygame.draw.line(surface, GRAY, (x, 5), (x, window_height))
    for y in range(0, window_height, 30):
        pygame.draw.line(surface, GRAY, (5, y), (window_width, y))
    pygame.display.update()

#Create an input field for the players to type into
def input_field(events, current_text):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                current_text = current_text[:-1]
            elif event.key == pygame.K_RETURN:
                print("What a beautiful", current_text, "!")
            else:
                current_text += event.unicode
    return current_text

#Create a class for Buttons 
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False # Initialize clicked state

    def draw(self, surface):
        #mouse position
        Mouse_Pos = pygame.mouse.get_pos()
        #Check if mouse clicked the button
        if self.rect.collidepoint(Mouse_Pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                #Print Bug fact
                draw(surface, "Bees are winged insects closely related to wasps and ants, known for their roles in pollination and, in the case of the best-known bee species, the western honey bee, for producing honey. Did you know that bees dance to communicate?", 60,200,GRAY)
            if pygame.mouse.get_pressed()[0] == 0: 
                self.clicked = False
        #Draw Button to screen
        surface.blit(self.image, self.rect)

#Main (Handles most/all events)
def main():
    run = True
    clock = pygame.time.Clock()
    input_text = ""

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Clear the screen and draw background and lines
        draw(WIN, "")

        # Handle input field
        input_text = input_field(pygame.event.get(), input_text)

        # Draw input field prompt and text
        draw(WIN, "What bug did you collect?", 50, 50)
        draw(WIN, input_text, 50, 100)

        #Load in the bug
        if "Bee" in input_text:
            Bee_Button = Button(100,200, pygame.image.load("Bee.png").convert_alpha())
            Bee_Button.draw(WIN)

        # Limit frame rate to 30 FPS
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
