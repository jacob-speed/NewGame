import pygame
from Functions import ball_collision, highscore, screen_shrink, set_start_parameters, update_scores
from Objects import Ball, Character

# Parameters
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
FPS = 24
SCALE = 0.8 
main_menu = True
frames_counter, timer, global_speed, scaler, print_score_counter, balls, char = set_start_parameters(Character, WINDOW_WIDTH, WINDOW_HEIGHT)


# Create window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Ball Game")

# Main game loop
running = True
while running:

    # Clear screen
    window.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Return to main menu
    if keys[pygame.K_ESCAPE]:
        main_menu = True    
        frames_counter, timer, global_speed, scaler, print_score_counter, balls, char = set_start_parameters(Character, WINDOW_WIDTH, WINDOW_HEIGHT)


    if main_menu:
        if keys[pygame.K_RETURN]:
            main_menu = False
        
        pygame.font.init()
        font = pygame.font.SysFont('comicsans', 50)
        label = font.render(f'Ball Game', True, (255, 255, 255))
        window.blit(label, ((WINDOW_WIDTH - label.get_width()) / 2, ((WINDOW_HEIGHT - label.get_height()) / 2)))
        label = font.render(f'Press Enter to play', True, (255, 255, 255))
        window.blit(label, ((WINDOW_WIDTH - label.get_width()) / 2, ((WINDOW_HEIGHT + label.get_height()) / 2)))

        # Update display
        pygame.display.update()
        pygame.time.delay(1000 // FPS)
        continue 



    # Move Character

    if keys[pygame.K_LEFT] and char.x > 0:
        char.x -= char.speed
    if keys[pygame.K_RIGHT] and char.x + char.width < WINDOW_WIDTH:
        char.x += char.speed
    if keys[pygame.K_DOWN] and char.y + char.height < WINDOW_HEIGHT:
        char.y += char.speed
    if keys[pygame.K_UP] and char.y > 0:
        char.y -= char.speed
    
    # Add Balls
    if (frames_counter % 100) == 0:
        balls.append(Ball(WINDOW_WIDTH, WINDOW_HEIGHT, scaler))
       



    # Move ball
    for ball in balls[:]:
        ball.x += ball.speed_x * global_speed
        ball.y += ball.speed_y * global_speed

    # Check for ball collisions with balls
        if ball.x <= ball.radius or ball.x >= WINDOW_WIDTH - ball.radius:
            ball.speed_x = -ball.speed_x
        if ball.y <= ball.radius or ball.y >= WINDOW_HEIGHT - ball.radius:
            ball.speed_y = -ball.speed_y
            
    # Check for ball collisions with character
        if ball_collision(ball, char):
            if ball.type == 1:
                screen_shrink(char, balls, scaler, SCALE)
            if ball.type == 2:
                char.speed *= 1.5
            if ball.type == 3:
                char.hp *= 2
            if ball.type == 4:
                char.hp -= ball.hp
            char.width = (20 + char.hp)
            char.height = 1.3 * char.width
            balls.remove(ball)
            

    # Update Frames
    frames_counter += 1 
    timer = round(frames_counter/24, 2)
    global_speed += 0.001

    # upon death
    if char.hp <= 0:
        preivous_time = timer
        frames_counter, timer, global_speed, scaler, print_score_counter, balls, char = set_start_parameters(Character, WINDOW_WIDTH, WINDOW_HEIGHT)
        print_score_counter = 100
        update_scores(preivous_time)
















    # Draw objects
    char.draw(window)
    for ball in balls:
        ball.draw(window)

    # Timer
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 20)
    label = font.render(f'Time {timer}', True, (255, 255, 255))
    window.blit(label, (WINDOW_WIDTH - 150, (label.get_height() / 2)))

    # high score
    label = font.render(f'High Score {highscore()}', True, (255, 255, 255))
    window.blit(label, (50, (label.get_height() / 2)))

    # previous time
    if print_score_counter > 0:
        print_score_counter -= 1
        font = pygame.font.SysFont('comicsans', 50)
        label = font.render(f'{preivous_time}', True, (255, 255, 255))
        window.blit(label, ((WINDOW_WIDTH - label.get_width()) / 2, ((WINDOW_HEIGHT - label.get_height()) / 2)))

    # Update display
    pygame.display.update()

    # Delay to maintain frame rate
    pygame.time.delay(1000 // FPS)

# Quit pygame
pygame.quit()
