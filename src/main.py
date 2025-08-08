import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Saucey Clicker: Vibe Edition")

# Load the bird image
bird_img_original = pygame.image.load('assets/bird.png').convert_alpha()
bird_img_small = pygame.transform.scale(bird_img_original, (int(bird_img_original.get_width() * 0.9), int(bird_img_original.get_height() * 0.9)))
bird_img_to_display = bird_img_original
bird_rect = bird_img_to_display.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))


# Score
score = 0
font = pygame.font.Font(None, 36)
points_per_click = 1

# Upgrade
upgrade_cost = 10
upgrade_level = 1
upgrade_rect = pygame.Rect(SCREEN_WIDTH - 200, 50, 180, 50)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bird_rect.collidepoint(event.pos):
                score += points_per_click
                bird_img_to_display = bird_img_small
            if upgrade_rect.collidepoint(event.pos):
                if score >= upgrade_cost:
                    score -= upgrade_cost
                    upgrade_level += 1
                    points_per_click += 1
                    upgrade_cost = int(upgrade_cost * 1.5)

    # Fill the background
    screen.fill((255, 255, 255))  # White

    # Update bird rect
    bird_rect = bird_img_to_display.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Draw the bird
    screen.blit(bird_img_to_display, bird_rect)

    # Reset bird image after drawing
    if bird_img_to_display == bird_img_small:
        bird_img_to_display = bird_img_original

    # Draw the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Draw the upgrade button
    pygame.draw.rect(screen, (0, 200, 0), upgrade_rect)
    upgrade_text = font.render(f"Upgrade (Cost: {upgrade_cost})", True, (255, 255, 255))
    screen.blit(upgrade_text, (upgrade_rect.x + 10, upgrade_rect.y + 10))


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
