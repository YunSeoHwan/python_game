import pygame
import os
#########################################################
# 기본 초기화(반드시 해야 할 것들)
pygame.init()

# 화면 크기 설정
screen_width = 680 
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang Game")

# FPS
clock = pygame.time.Clock()
#########################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트 등)
current_path = os.path.dirname(__file__)  # 현재 파일 위치 반환
image_path = os.path.join(current_path, "project2_image") # project2_image 위치 반환

# 배경화면
background = os.path.join(image_path, "background.png")

# 스테이지 생성
stage = os.path.join(image_path, "stage.png")
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 생성
character = os.path.join(image_path, "character.png")
character_size = character.get_rect().size


running = True  
while running:
  dt = clock.tick(60) 

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:   
      running = False  

  # 3. 게임 캐릭터 위치 정의

  # 4. 충돌 처리

  # 5. 화면 그리기
  screen.blit(background, (0, 0))
  screen.blit(stage, (0,screen_height - stage_height))

  pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) 

# 게임 종료
pygame.quit()