import pygame
import math
import numpy as np
import time
import sys

def draw_epicycloid(screen, width, height):
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Epicycloid parameters
    R = 100  # Radius of the fixed circle
    r = 30   # Radius of the rolling circle

    clock = pygame.time.Clock()

    points = []
    pointsII = []
    pointsIII = []

    angle = np.arange(0, 800, 0.01)

    newShape = 13
    AngleShift = 0.3

    TimeExceeded = False
    start_time = time.time()
    end_time = 0
    execution_time = 0 

    TimeLimit = 19
    increment = 0

    RotatingSize = 0

    running = True

    colors = [
        # (0, 0, 0),       # black
        (255, 255, 255), # white
        (255, 0, 0),     # red
        (0, 255, 0),     # green
        (0, 0, 255),     # blue
        (255, 255, 0),   # yellow
        (0, 255, 255),   # cyan
        (255, 0, 255),   # magenta
        (128, 128, 128), # gray
        (64, 64, 64),    # dark gray
        (192, 192, 192), # light gray
        (255, 165, 0),   # orange
        (128, 0, 128),   # purple
        (165, 42, 42),   # brown
        (255, 192, 203), # pink
        (0, 255, 0),     # lime
        (0, 128, 128),   # teal
        (0, 0, 128),     # navy
        (255, 215, 0),   # gold
        (192, 192, 192), # silver
        (128, 0, 0),     # maroon
        (128, 128, 0)    # olive
    ]
    TotalColors = len(colors) - 1

    for theta in (angle):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not running:
            break 

        if theta == newShape or TimeExceeded:
            if RotatingSize % 2 == 0:
                r += 2 
            else:
                r += 3

            points = []
            pointsII = []
            pointsIII = []

            newShape += theta

            AngleShift += 0.3

            start_time = time.time()
            TimeExceeded = False

            increment += 0.25
            TimeLimit += increment

            if RotatingSize==TotalColors:
                RotatingSize = 0
            else:
                RotatingSize += 1

            pygame.time.delay(3000)
            
            
        screen.fill(black)

        x = (R + r) * math.cos(theta) - r * math.cos((R + r) / r * theta)
        y = (R + r) * math.sin(theta) - r * math.sin((R + r) / r * theta)

        xII = (R + (r)) * math.cos(theta+AngleShift) - (r) * math.cos((R + (r)) / (r) * (theta))
        yII = (R + (r)) * math.sin(theta+AngleShift) - (r) * math.sin((R + (r)) / (r) * (theta))

        xIII = (R + (r)) * math.cos(theta+(2*AngleShift)) - (r) * math.cos((R + (r)) / (r) * (theta))
        yIII = (R + (r)) * math.sin(theta+(2*AngleShift)) - (r) * math.sin((R + (r)) / (r) * (theta))

        points.append((int(width / 2 + x), int(height / 2 + y)))
        pointsII.append((int(width / 2 + xII), int(height / 2 + yII)))
        pointsIII.append((int(width / 2 + xIII), int(height / 2 + yIII)))

        end_time = time.time()
        if (end_time - start_time) >= TimeLimit:
            TimeExceeded = True

        
        # Draw all points
        for point, p2, p3 in zip(points,pointsII,pointsIII):
            pygame.draw.circle(screen, colors[RotatingSize], point, 2)
            pygame.draw.circle(screen, colors[RotatingSize], p2, 2)
            pygame.draw.circle(screen, colors[RotatingSize], p3, 2)

        pygame.display.flip()
        clock.tick(200)




def koch_snowflake(screen,TimeLimit, InitialLength, TotalIterations, Massage ):
    
    clock = pygame.time.Clock()

    # Initial scale and position
    scale = 1.0

    # Define points using NumPy arrays
    StartingPoint = 300

    XPoints = np.array([StartingPoint, StartingPoint + InitialLength, StartingPoint + InitialLength / 2, StartingPoint])
    YPoints = np.array([StartingPoint, StartingPoint, StartingPoint + InitialLength * np.sqrt(3) / 2, StartingPoint])

    points = np.vstack((XPoints, YPoints)).T 
    
    screen.fill((0, 0, 0)) 
    AQUA_BLUE = (127, 255, 212)
    pygame.draw.lines(screen, AQUA_BLUE, True, points, 5) 
    pygame.display.flip()
    clock.tick(60)
    pygame.time.delay(1500)

    running = True
    dragging = False

    ChangeInX = 0
    ChangeInY = 0 
    for iteration in range(TotalIterations):
        NewXPoints = []
        NewYPoints = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    mouse_x, mouse_y = event.pos

                    # Create a bounding box around the points
                    StartingWidth = min(XPoints) - 10
                    EndingWidth = max(XPoints) + 10
                    StartingHeight = min(YPoints) - 10
                    EndingHeight = max(YPoints) + 10

                    if mouse_x >= StartingWidth and mouse_x <= EndingWidth:
                        if mouse_y >= StartingHeight and mouse_y <= EndingHeight:
                            dragging = True

                            CopyX = XPoints.copy()
                            CopyY = YPoints.copy()

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    CurrMouseX, CurrMouseY = event.pos

                    ChangeInX = CurrMouseX - mouse_x
                    ChangeInY = CurrMouseY - mouse_y
                    
                    XPoints = CopyX + ChangeInX
                    YPoints = CopyY + ChangeInY

        if not running:
            break 


        TotalPoints = len(XPoints)
        for index in range(1,TotalPoints):
            NewXPoints.append(XPoints[(index-1)])
            NewYPoints.append(YPoints[(index-1)])

            NewX1 =  (XPoints[(index-1)] + ( (XPoints[index] - XPoints[(index-1)] ) / 3 ) )
            NewY1 =  (YPoints[(index-1)] + ( (YPoints[index] - YPoints[(index-1)] ) / 3 ) ) 

            NewX2 =  ( XPoints[(index-1)] + (( XPoints[index] - XPoints[(index-1)]) / 2 ) + ((YPoints[index]  - YPoints[(index-1)] ) * np.sqrt(3) / 6) )
            NewY2 =  ( YPoints[(index-1)] + (YPoints[index]  - YPoints[(index-1)] ) / 2 - (XPoints[index] - XPoints[(index-1)]) * np.sqrt(3) / 6 )

            NewX3 = ( XPoints[(index-1)] + ( (XPoints[index] - XPoints[(index-1)] ) * (2/3)))
            NewY3 = ( YPoints[(index-1)] + ( (YPoints[index] - YPoints[(index-1)] ) * (2/3)))
        
            NewXPoints.extend([NewX1, NewX2, NewX3])
            NewYPoints.extend([NewY1, NewY2, NewY3])

        NewXPoints.append(XPoints[0])
        NewYPoints.append(YPoints[0])

        XPoints = np.array(NewXPoints)
        YPoints = np.array(NewYPoints)
            
        points = np.vstack((XPoints, YPoints)).T 
        screen.fill((0, 0, 0))  
        pygame.draw.lines(screen, AQUA_BLUE, True, points, 3)

        pygame.display.flip()
        clock.tick(60)
        pygame.time.delay(550)


    font = pygame.font.SysFont(None, 48)
    screen.fill((0, 0, 0))  
    text_surface = font.render(Massage, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.delay(1000)

    running = True
    ChangeInX = 0
    ChangeInY = 0


    start_time = time.time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    mouse_x, mouse_y = event.pos

                    # Create a bounding box around the points
                    StartingWidth = min(XPoints) - 10
                    EndingWidth = max(XPoints) + 10
                    StartingHeight = min(YPoints) - 10
                    EndingHeight = max(YPoints) + 10

                    if mouse_x >= StartingWidth and mouse_x <= EndingWidth:
                        if mouse_y >= StartingHeight and mouse_y <= EndingHeight:
                            dragging = True

                            CopyX = XPoints.copy()
                            CopyY = YPoints.copy()

                elif event.button == 4:  # Scroll up
                    scale *= 1.1

                    XPoints *= scale 
                    YPoints *= scale
                elif event.button == 5:  # Scroll down
                    scale /= 1.1

                    XPoints *= scale 
                    YPoints *= scale

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    CurrMouseX, CurrMouseY = event.pos

                    ChangeInX = CurrMouseX - mouse_x
                    ChangeInY = CurrMouseY - mouse_y
                    
                    XPoints = CopyX + ChangeInX
                    YPoints = CopyY + ChangeInY

            if not running:
                break

        scale = 1

        points = np.vstack((XPoints, YPoints)).T
        screen.fill((0, 0, 0))
        pygame.draw.lines(screen, AQUA_BLUE, True, points, 2)

        pygame.display.flip()
        clock.tick(60)

        end_time = time.time()
        if (end_time - start_time) >= TimeLimit:
            running = False



def main():
    # Initialize PyGame
    pygame.init()

    # Screen dimensions
    width, height = 1366, 768
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Epicycloid Wallpaper')

    
    draw_epicycloid(screen, width, height)

        
    InitialLength = 200
    TotalIterations = 8
    massage = "Rendering complete!!!"
    playTime = 10

    koch_snowflake(screen, playTime, InitialLength, TotalIterations, massage )

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()