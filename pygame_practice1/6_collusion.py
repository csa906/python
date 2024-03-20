import pygame
import os

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()
fps = 60

# 폴더 주소 가져오기
dir = os.getcwd()

# 배경 이미지 불러오기
background = pygame.image.load(dir + "\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(dir + "\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = (screen_width - character_width) / 2 # 캐릭터 가로 위치
character_y_pos = screen_height- character_height # 캐릭터 세로 위치

# 이동할 좌표
to_x = 0
to_y = 0
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load(dir + "\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터 가로 크기
enemy_height = enemy_size[1] # 캐릭터 세로 크기
enemy_x_pos = (screen_width - enemy_width) / 2 # 캐릭터 가로 위치
enemy_y_pos = (screen_height - enemy_height) / 2 # 캐릭터 세로 위치

# 이벤트 루프
running = True
while(running):
    dt = clock.tick(fps) # 프레임 수 설정
    print("fps : {0}".format(clock.get_fps()))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT): # 창 닫히는 이벤트
            running = False

        if(event.type == pygame.KEYDOWN): # 키 누르는 이벤트
            if(event.key == pygame.K_LEFT): # 캐릭터 왼쪽 이동
                to_x -= character_speed
            elif(event.key == pygame.K_RIGHT): 
                to_x += character_speed
            elif(event.key == pygame.K_UP):
                to_y -= character_speed
            elif(event.key == pygame.K_DOWN):
                to_y += character_speed

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                to_x = 0
            elif(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                to_y = 0
        
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if(character_x_pos < 0):
        character_x_pos = 0
    elif(character_x_pos > screen_width - character_width):
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if(character_y_pos < 0):
        character_y_pos = 0
    elif(character_y_pos > screen_height - character_height):
        character_y_pos = screen_height - character_height
    
    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if(character_rect.colliderect(enemy_rect)):
        print("충돌했어요")
        running = False

    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()

pygame.quit()