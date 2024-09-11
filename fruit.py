import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Fruit Ninja")

# Define colors
white = (255, 255, 255)

# Load images
background_img = pygame.image.load(r"C:\Users\thole\OneDrive\Desktop\anjali\background.png")
banana_img = pygame.image.load(r"C:\Users\thole\OneDrive\Desktop\anjali\banana1.png")
apple_img = pygame.image.load(r"C:\Users\thole\OneDrive\Desktop\anjali\apple1.png")
mango_img = pygame.image.load(r"C:\Users\thole\OneDrive\Desktop\anjali\mango1.png")
grapes_img = pygame.image.load(r"C:\Users\thole\OneDrive\Desktop\anjali\watermelon1.png")
kiwi_img = pygame.image.load(r"C:\Users\thole\OneDrive\Desktop\anjali\kiwi1.png")
bomb_img = pygame.image.load(r"C:\Users\thole\OneDrive\Desktop\anjali\bomb.png")
play_button_img = pygame.image.load(r"C:\Users\thole\OneDrive\Desktop\anjali\playy1.png")

# Set up the clock
clock = pygame.time.Clock()

# Game variables
score = 0
lives = 3
game_active = False

# Fruit class
class Fruit(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, window_width - 100)
        self.rect.y = window_height
        self.speed = random.randint(2, 6)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.x = random.randint(100, window_width - 100)
            self.rect.y = window_height
            self.speed = random.randint(2, 6)

# Bomb class
class Bomb(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, window_width - 100)
        self.rect.y = window_height
        self.speed = random.randint(2, 6)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.x = random.randint(100, window_width - 100)
            self.rect.y = window_height
            self.speed = random.randint(2, 6)

# Create sprite groups
fruits_group = pygame.sprite.Group()
bombs_group = pygame.sprite.Group()

# Create initial fruits
fruit_images = [banana_img, apple_img, mango_img, grapes_img, kiwi_img]
for _ in range(50):
    fruit_image = random.choice(fruit_images)
    fruit = Fruit(fruit_image)
    fruits_group.add(fruit)

# Create initial bombs
for _ in range(4):
    bomb = Bomb(bomb_img)
    bombs_group.add(bomb)


# Function to start the game
def start_game():
    global game_active, score, lives
    game_active = True
    score = 0
    lives = 3
    fruits_group.empty()
    bombs_group.empty()
    for _ in range(50):
        fruit_image = random.choice(fruit_images)
        fruit = Fruit(fruit_image)
        fruits_group.add(fruit)
    for _ in range(3):
        bomb = Bomb(bomb_img)
        bombs_group.add(bomb)


# Add play button functionality
play_button_rect = play_button_img.get_rect()
play_button_rect.center = (window_width // 2, window_height // 2)


# Function to display the game over text
def display_game_over():
    game_over_text = game_font.render("Game Over", True, (0, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(game_over_text, game_over_rect)


# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_active and play_button_rect.collidepoint(event.pos):
                start_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

   
    # Clear the screen
    window.fill(white)
    window.blit(background_img, (0, 0))

    if game_active:
        # Update and draw fruits
        fruits_group.update()
        fruits_group.draw(window)

        # Update and draw bombs
        bombs_group.update()
        bombs_group.draw(window)

        # Check for collisions with fruits
        for fruit in fruits_group:
            if fruit.rect.collidepoint(pygame.mouse.get_pos()):
                fruits_group.remove(fruit)
                score += 1

        # Check for collisions with bombs
        for bomb in bombs_group:
            if bomb.rect.collidepoint(pygame.mouse.get_pos()):
                bombs_group.remove(bomb)
                lives -= 1
                if lives == 0:
                    game_active = False
                    display_game_over()
        # Define a font for the game text
        game_font = pygame.font.Font(None, 48)

        # Display score and lives
        score_text = game_font.render(f"Score: {score}", True, (0, 0, 0))
        lives_text = game_font.render(f"Lives: {lives}", True, (0, 0, 0))
        window.blit(score_text, (10, 10))
        window.blit(lives_text, (window_width - lives_text.get_width() - 10, 10))
    else:
        # Display play button
        window.blit(play_button_img, play_button_rect)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()