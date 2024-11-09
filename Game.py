import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("bg.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, color, height, width):
        
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)
        

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint( 0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

sprite3 = Sprite(pygame.Color('gold'), 20, 30)
sprite3.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite3.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite3)

sprite4 = Sprite(pygame.Color('blue'), 20, 30)
sprite4.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite4.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite4)

sprite5 = Sprite(pygame.Color('lightblue'), 20, 30)
sprite5.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite5.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite5)

sprite6= Sprite(pygame.Color('green'), 20, 30)
sprite6.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite6.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite6)

sprite7 = Sprite(pygame.Color('white'), 20, 30)
sprite7.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite7.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite7)

sprite8 = Sprite(pygame.Color('pink'), 20, 30)
sprite8.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite8.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite8)

sprite9 = Sprite(pygame.Color('cyan'), 20, 30)
sprite9.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite9.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite9)

sprite10 = Sprite(pygame.Color('yellow'), 20, 30)
sprite10.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite10.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite10)

sprite11 = Sprite(pygame.Color('orange'), 20, 30)
sprite11.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite11.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite11)

sprite12 = Sprite(pygame.Color('purple'), 20, 30)
sprite12.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite12.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite12)

sprite13 = Sprite(pygame.Color('magenta'), 20, 30)
sprite13.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite13.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite13)

sprite14 = Sprite(pygame.Color('white'), 20, 30)
sprite14.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite14.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite14)

sprite15 = Sprite(pygame.Color('cyan'), 20, 30)
sprite15.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite15.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite15)

sprite16 = Sprite(pygame.Color('gold'), 20, 30)
sprite16.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite16.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(all_sprites)

sprite17 = Sprite(pygame.Color('darkblue'), 20, 30)
sprite17.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite17.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite17)

sprite18 = Sprite(pygame.Color('green'), 20, 30)
sprite18.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite18.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite18)

sprite19 = Sprite(pygame.Color('purple'), 20, 30)
sprite19.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite19.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite19)

sprite20 = Sprite(pygame.Color('pink'), 20, 30)
sprite20.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite20.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite20)

running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
            
    if not won:
        keys = pygame.key.get_pressed()
        
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED 
        
        sprite1.move(x_change, y_change)
        
        if sprite1.rect.colliderect(sprite2.rect):
            
            all_sprites.remove(sprite2)
            won = True
        
        
        if sprite1.rect.colliderect(sprite3.rect):
            
            all_sprites.remove(sprite3)
            
        
        if sprite1.rect.colliderect(sprite4.rect):
            
            all_sprites.remove(sprite4)
        
        
        if sprite1.rect.colliderect(sprite5.rect):
            
            all_sprites.remove(sprite5)
            
        
        if sprite1.rect.colliderect(sprite6.rect):
            
            all_sprites.remove(sprite6)
            
        
        if sprite1.rect.colliderect(sprite7.rect):
            
            all_sprites.remove(sprite7)
            
        
        if sprite1.rect.colliderect(sprite8.rect):
            
            all_sprites.remove(sprite8)
            
        
        if sprite1.rect.colliderect(sprite9.rect):
            
            all_sprites.remove(sprite9)
            
        
        if sprite1.rect.colliderect(sprite10.rect):
            
            all_sprites.remove(sprite10)
            
        
        if sprite1.rect.colliderect(sprite11.rect):
            
            all_sprites.remove(sprite11)
            
        
        if sprite1.rect.colliderect(sprite12.rect):
            
            all_sprites.remove(sprite12)
            
        
        if sprite1.rect.colliderect(sprite13.rect):
            
            all_sprites.remove(sprite13)
            
        
        if sprite1.rect.colliderect(sprite14.rect):
            
            all_sprites.remove(sprite14)
            
        
        if sprite1.rect.colliderect(sprite15.rect):
            
            all_sprites.remove(sprite15)
            
        
        if sprite1.rect.colliderect(sprite16.rect):
            
            all_sprites.remove(sprite16)
        
        
        if sprite1.rect.colliderect(sprite17.rect):
            
            all_sprites.remove(sprite17)
            
            
        if sprite1.rect.colliderect(sprite18.rect):
            
            all_sprites.remove(sprite18)
            
            
        if sprite1.rect.colliderect(sprite19.rect):
            
            all_sprites.remove(sprite19)
            
            
        if sprite1.rect.colliderect(sprite20.rect):
            
            all_sprites.remove(sprite20)

            
        
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)
    
    
    if won:
        win_text = font.render("YOU LOSE!", True, pygame.Color('black'))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2, (SCREEN_HEIGHT - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(90)
    
pygame.quit()

    
        