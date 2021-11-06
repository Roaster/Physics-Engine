import pygame
import random

black = 0,0,0
white = 255,255,255



class ball():

    def __init__(self, surface, color, center = (250,250), radius = 5):
        self.surface = surface
        self.color = color
        self.xPos = center[0]
        self.yPos = center[1]
        self.center = center
        self.radius = radius
        self.left = True

        self.xVelocity = random.randrange(-70,70)
        self.yVelocity = random.randrange(-70,70)

        self.acceleration = 1500
        self.xAcceleration = 0

    def display(self):
        pygame.draw.circle(self.surface, self.color, (self.xPos, self.yPos), self.radius)

    def jiggle(self):
        if self.left:
            self.xPos -= 20
            self.left = False
        else:
            self.xPos += 20
            self.left = True
    
    def updatePosition(self, dtime):
        self.yVelocity += self.acceleration * dtime
        self.xVelocity += self.xAcceleration * dtime
        self.xPos += (self.xVelocity * dtime + 0.5*self.acceleration*dtime**2)
        self.yPos += (self.yVelocity * dtime + 0.5*self.acceleration*dtime**2)


    def changeVelocity(self, xVelocity, yVelocity):
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

class player():

    def __init__(self, surface):
        self.height = 30
        self.width = 10
        self.surface = surface
        self.playerModel = pygame.Rect(0,100, 10, 50)
    
    def display(self):
        pygame.draw.rect(self.surface, white, self.playerModel)
    


class Game():

    
    def __init__(self, size = (600,400)):
        self.width = size[0]
        self.height = size[1]
        self.size = size

    def randomBalls(self, screen, count = 10):
        myBalls = []
        for i in range(count):
            xPos = random.uniform(0,600)
            yPos = random.uniform(0,400)
            myBalls.append(ball(screen,white,(xPos,yPos)))
        return myBalls

    def start(self):

        pygame.init()
        screen = pygame.display.set_mode(self.size)

        clock = pygame.time.Clock()
        fpsLimit = 60

        myBalls = self.randomBalls(screen, 10)
        player1 = player(screen)

        dt = 0
        while True:
            dtime = clock.tick(fpsLimit)
            dtime = dtime / 1000
            
            print(dtime)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            
            screen.fill(black)
            randomVelocity = False
       
                
            for ball in myBalls:
                ball.updatePosition(dtime)

                # move collision detection into ball class
                if ball.xPos <= 0: 
                    ball.xPos = 1
                    ball.changeVelocity(-ball.xVelocity*.8, ball.yVelocity)
                elif ball.xPos >= self.size[0]:
                    ball.xPos = self.size[0]
                    ball.changeVelocity(-ball.xVelocity*.8, ball.yVelocity)
                if ball.yPos <= 0: 
                    ball.changeVelocity(ball.xVelocity, -ball.yVelocity*.8)
                elif ball.yPos >= self.size[1]:
                   
                    ball.yPos = self.size[1]
                    ball.changeVelocity(ball.xVelocity, -ball.yVelocity*.8)
                ball.display()
            
            player1.display()
            pygame.display.flip()
    

x = Game()
x.start()