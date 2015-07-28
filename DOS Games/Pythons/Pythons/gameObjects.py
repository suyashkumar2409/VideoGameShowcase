import pygame
import random

"""   *********************** Colors ************************* """
black = (0, 0, 0)
green = (0, 155, 0)
red = (255, 0, 0)
white = (255, 255, 255)


## **************************** Class definitions ************************ ##
class GameWindow:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height

    def setWidth(self, width=800):
        self.width = width

    def getWidth(self):
        return self.width

    def setHeight(self, height=800):
        self.height = height

    def getHeight(self):
        return self.height

    def getDimensions(self):
        return (self.width, self.height)


class Snake:
    # The variables are
    # posx, posy
    # speed
    # width, height
    # horizontalMovement, verticalMovement
    # color
    # length
    # snakeList


    def __init__(self, posx, posy, **kwargs):
        self.properties = dict(posx=posx, posy=posy, angle=270, speed=20, width=20, height=20, horizontalMovement=0,verticalMovement=0, length=5, snakeList=[], increaseLength=2,snakehead=pygame.image.load("Image Assets/largesnakehead.png"),snakebody=pygame.image.load("Image Assets/largesnakebody.png"),snaketail=pygame.image.load("Image Assets/largesnaketail.png"))
        for k, v in kwargs:
            self.properties[k] = v




    def setPosition(self, pos):
        self.properties['posx'] = pos[0]
        self.properties['posy'] = pos[1]

    def setXpos(self, val):
        self.properties['posx'] = val

    def getXpos(self):
        return self.properties['posx']

    def setYpos(self, val):
        self.properties['posy'] = val

    def getYpos(self):
        return self.properties['posy']

    def setSpeed(self, speed):
        self.properties['speed'] = speed

    def getSpeed(self):
        return self.properties['speed']

    def setSize(self, width=20, height=20):
        self.properties['width'] = width
        self.properties['height'] = height

    def getWidth(self):
        return self.properties['width']

    def getHeight(self):
        return self.properties['height']

    def setHorizontalMovement(self, val):
        self.properties['horizontalMovement'] = val

    def setVerticalMovement(self, val):
        self.properties['verticalMovement'] = val

    def getHorizontalMovement(self):
        return self.properties['horizontalMovement']

    def getVerticalMovement(self):
        return self.properties['verticalMovement']

    def getLength(self):
        return self.properties['length']

    def setLength(self, val):
        self.properties['length'] = val

    def incrementLength(self):
        self.properties['length'] += self.properties['increaseLength']

    ## The main functions
    def movementChange(self, event):
        if event.key == pygame.K_LEFT:
            if(self.getHorizontalMovement()!=1):
                self.setHorizontalMovement(-1)
                self.setVerticalMovement(0)
                return True
        elif event.key == pygame.K_RIGHT:
            if(self.getHorizontalMovement()!=-1):
                self.setHorizontalMovement(1)
                self.setVerticalMovement(0)
                return True
        elif event.key == pygame.K_UP:
            if(self.getVerticalMovement()!=1):
                self.setVerticalMovement(-1)
                self.setHorizontalMovement(0)
                return True
        elif event.key == pygame.K_DOWN:
            if(self.getVerticalMovement()!=-1):
                self.setVerticalMovement(1)
                self.setHorizontalMovement(0)
                return True

        return False

    def movementUpdate(self, window):
        temp = [0, 0, 0, 0, 0]
        if self.getHorizontalMovement() == 1:
            self.setXpos(self.getXpos() + self.getSpeed())
            temp[2]=270
        elif self.getHorizontalMovement() == -1:
            self.setXpos(self.getXpos() - self.getSpeed())
            temp[2]=90
        elif self.getVerticalMovement() == 1:
            self.setYpos(self.getYpos() + self.getSpeed())
            temp[2]=180
        elif self.getVerticalMovement() == -1:
            self.setYpos(self.getYpos() - self.getSpeed())
            temp[2]=0
        else:
            if(len(self.properties['snakeList'])>=1):
                return

        temp[3]=self.getHorizontalMovement()
        temp[4]=self.getVerticalMovement()
        self.setXpos(self.getXpos() % window.getWidth())
        self.setYpos(self.getYpos() % window.getHeight())

        temp[0] = self.getXpos()
        temp[1] = self.getYpos()

        self.properties['snakeList'].append(temp)


        if len(self.properties['snakeList']) > self.getLength():
            del self.properties['snakeList'][0]

        if(self.properties['horizontalMovement']!=0 or self.properties['verticalMovement']!=0):
            for each in self.properties['snakeList'][:-1]:
                if each[0] == self.getXpos() and each[1] == self.getYpos():
                    print ("hoolah")
                    return True

        return False


    def render(self, displayObject):

        if len(self.properties['snakeList'])>=2:
            temp = self.properties['snakeList'][1][2]
        else:
            temp = self.properties['snakeList'][0][2]

        addx=0
        addy=0


        displayObject.blit(pygame.transform.rotate(self.properties['snaketail'],temp),(self.properties['snakeList'][0][0]+addx, self.properties['snakeList'][0][1]+addy))        # draw tail


        for coordinate in self.properties['snakeList'][1:-1]:
            displayObject.blit(pygame.transform.rotate(self.properties['snakebody'],coordinate[2]),(coordinate[0]+addx,coordinate[1]+addy))        # draw body




        displayObject.blit(pygame.transform.rotate(self.properties['snakehead'],self.properties['snakeList'][-1][2]),(self.properties['snakeList'][-1][0],self.properties['snakeList'][-1][1]))        # draw body



class Food:
    def __init__(self, snake, wallwidth, window, posx=0, posy=0, width=20, height=20):
        self.properties = dict(posx=posx, posy=posy, width=width, height=height)
        self.place(snake, wallwidth, window)

    def setPosition(self, *args):
        self.properties['posx'] = args[0]
        self.properties['posy'] = args[1]

    def getPosition(self):
        return self.properties['posx'], self.properties['posy']

    def getWidth(self):
        return self.properties['width']

    def place(self, snake, wallwidth, window):
        self.properties['posx'] = round(
            random.randrange(2*wallwidth, (window.getWidth() - 3*wallwidth))/20.0) * 20


        self.properties['posy'] = round(
            random.randrange(2*wallwidth, (window.getHeight()- 3*wallwidth))/20.0) * 20

    def render(self, displayObject):
        pygame.draw.rect(displayObject, red,
                         [self.properties['posx'], self.properties['posy'], self.getWidth(), self.getWidth()])
