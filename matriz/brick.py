import pygame

"""CLASSE DO OBSTACULO INQUEBRAVEL"""
class Brick (pygame.sprite.Sprite):
        def __init__(self, img,x,y,largura,altura):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x*largura
            self.rect.y = y*altura