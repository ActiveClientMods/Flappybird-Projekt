import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height))

#define game variables
ground_scroll = 0
scroll_speed = 4
center_horizontal = int(screen_height / 2)
center_vertical = int(screen_width / 2)

#load images
bg = pygame.image.load('images/bg.png')
ground_img = pygame.image.load('images/ground.png')


class Bird(pygame.sprite.Sprite):
    def init(self, x, y):
        pygame.sprite.Sprite.init(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'images/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):

        #handle the animation
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]


bird_group = pygame.sprite.Group()

flappy = Bird(100, center_horizontal)

bird_group.add(flappy)


run = True
while run:

    clock.tick(fps)
    pygame.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))

    #draw background
    screen.blit(bg, (0,0))

    bird_group.draw(screen)
    bird_group.update()

    #draw and scroll the ground
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()

pygame.quit()