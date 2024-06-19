import pygame
import math
import numpy as np
import time

def draw_epicycloid(screen, colors, width, height, R, r, theta, angle_shift, points, pointsII, pointsIII, rotating_size):
    x = (R + r) * math.cos(theta) - r * math.cos((R + r) / r * theta)
    y = (R + r) * math.sin(theta) - r * math.sin((R + r) / r * theta)

    xII = (R + r) * math.cos(theta + angle_shift) - r * math.cos((R + r) / r * theta)
    yII = (R + r) * math.sin(theta + angle_shift) - r * math.sin((R + r) / r * theta)

    xIII = (R + r) * math.cos(theta + 2 * angle_shift) - r * math.cos((R + r) / r * theta)
    yIII = (R + r) * math.sin(theta + 2 * angle_shift) - r * math.sin((R + r) / r * theta)

    points.append((int(width / 2 + x), int(height / 2 + y)))
    pointsII.append((int(width / 2 + xII), int(height / 2 + yII)))
    pointsIII.append((int(width / 2 + xIII), int(height / 2 + yIII)))

    for point, p2, p3 in zip(points, pointsII, pointsIII):
        pygame.draw.circle(screen, colors[rotating_size], point, 2)
        pygame.draw.circle(screen, colors[rotating_size], p2, 2)
        pygame.draw.circle(screen, colors[rotating_size], p3, 2)

def main():
    # Initialize PyGame
    pygame.init()

    # Screen dimensions
    width, height = 1366, 768
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Epicycloid Wallpaper')

    # Colors
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

    new_shape = 13
    angle_shift = 0.3

    time_exceeded = False
    start_time = time.time()
    time_limit = 18
    increment = 0

    rotating_size = 0

    running = True

    colors = [
        (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
        (0, 255, 255), (255, 0, 255), (128, 128, 128), (64, 64, 64),
        (192, 192, 192), (255, 165, 0), (128, 0, 128), (165, 42, 42),
        (255, 192, 203), (0, 255, 0), (0, 128, 128), (0, 0, 128),
        (255, 215, 0), (192, 192, 192), (128, 0, 0), (128, 128, 0)
    ]
    total_colors = len(colors) - 1

    for theta in angle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not running:
            break

        if theta == new_shape or time_exceeded:
            if rotating_size % 2 == 0:
                r += 2
            else:
                r += 3

            points = []
            pointsII = []
            pointsIII = []

            new_shape += theta

            angle_shift += 0.3

            start_time = time.time()
            time_exceeded = False

            increment += 0.4
            time_limit += increment

            if rotating_size == total_colors:
                rotating_size = 0
            else:
                rotating_size += 1

            pygame.time.delay(3000)

        screen.fill(black)
        draw_epicycloid(screen, colors, width, height, R, r, theta, angle_shift, points, pointsII, pointsIII, rotating_size)

        end_time = time.time()
        if (end_time - start_time) >= time_limit:
            time_exceeded = True

        pygame.display.flip()
        clock.tick(200)

    pygame.quit()

if __name__ == "__main__":
    main()