import pygame
import sys
import random

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_size = 100
player_speed = 5

# Enemy settings
enemy_size = 100
base_enemy_speed = 3
enemy_speed_increase = 3

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load and resize images
background_image = pygame.image.load("background-img.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

player_image = pygame.image.load("rocket.png")
player_image = pygame.transform.scale(player_image, (player_size, player_size))

enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))

# Load sound effects
collision_sound = pygame.mixer.Sound(
    "collision_sound.mp3")  # Replace with your sound file
movement_sound = pygame.mixer.Sound(
    "movment.mp3")  # Replace with your sound file

# Load background music
pygame.mixer.music.load("background-music.mp3")  # Replace with your music file
pygame.mixer.music.set_volume(0.5)  # Adjust the volume (0.0 to 1.0)

# Font for the score
font = pygame.font.Font(None, 36)

# Function to draw the player


def draw_player(x, y):
    screen.blit(player_image, (x, y))

# Function to draw an enemy


def draw_enemy(x, y):
    screen.blit(enemy_image, (x, y))

# Function to display the score


def display_score(score):
    score_text = font.render("Score: {}".format(score), True, WHITE)
    screen.blit(score_text, (10, 10))

# Game loop


def game_loop():
    score = 0
    collision_time = 0

    # Initial player position
    player_x = WIDTH // 2 - player_size // 2
    player_y = HEIGHT - player_size - 10

    # Initial enemy position
    enemy_x = random.randint(0, WIDTH - enemy_size)
    enemy_y = 0

    # Initialize enemy_speed with base_enemy_speed
    enemy_speed = base_enemy_speed

    # Start playing background music
    pygame.mixer.music.play(-1)

    print("Game started")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
            print("Playing movement sound")
            movement_sound.play()
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed
            print("Playing movement sound")
            movement_sound.play()

        # Update enemy position
        enemy_y += enemy_speed
        if enemy_y > HEIGHT:
            enemy_x = random.randint(0, WIDTH - enemy_size)
            enemy_y = 0
            score += 1

            # Increase enemy speed every 10 points
            if score % 10 == 0:
                enemy_speed += enemy_speed_increase

        # Check for collision
        if (
            player_x < enemy_x + enemy_size
            and player_x + player_size > enemy_x
            and player_y < enemy_y + enemy_size
            and player_y + player_size > enemy_y
            and pygame.time.get_ticks() - collision_time > 5000  # 5000 milliseconds (5 seconds)
        ):
            print("Collision! Your Score: {}".format(score))
            collision_sound.play()
            # Add this line to check if the sound is triggered
            print("Playing collision sound")
            collision_time = pygame.time.get_ticks()  # Record the collision time
            pygame.time.delay(5000)  # Delay for 5 seconds before quitting

            pygame.quit()
            sys.exit()

        # Draw the background
        screen.blit(background_image, (0, 0))

        # Draw player and enemy
        draw_player(player_x, player_y)
        draw_enemy(enemy_x, enemy_y)

        # Display the score
        display_score(score)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)


if __name__ == "__main__":
    game_loop()
