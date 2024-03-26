import pygame
import os

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang")

# FPS
clock = pygame.time.Clock()
fps = 60

# 1. 사용자 게임 초기화
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png")) 
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 이벤트 루프
running = True
while(running):
    dt = clock.tick(fps) # 프레임 수 설정


    # 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT): # 창 닫히는 이벤트
            running = False\
            
        if(event.type == pygame.KEYDOWN): 
            if(event.key == pygame.K_LEFT): # 캐릭터 왼쪽으로
                character_to_x -= character_speed
            elif(event.key == pygame.K_RIGHT): # 캐릭터 오른쪽으로
                character_to_x += character_speed
            elif(event.key == pygame.K_SPACE): # 무기 발사
                pass

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                character_to_x = 0


    # 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if(character_x_pos < 0):
        character_x_pos = 0
    elif(character_x_pos > screen_width - character_width):
        character_x_pos = screen_width - character_width

    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()


# pygame 종료
pygame.quit()