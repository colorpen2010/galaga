import pygame,nadpis,random,knopka,enemycl


class Marshutizator():
    def __init__(self,color= [2,2,2]):
        self.timer_number = pygame.event.custom_type()
        pygame.time.set_timer(self.timer_number, 2)
        self.color=color
        self.n1=nadpis.Nadpis(0,0,'build a way mode: ON',15,[255,254,7])
        self.rector=[]
        self.crygi=[]
        self.points=[]
        self.numb=[]
        self.button=knopka.Knopka(10,20,'custom/Entity/кнопка.png',self.ryletka)
        self.test = enemycl.Enemyc('original/enemy/butterfly_red1.png', 'original/enemy/butterfly_red2.png', 200, 10,
                                   500,
                                   200, 200, 10, 15)

        self.ryletka()
        self.ryletka()
        self.ryletka()
        self.vidilenie=None
        self.test_flying()

    def draw(self,screen):
        for j in self.crygi:
            pygame.draw.circle(screen,[255,255,255],j,3)
        for o in self.rector:
            if self.vidilenie is o:
                pygame.draw.rect(screen,[0,255,0],o)
            elif self.rector[0] is o:
                pygame.draw.rect(screen,[0,0,255],o)
            else:
                pygame.draw.rect(screen, [120, 30, 59], o)
        for i in self.numb:
            i.risyi(screen)
        self.n1.risyi(screen)
        self.button.risyem(screen)
        self.test.paint(screen)
    def ryletka(self):
        self.rectik=pygame.rect.Rect(random.randint(10,580),random.randint(10,580),10,10)
        self.rector.append(self.rectik)
        self.points.append([self.rectik.centerx,self.rectik.centery])
        self.numb.append(nadpis.Nadpis(self.rectik.x + 4, self.rectik.y + 4, str(self.rector.index(self.rectik)), 20, [255, 0, 0]))
        self.test_flying()

    def clear_spisok(self):
        if len(self.crygi) != 0:
            self.crygi.clear()

    def test_flying(self):
        self.clear_spisok()
        self.test.plavniy_fly_tohcy(self.rector[0].topleft, self.points)
        while self.test.plavniy_tourch_yes_or_no == True:
            self.test.plavniy_flying_tohcy()
            self.crygi.append([self.test.rect.centerx, self.test.rect.centery])
    def control_center(self,events):
        self.button.event(events)
        self.test.toolgun(events)
        for o in events:


            if o.type==pygame.KEYUP and o.key == pygame.K_KP_ENTER:
                self.test_flying()
            if o.type == pygame.KEYUP and o.key == pygame.K_s:
                self.clear_spisok()
                self.test.plavniy_fly_tohcy(self.rector[0].topleft, self.points)

            if self.test.plavniy_tourch_yes_or_no==True and o.type==self.timer_number:
                self.crygi.append([self.test.rect.centerx,self.test.rect.centery])

            for j in self.rector:

                if o.type == pygame.MOUSEBUTTONUP and j.collidepoint(o.pos):
                    self.vidilenie=j
                    self.vidilenie_numbera=self.numb[self.rector.index(j)]
                    self.vidilenie_point=self.points[self.rector.index(j)]
            if o.type==pygame.KEYUP and o.key == pygame.K_KP_PERIOD:
                self.vidilenie=None
                self.vidilenie_numbera = None
                self.vidilenie_point = None
            if o.type==pygame.KEYUP and o.key == pygame.K_KP_0:
                self.rector.clear()
                self.numb.clear()
                self.points.clear()
                self.vidilenie=None
                self.vidilenie_numbera = None
                self.vidilenie_point = None
                self.clear_spisok()



            if self.vidilenie is not None:
                if o.type == pygame.KEYDOWN and o.key== pygame.K_KP8:
                    self.vidilenie.y-=5
                    self.vidilenie_numbera.y-=5
                    self.vidilenie_point[1]-=5
                    self.test_flying()
                if o.type == pygame.KEYDOWN and o.key== pygame.K_KP2:
                    self.vidilenie.y+=5
                    self.vidilenie_numbera.y+=5
                    self.vidilenie_point[1] += 5
                    self.test_flying()
                if o.type == pygame.KEYDOWN and o.key== pygame.K_KP4:
                    self.vidilenie.x-=5
                    self.vidilenie_numbera.x-=5
                    self.vidilenie_point[0] -= 5
                    self.test_flying()
                if o.type == pygame.KEYDOWN and o.key== pygame.K_KP6:
                    self.vidilenie.x+=5
                    self.vidilenie_numbera.x+=5
                    self.vidilenie_point[0] += 5
                    self.test_flying()



