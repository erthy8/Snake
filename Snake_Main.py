import pygame
import random

pygame.init()

# color values
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
background_colour = (0, 0, 0)

# Define the dimensions of
# screen object(width,height)
snakeSpeed = 10
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Set the caption of the screen
pygame.display.set_caption('Snake')

# Fill the background colour to the screen
screen.fill(background_colour)

# Message function
font_style = pygame.font.SysFont("comicsansms", 20)
score_font = pygame.font.SysFont("arial", 20)


def message(text, color):
    msg = font_style.render(text, True, color)
    screen.blit(msg, [width / 2 - 250, height / 2 - 30])


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])


def snakeDraw(snakeBlocks):
    screen.fill(background_colour)
    for i in snakeBlocks:
        pygame.draw.rect(screen, blue, [i[0], i[1], 10, 10])


# Update the display using flip
pygame.display.flip()


# game loop
def gameLoop():
    # snake values
    length = 1
    x = width / 2 - 10
    y = height / 2 - 20
    x_change = 0
    y_change = 0
    snakeBlocks = []

    # apple values
    appX = random.randrange(0, width, 10)
    appY = random.randrange(0, height, 10)

    running = True
    endScreen = False
    while running:
        # for loop through the event queue
        while endScreen:
            message("YOU LOST!!!!!! Press 1 to quit. Press 2 to play again", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        running = False
                        endScreen = False
                    elif event.key == pygame.K_2:
                        gameLoop()

        for event in pygame.event.get():
            print("x: ", x, " y: ", y, " Length: ", length)

            if event.type == pygame.QUIT:
                running = False

            # Making snake move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 10

        # Bounds check
        if x < 0 or x > width or y < 0 or y > height:
            endScreen = True
        for i in snakeBlocks[:-1]:
            if i[0] == x and i[1] == y:
                endScreen = True

        # Win Check
        if length > width*height:
            message("You Win! Press 1 to quit and 2 to play again", white)

        # Change Movement
        x += x_change
        y += y_change
        headPos = [x, y]
        snakeBlocks.append(headPos)

        # Apple Eating
        if x == appX and y == appY:
            length += 1
            appX = random.randrange(0, width, 10)
            appY = random.randrange(0, height, 10)

        # Draw Things
        screen.fill(background_colour)
        # Snake
        if len(snakeBlocks) > length:
            del snakeBlocks[0]

        snakeDraw(snakeBlocks)
        # Apple
        pygame.draw.rect(screen, red, [appX, appY, 10, 10])

        Your_score(length-1)

        pygame.display.update()
        clock.tick(snakeSpeed)

    pygame.quit()
    quit()


gameLoop()
