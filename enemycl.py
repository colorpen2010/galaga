import pygame,settings

pygame.init()


class Enemyc:
    def __init__(self, pyt, pyt2, x, y, timer, timer2, xmove_l, xmove_r, move_speed):
        self.timer_number = pygame.event.custom_type()
        self.timer_number2 = pygame.event.custom_type()
        pygame.time.set_timer(self.timer_number, timer)
        pygame.time.set_timer(self.timer_number2, timer2)
        self.gothere = True
        self.move_speed = move_speed

        self.image2 = pygame.image.load(pyt2)
        self.image = pygame.image.load(pyt)
        self.image2 = pygame.transform.scale(self.image2, [self.image2.get_width() * settings.dounler,
                                                           self.image2.get_height() * settings.dounler])
        self.image = pygame.transform.scale(self.image, [self.image.get_width() * settings.dounler,
                                                         self.image.get_height() * settings.dounler])
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.krilia_yes_or_no = True
        self.povorot_yes_or_no= True

        self.image_povoroter1 = self.image
        self.image_povoroter2 = self.image2

        self.move_rect = pygame.rect.Rect(xmove_l, y, xmove_r - xmove_l, self.rect.height)

    def paint(self, view, screen: pygame.Surface):
        self.screen = screen
        if view == False:
            if self.krilia_yes_or_no == True:
                screen.blit(self.image, [self.rect.x, self.rect.y])
            if self.krilia_yes_or_no == False:
                screen.blit(self.image2, [self.rect.x, self.rect.y])
        if view == True:
            if self.krilia_yes_or_no == True:
                screen.blit(self.image_povoroter1, [self.rect.x, self.rect.y])
            if self.krilia_yes_or_no == False:
                screen.blit(self.image_povoroter2, [self.rect.x, self.rect.y])

    def rect_remaker(self):
        if self.krilia_yes_or_no == True:
            if self.povorot_yes_or_no==True:
                ycenter = self.rect.centery
                xcenter = self.rect.centerx
                self.rect.width = self.image_povoroter1.get_width()
                self.rect.height = self.image_povoroter1.get_height()
                self.rect.centerx = xcenter
                self.rect.centery = ycenter
            if self.povorot_yes_or_no == False:
                ycenter = self.rect.centery
                xcenter = self.rect.centerx
                self.rect.width = self.image.get_width()
                self.rect.height = self.image.get_height()
                self.rect.centerx = xcenter
                self.rect.centery = ycenter
        if self.krilia_yes_or_no == False:
            if self.povorot_yes_or_no == True:
                ycenter = self.rect.centery
                xcenter = self.rect.centerx
                self.rect.width = self.image_povoroter2.get_width()
                self.rect.height = self.image_povoroter2.get_height()
                self.rect.centerx = xcenter
                self.rect.centery = ycenter
            if self.povorot_yes_or_no == False:
                ycenter = self.rect.centery
                xcenter = self.rect.centerx
                self.rect.width = self.image_povoroter1.get_width()
                self.rect.height = self.image_povoroter1.get_height()
                self.rect.centerx = xcenter
                self.rect.centery = ycenter

    def paint_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect, 3)
        pygame.draw.rect(screen, [0, 255, 0], self.move_rect, 3)

    def moving(self, number):
        self.animation_krilia()
        self.rect_remaker()
        self.rect.x += number

    def animation_krilia(self):

        self.krilia_yes_or_no = not self.krilia_yes_or_no

    def toolgun(self, events):
        for o in events:
            if o.type == self.timer_number:
                self.modelier()
            # if o.type == self.timer_number2:
            #     self.povorot(True, False, 45)

    def modelier(self):
        if self.gothere == True:
            self.moving(-self.move_speed)
        elif self.gothere == False:
            self.moving(self.move_speed)
        if self.rect.right >= self.move_rect.right:
            self.gothere = True
            self.rect.right = self.move_rect.right
        elif self.rect.left <= self.move_rect.left:
            self.gothere = False
            self.rect.left = self.move_rect.left

    def povorot(self, ygol):
        ycenter = self.rect.centery
        xcenter = self.rect.centerx
        self.image_povoroter1 = pygame.transform.rotate(self.image, ygol)
        self.image_povoroter2 = pygame.transform.rotate(self.image2, ygol)
        self.rect.width = self.image_povoroter1.get_width()
        self.rect.height = self.image_povoroter1.get_height()
        self.rect.width = self.image_povoroter2.get_width()
        self.rect.height = self.image_povoroter2.get_height()
        self.rect.centerx = xcenter
        self.rect.centery = ycenter