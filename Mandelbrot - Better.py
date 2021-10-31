import os, pygame.gfxdraw, pygame, math, random, time
pygame.init()

DisplayX, DisplayY = 1920,1080
win = pygame.display.set_mode((DisplayX, DisplayY))
pygame.display.set_caption("Mandelbrot Set in Pygame")

RealRange = 3.5
RealBase = (2/3)*RealRange
ImaginaryRange = (DisplayY/DisplayX)*RealRange
ImaginaryBase = ImaginaryRange/2

Black = (0,0,0)
Blue  = (70,70,255)
Red   = (250,90,90)

x,y = 0,0
Running = True
Done = False

def DiscoverImaginaryComponents(x,y):
    a = (x/DisplayX)*RealRange+-RealBase
    b = (y/DisplayY)*ImaginaryRange-ImaginaryBase
    return a,b

def ReturnSquared(a,b):
    new_a = a*a - b*b
    new_b = 2*a*b
    return new_a,new_b

def Iteration(i):
    c = i[0],i[1]
    a,b = 0,0
    global NumberIterations
    isWithinSet = True
    for NumberIterations in range(IterationSize):
        new_a,new_b = ReturnSquared(a,b)
        a = new_a+c[0]
        b = new_b+c[1]
        if a*a + b*b > 4:
            isWithinSet = False
            break
    return isWithinSet

PerFrame = 1000
IterationSize = 250
Power = 0.3
MaxRGB = 255
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    for n in range(PerFrame):
        isWithinSet = Iteration(DiscoverImaginaryComponents(x,y))
        if isWithinSet:
            pygame.gfxdraw.pixel(win, x, y, Black)
        else:
            if NumberIterations != 0:
                scale = (NumberIterations/IterationSize)**Power
            else:
                scale = (0.8/IterationSize)**Power
            pygame.gfxdraw.pixel(win, x, y, (MaxRGB*scale,MaxRGB*scale,MaxRGB))
        x += 1
        if x > DisplayX - 1:
            x = 0
            y += 1
            if y > DisplayY - 1:
                Done = True
                break
    pygame.display.update()
    if Done:
        break
while Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = False
pygame.quit()








