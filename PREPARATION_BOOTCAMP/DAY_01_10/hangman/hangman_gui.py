import math
import os
import sys
import time
import pygame
from PREPARATION_BOOTCAMP.DAY_01_10.hangman.hangman import Hangman, get_args, load_words, pick_word, save_score, error

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (40, 170, 70)
RED = (210, 50, 50)
GREY = (150, 150, 150)
WOOD = (130, 85, 40)
DARK = (30, 30, 50)

HERE = os.path.dirname(os.path.abspath(__file__))


def load_background():
    # Background image, or a plain sky if the file is missing or broken
    try:
        image = pygame.image.load(os.path.join(HERE, "assets", "background.jpg")).convert()
        return pygame.transform.scale(image, (WIDTH, HEIGHT))
    except (pygame.error, FileNotFoundError):
        surface = pygame.Surface((WIDTH, HEIGHT))
        surface.fill((135, 200, 235))
        return surface


def letter_rects():
    # One clickable square per letter, 6 per row, on the left side
    rects = {}
    for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        rects[letter] = pygame.Rect(30 + (i % 6) * 55, 90 + (i // 6) * 55, 45, 45)
    return rects


def draw_gallows(surface):
    pygame.draw.line(surface, WOOD, (470, 520), (720, 520), 10)  # floor
    pygame.draw.line(surface, WOOD, (680, 520), (680, 110), 10)  # post
    pygame.draw.line(surface, WOOD, (685, 110), (550, 110), 10)  # beam
    pygame.draw.line(surface, WOOD, (680, 160), (630, 110), 6)   # diagonal
    pygame.draw.line(surface, WOOD, (560, 110), (560, 170), 3)   # rope


def draw_stickman(surface, parts, x=560, y=200, color=BLACK):
    # Draws only the first `parts` body parts (0 to 6)
    limbs = [
        ((x, y + 30),  (x, y + 150)),       # body
        ((x, y + 60),  (x - 50, y + 110)),  # left arm
        ((x, y + 60),  (x + 50, y + 110)),  # right arm
        ((x, y + 150), (x - 40, y + 230)),  # left leg
        ((x, y + 150), (x + 40, y + 230)),  # right leg
    ]
    if parts >= 1:
        pygame.draw.circle(surface, color, (x, y), 30, 4)  # head
    for start, end in limbs[:parts - 1]:
        pygame.draw.line(surface, color, start, end, 4)


def text(surface, font, msg, color, center):
    image = font.render(msg, True, color)
    surface.blit(image, image.get_rect(center=center))


def draw(screen, fonts, background, game, rects, message, time_left, end_lines):
    big, medium, small = fonts
    screen.blit(background, (0, 0))

    # Top bar: life bar, attempts, timer
    pygame.draw.rect(screen, DARK, (0, 0, WIDTH, 60))
    life = max(0, 1 - game.penalties / game.max_penalties)
    pygame.draw.rect(screen, GREY, (20, 20, 200, 20), 2)
    pygame.draw.rect(screen, GREEN if life > 0.3 else RED, (22, 22, int(196 * life), 16))
    text(screen, small, f"Attempts: {game.attempts}", WHITE, (330, 30))
    if time_left is not None:
        text(screen, small, f"Time: {math.ceil(time_left)}s",
             RED if time_left < 10 else WHITE, (480, 30))
    text(screen, small, f"Penalties: {game.penalties}/{game.max_penalties}", WHITE, (670, 30))

    # Letters: green = found, red = wrong, dark = not tried yet
    for letter, rect in rects.items():
        color = GREEN if letter in game.found else RED if letter in game.wrong else DARK
        pygame.draw.rect(screen, color, rect, border_radius=8)
        text(screen, medium, letter, WHITE, rect.center)

    # Gallows + the stickman grows with the penalties
    draw_gallows(screen)
    parts = min(6, math.ceil(game.penalties * 6 / game.max_penalties))
    draw_stickman(screen, parts)

    # The word: hidden letters as "_", missed letters in red at the end
    over = bool(end_lines)
    x = WIDTH // 2 - len(game.word) * 18
    for i, c in enumerate(game.word):
        shown = c in game.found or game.word_guessed
        if shown or over:
            text(screen, big, c, BLACK if shown else RED, (x + i * 36 + 18, 470))
        else:
            text(screen, big, "_", BLACK, (x + i * 36 + 18, 470))

    if message:
        text(screen, small, message, DARK, (WIDTH // 2, 540))

    # End screen
    if over:
        veil = pygame.Surface((WIDTH, 170), pygame.SRCALPHA)
        veil.fill((0, 0, 0, 180))
        screen.blit(veil, (0, 190))
        for i, (line, color) in enumerate(end_lines):
            text(screen, medium if i == 0 else small, line, color, (WIDTH // 2, 225 + i * 40))
        text(screen, small, "ENTER: play again   -   ESC: quit", WHITE, (WIDTH // 2, 335))

    pygame.display.flip()


def main():
    args = get_args()
    try:
        words = load_words(args.file)
    except ValueError as e:
        error(e)
        sys.exit(1)
    if pick_word(words, args.length) is None:
        error(f"no word of {args.length} letters in the file")
        sys.exit(1)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")
    clock = pygame.time.Clock()
    fonts = (pygame.font.Font(None, 56), pygame.font.Font(None, 36), pygame.font.Font(None, 26))
    background = load_background()
    rects = letter_rects()

    def new_game():
        return Hangman(pick_word(words, args.length), args.penalties), time.time()

    game, start = new_game()
    message = "Click a letter or type it on your keyboard"
    end_lines = []  # filled when the game is over

    running = True
    while running:
        guess = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif end_lines and event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    game, start = new_game()
                    message, end_lines = "", []
                elif not end_lines and event.unicode.isascii() and event.unicode.isalpha():
                    guess = event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not end_lines:
                for letter, rect in rects.items():
                    if rect.collidepoint(event.pos):
                        guess = letter

        time_left = None
        if args.time and not end_lines:
            time_left = max(0, args.time - (time.time() - start))

        if guess:
            status, message = game.guess(guess)

        # Check the end of the game (only once, when end_lines is still empty)
        if not end_lines:
            if game.won():
                end_lines = [("You found it!", GREEN),
                             (save_score(game.word, game.attempts), WHITE)]
            elif game.lost():
                end_lines = [(f"You lose! The word was {game.word}", RED)]
            elif time_left == 0:
                end_lines = [(f"Time's up! The word was {game.word}", RED)]

        draw(screen, fonts, background, game, rects, message, time_left, end_lines)
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()