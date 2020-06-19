import pygame
import random

running = True
background_color = (255, 255, 255)
(width, height) = (600, 800)
pipeheight = 370
restart = False

# init of pygame
pygame.init()
pygame.display.set_caption("Flappy Birds")

# class for pipes
class pipe():
    def __init__(self, screen, pipeheight = 300, pipex = 600):
        self.pipeheight = pipeheight
        self.pipex = pipex
        self.space = 150
        self.upperpipe = pygame.draw.rect(screen, (0,255,0), [self.pipex, 0, 40, self.pipeheight])
        self.lowerpipe = pygame.draw.rect(screen, (0,255,0), [self.pipex, self.pipeheight + self.space, 40, 800 - self.pipeheight])

    def redrawPipe(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), [self.pipex, 0, 40, self.pipeheight])
        pygame.draw.rect(screen, (255, 255, 255), [self.pipex, self.pipeheight + self.space, 40, 800 - self.pipeheight])
        if self.pipex > -40:
            self.pipex -= 2
        else:
            self.pipex = 600
            self.pipeheight = random.randint(300, 600)
        self.upperpipe = pygame.draw.rect(screen, (0, 255, 0), [self.pipex, 0, 40, self.pipeheight])
        self.lowerpipe = pygame.draw.rect(screen, (0, 255, 0), [self.pipex, self.pipeheight + self.space, 40, 800 - self.pipeheight])

#class for Bird
class bird(object):
    def __init__(self, screen):
        self.width = 20
        self.height = 30
        self.x = 140
        self.y = 280
        self.rect = pygame.draw.rect(screen, (0,0,0), [self.x, self.y, self.width, self.height])

    def redrawBird(self, screen, y):
        pygame.draw.rect(screen, (255,255,255), [self.x, self.y, self.width, self.height])
        self.y += y
        self.rect = pygame.draw.rect(screen, (0, 0, 0), [self.x, self.y, self.width, self.height])

    def deadBird(self, pipe):
        if self.y <= pipe.pipeheight or self.y + self.height >= pipe.pipeheight + pipe.space:
            return False
        else:
            return True

def gameOver(running, screen, sentence):
    if running == False:
        font = pygame.font.Font('odibeesans-regular.tff/OdibeeSans-Regular.ttf', 45)
        text = font.render(sentence, True, (0, 255, 0), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (width // 2, height // 2)
        screen.blit(text, textRect)
        pygame.display.update()
        pygame.time.wait(4000)

def displayScore(screen, number):
    font = pygame.font.Font("odibeesans-regular.tff/OdibeeSans-Regular.ttf", 40)
    text = font.render(str(number), True, (0,0,0), (190, 190, 190))
    scoreRect = text.get_rect()
    scoreRect.center = (width // 2, 40)
    pygame.draw.rect(screen, (190,190,190), [width//2 - 40, 17, 80, 46])
    screen.blit(text, scoreRect)

class main:
    screen = pygame.display.set_mode((width, height))
    screen.fill(background_color)
    bird1 = bird(screen)
    alive = True
    p1 = pipe(screen)
    p2 = pipe(screen, random.randint(300, 500), width + 340)
    pygame.display.update()
    timer = 0
    score = 0


    while running:
        pygame.time.Clock().tick(60)
        p1.redrawPipe(screen)
        p2.redrawPipe(screen)
        if bird1.y < height - bird1.height and timer == 0:
            bird1.redrawBird(screen, 2)
        else:
            bird1.redrawBird(screen, 0)
            timer -= 1

        if bird1.x + 20 == p1.pipex or (bird1.x >= p1.pipex and bird1.x <= p1.pipex + 40):
            running = bird1.deadBird(p1)
            gameOver(running, screen, "You hit a pipe")
        elif bird1.x + 20 == p2.pipex or (bird1.x >= p2.pipex and bird1.x <= p2.pipex + 40):
            running = bird1.deadBird(p2)
            gameOver(running, screen, "You hit a pipe")

        if bird1.x + 20 == p1.pipex + 2:
            score += 1
        if bird1.x + 20 == p2.pipex + 2:
            score += 1

        displayScore(screen, score)

        if ((bird1.y + bird1.height) == height):
            running = False
            gameOver(running, screen, "You hit the floor")
        pygame.display.update()

        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[pygame.K_SPACE] == 1:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird1.redrawBird(screen, -40)
                count = 10
        if running == False:
            pygame.quit()


main()
