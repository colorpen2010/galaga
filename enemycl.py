import pygame,settings


class Enemyc:
    def __init__(self, pyt,pyt2, x, y):
        self.image2 = pygame.image.load(pyt2)
        self.image = pygame.image.load(pyt)
        self.image2=pygame.transform.scale(self.image2,[self.image2.get_width()*settings.dounler,self.image2.get_height()*settings.dounler])
        self.image=pygame.transform.scale(self.image,[self.image.get_width()*settings.dounler,self.image.get_height()*settings.dounler])
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

    def paint(self, screen: pygame.Surface):
        screen.blit(self.image, [self.rect.x, self.rect.y])
        screen.blit(self.image2, [self.rect.x, self.rect.y+100])

    def paint_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect, 3)

    def moveright(self):
        self.rect.x+=5
