import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 300, 300
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define the Tic Tac Toe grid
grid = [[' ' for _ in range(3)] for _ in range(3)]

# Function to draw the X and O symbols


def draw_symbols():
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 'X':
                pygame.draw.line(win, black, (col * width // 3, row * height // 3),
                                 ((col + 1) * width // 3, (row + 1) * height // 3), 3)
                pygame.draw.line(win, black, ((col + 1) * width // 3, row * height // 3),
                                 (col * width // 3, (row + 1) * height // 3), 3)
            elif grid[row][col] == 'O':
                pygame.draw.circle(win, black, (col * width // 3 + width // 6, row * height // 3 + height // 6),
                                   min(width // 6, height // 6), 3)

# Function to check for a win


def check_win():
    # Check rows and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != ' ' or grid[0][i] == grid[1][i] == grid[2][i] != ' ':
            return True
    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != ' ' or grid[0][2] == grid[1][1] == grid[2][0] != ' ':
        return True
    return False

# Function to check for a draw


def check_draw():
    for row in grid:
        for cell in row:
            if cell == ' ':
                return False
    return True


# Main game loop
player_turn = 'X'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // (height // 3)
            clicked_col = mouseX // (width // 3)

            if grid[clicked_row][clicked_col] == ' ':
                grid[clicked_row][clicked_col] = player_turn
                if check_win():
                    print(f"Player {player_turn} wins!")
                    pygame.quit()
                    sys.exit()
                elif check_draw():
                    print("It's a draw!")
                    pygame.quit()
                    sys.exit()
                else:
                    player_turn = 'O' if player_turn == 'X' else 'X'

    # Draw the game board
    win.fill(white)
    # Draw grid lines
    for i in range(1, 3):
        pygame.draw.line(win, black, (i * width // 3, 0),
                         (i * width // 3, height), 3)
        pygame.draw.line(win, black, (0, i * height // 3),
                         (width, i * height // 3), 3)

    # Draw X and O symbols
    draw_symbols()

    pygame.display.update()
