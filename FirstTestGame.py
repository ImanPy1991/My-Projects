import turtle
import pygame , sys
import pygame.locals as Game_Local
import pygame.event as Game_Events

turtle.setup(width=800 , height=650 , startx=300, starty=40)
turtle.reset()
turtle.hideturtle()
turtle.speed(0)
turtle.bgcolor("#111")
c = x = 0

colors = [
#reddish colors
(1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
#orangey colors
(1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
#yellowy colors
(1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
#greenish colors
(0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
#blueish colors
(0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
]

while x < 1000:
    color = colors[int(c)]
    turtle.color(color)
    turtle.forward(x)
    turtle.right(120)
    x = x + 1
    c= c + 0.1

turtle.exitonclick()

import pip as PIP
#--------------------------------------------------------

pygame.init ()

windowGame = pygame.display.set_mode ( (700 , 700 ) )
pygame.display.set_caption ( 'Iman Game TOKEN' )



RectX = 130
RectY = 10
SpeedX = 0
SpeedY = 0


class Bazikon ( object ):
    def __init__(self):
        self.rect = pygame.Rect ( 40 , 40 , 20 , 20 )

    def moving(self , SelfX , SelfY):
        if SelfX != 0:
            self.MoveItMoveIt ( SelfX , 0 )
        if SelfY != 0:
            self.MoveItMoveIt ( 0 , SelfY )

    def MoveItMoveIt(self , SelfX , SelfY):
        self.rect.x += SelfX
        self.rect.y += SelfY

        for wall in walls:
            if self.rect.colliderect ( wall.rect ):
                if SelfX > 0:
                    self.rect.right = wall.rect.left
                if SelfX < 0:
                    self.rect.left = wall.rect.right
                if SelfY > 0:
                    self.rect.bottom = wall.rect.top
                if SelfY < 0:
                    self.rect.top = wall.rect.bottom


class divar ( object ):
    def __init__(self , position):
        walls.append ( self )
        self.rect = pygame.Rect ( position[0] , position[1] , 20 , 20 )


walls = []
bazikon = Bazikon()
s = pygame.time.Clock ()

level = [

    "DDD DDDDDD DDDDDDD DDDD DDDDDDDDD   DDDDD DDD",
    "D                                 D",
    "D                                 D",
    "D                                 D",
    "D                                 D",
    "D       D       DDDDDDD           D",
    "D       D       DDDDDDD           D",
    "D     D         DDDDDDD           D",
    "D       D       DDDDDDD           D",
    "D                   D             D",
    "D                   D             D",
    "D                   D             D",
    "D        DDDDDDDDDDDD             D",
    "D         D D D  D       D",
    "D                                D",
    "D            G             D",
    "D                     D",
    "DDD D DDDD DDDD DDD DDDDDDDD",

]

x = y = 0
for row in level:
    for col in row:
        if col == "D":
            divar((x , y))
        if col == "G":
            TheEnd_rect = pygame.Rect ( x , y , 13 , 13 )
        x += 20
    y += 20
    x = 0


while True:
    s.tick ( 3000 )
    # pygame.draw.rect(windowGame, (80, 180, 80), (RectX, RectY, 30, 50))

    for event in Game_Events.get ():
        # if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_LEFT:
        # SpeedX = -3
        # if event.key == pygame.K_RIGHT:
        # SpeedX = 3
        if event.type == Game_Local.QUIT:
            pygame.quit ()
            sys.exit ()

    dokme = pygame.key.get_pressed ()
    if dokme[pygame.K_LEFT]:
        bazikon.moving ( -1 , 0 )
    if dokme[pygame.K_RIGHT]:
        bazikon.moving ( 1 , 0 )
    if dokme[pygame.K_UP]:
        bazikon.moving ( 0 , -1 )
    if dokme[pygame.K_DOWN]:
        bazikon.moving ( 0 , 1 )

    if bazikon.rect.colliderect(TheEnd_rect):
        pygame.quit()

    windowGame.fill ( (0 , 20 , 0) )
    MyFont = pygame.font.Font ( 'fonts/calibri.ttf' , 40 )
    text = MyFont.render ( 'Its my Text .. respect it' , True , (100 , 45 , 35) )
    windowGame.blit(text,(100,80))

    for wall in walls:
        pygame.draw.rect ( windowGame , (160 , 160 , 160) , wall.rect )
        pygame.draw.rect ( windowGame , (5 , 25 , 180) , TheEnd_rect)
        pygame.draw.rect ( windowGame , (240 , 5 , 5) , bazikon.rect )
    pygame.display.update ()
