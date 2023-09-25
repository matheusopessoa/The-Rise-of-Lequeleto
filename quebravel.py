import pygame


class Bloco_q (pygame.sprite.Sprite):
    def __init__(self,x,y,largura,altura):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/quebravel.png')
        self.image = pygame.transform.scale(self.image, (largura, altura))
        self.rect = self.image.get_rect()
        self.rect.x = x*largura
        self.rect.y = y*altura

        self.x = x
        self.y = y 