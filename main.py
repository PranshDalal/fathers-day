import pygame
import random


pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Star Wars Quote Generator")

pygame.mixer.music.load("star_wars_music.mp3")  
pygame.mixer.music.play(-1)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


font = pygame.font.Font(None, 36)


quotes = [
    "May the Force be with you.",
    "I am your father.",
    "Do. Or do not. There is no try.",
    "In my experience, there is no such thing as luck.",
    "The Force will be with you, always.",
    "It's a trap!",
    "I find your lack of faith disturbing.",
    "Help me, Obi-Wan Kenobi. You're my only hope.",
    "Fear is the path to the dark side.",
    "I've got a bad feeling about this.",
    "The ability to speak does not make you intelligent.",
    "Never tell me the odds.",
    "It is our choices that show us who we truly are.",
    "I love you. I know.",
    "You were the chosen one!",
    "That's no moon. It's a space station.",
    "You don't need to see his identification.",
    "I find your lack of faith disturbing.",
    "It's the ship that made the Kessel Run in less than twelve parsecs.",
    "You can't stop the change, any more than you can stop the suns from setting.",
    "A long time ago in a galaxy far, far away...",
    "The Force is strong with this one.",
    "I suggest a new strategy, R2: let the Wookiee win.",
    "I have a bad feeling about this.",
    "I'm just a simple man trying to make my way in the universe.",
    "I've got a bad feeling about this.",
    "Your focus determines your reality.",
    "I find your lack of faith disturbing.",
    "Chewie, we're home.",
    "It's a trap!",
    "That's not how the Force works!",
    "I suggest a new strategy, Artoo: let the Wookiee win.",
    "The garbage'll do!",
    "That's one hell of a pilot!",
    "The Force will be with you. Always.",
    "I'm one with the Force. The Force is with me.",
    "I'll never turn to the dark side. You've failed, your highness. I am a Jedi, like my father before me.",
    "I'm just a simple man trying to make my way in the universe.",
    "You have hate, you have anger, but you don't use them.",
    "This is a rebellion, isn't it? I rebel.",
    "I find your lack of faith disturbing.",
    "Help me, Obi-Wan Kenobi. You're my only hope.",
    "The Force will be with you, always.",
    "I suggest a new strategy, R2: let the Wookiee win.",
    "I have a bad feeling about this.",
    "It's the ship that made the Kessel Run in less than twelve parsecs.",
    "You can't stop the change, any more than you can stop the suns from setting.",
    "A long time ago in a galaxy far, far away...",
    "The Force is strong with this one.",
    "I suggest a new strategy, R2: let the Wookiee win.",
    "I'm just a simple man trying to make my way in the universe.",
    "I've got a bad feeling about this.",
    "Your focus determines your reality.",
    "I find your lack of faith disturbing.",
    "Chewie, we're home.",
    "It's a trap!",
    "That's not how the Force works!",
    "I suggest a new strategy, Artoo: let the Wookiee win.",
]


current_quote = random.choice(quotes)


running = True
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:

            current_quote = random.choice(quotes)

    window.fill(BLACK)

    happy_text = font.render("Happy father's day", True, WHITE)
    window.blit(happy_text, (275, 100))

    press_text = font.render("Press anywhere to move on", True, WHITE)
    window.blit(press_text, (250, 400))

    quote_text = font.render(current_quote, True, WHITE)
    quote_rect = quote_text.get_rect(center=(window_width/2, window_height/2))
    window.blit(quote_text, quote_rect)


    pygame.display.update()

    clock.tick(30)


pygame.quit()