import pygame
import os
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 500
BIRD_SIDE_LENGTH = 50
PIPE_WIDTH = 70
PIPE_HEIGHT = 400

GRAVITY = 0.4

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



YELLOW = (255, 255, 0)
GREEN = (124,252,0)
FPS = 60

image_path = "FlappyBird\\flappy_bird_background.png" 

BACKGROUND = pygame.transform.scale(
    pygame.image.load(image_path), (SCREEN_WIDTH, SCREEN_HEIGHT)
)

DEAD = pygame.USEREVENT + 1

pygame.display.set_caption("Flappy Bird")

def handle_bird_movement(bird, bird_speed, pipes):
    bird.y = bird.y - bird_speed
     
    if bird.y <= -BIRD_SIDE_LENGTH or bird.y > SCREEN_HEIGHT - 80:
        pygame.event.post(pygame.event.Event(DEAD))
    
    for pipe in pipes:
        if pipe.colliderect(bird):
            pygame.event.post(pygame.event.Event(DEAD))
    
def handle_pipes(pipes, new_pipe_countdown):
    pipe_speed = 10
    for pipe in pipes:
        pipe.x = pipe.x - pipe_speed
    new_pipe_countdown = new_pipe_countdown- pipe_speed
    print(new_pipe_countdown)
    if new_pipe_countdown <= 0:
        new_pipe_countdown = 450
        placement = random.randint(0, 300)
        pipe_bottom = pygame.Rect(1000, 400 - placement + 75, PIPE_WIDTH, PIPE_HEIGHT) 
        pipe_top = pygame.Rect(1000, 400 - placement - PIPE_HEIGHT - 75, PIPE_WIDTH, PIPE_HEIGHT)
        pipes.append(pipe_bottom)
        pipes.append(pipe_top)
    
    for pipe in pipes:
        if pipe.x < -PIPE_WIDTH:
            pipes.remove(pipe)
    return new_pipe_countdown

def draw_window(bird, pipes):
    screen.blit(BACKGROUND, (0, 0))
    
    pygame.draw.rect(screen, YELLOW, bird)
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)
    pygame.display.update()

def main():
    run = True
    bird_x_start = 200
    bird_y_start = 250
    bird_speed = 0
    new_pipe_countdown = 450
    bird = pygame.Rect(bird_x_start, bird_y_start, BIRD_SIDE_LENGTH, BIRD_SIDE_LENGTH)
    
    floor = pygame.Rect(0, SCREEN_HEIGHT- 35, SCREEN_WIDTH, 50)
    pipes = []
    pipe1 = pygame.Rect(1000, 350, PIPE_WIDTH, PIPE_HEIGHT)
    pipe2 = pygame.Rect(1000, 350- PIPE_HEIGHT - 150, PIPE_WIDTH, PIPE_HEIGHT)
    
    pipes.append(pipe1)
    pipes.append(pipe2)
    
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_speed = 8
            if event.type == DEAD:
                run = False
                pygame.quit( )
                             
        handle_bird_movement(bird, bird_speed, pipes)
        new_pipe_countdown = handle_pipes(pipes, new_pipe_countdown)
        bird_speed -= GRAVITY
        draw_window(bird, pipes)

    pygame.quit()
        
if __name__ == "__main__":
    main()