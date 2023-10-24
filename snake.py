import os
import random
import msvcrt
import time

# Set up the game board
board_width = 20
board_height = 10
snake_char = '*'
food_char = 'X'
border_char = '#'

# Initialize the snake
snake = [(board_height // 2, board_width // 2)]
snake_direction = (0, 1)

# Initialize the food
food = (random.randint(1, board_height - 2), random.randint(1, board_width - 2))

# Game variables
score = 0
game_over = False

def draw_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(board_height):
        for j in range(board_width):
            if (i, j) == snake[0]:
                print(snake_char, end='')
            elif (i, j) == food:
                print(food_char, end='')
            elif i == 0 or i == board_height - 1 or j == 0 or j == board_width - 1:
                print(border_char, end='')
            else:
                print(' ', end='')
        print()

def move_snake():
    global game_over, score
    head_x, head_y = snake[0]
    new_head = (head_x + snake_direction[0], head_y + snake_direction[1])

    if new_head == food:
        snake.insert(0, new_head)
        score += 1
        food = (random.randint(1, board_height - 2), random.randint(1, board_width - 2))
    elif (new_head in snake[1:] or new_head[0] in (0, board_height - 1) or new_head[1] in (0, board_width - 1)):
        game_over = True
    else:
        snake.insert(0, new_head)
        snake.pop()

def get_key():
    key = msvcrt.getch()
    if key == b'w' and snake_direction != (1, 0):
        return (1, 0)
    elif key == b's' and snake_direction != (-1, 0):
        return (-1, 0)
    elif key == b'a' and snake_direction != (0, 1):
        return (0, -1)
    elif key == b'd' and snake_direction != (0, -1):
        return (0, 1)
    else:
        return snake_direction

while not game_over:
    snake_direction = get_key()
    move_snake()
    draw_board()
    time.sleep(0.1)

print("Game over! Your score: ", score)
