import pygame
import os
#########################################################
# 기본 초기화(반드시 해야 할 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640 
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang Game")

# FPS
clock = pygame.time.Clock()
#########################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트 등)
current_path = os.path.dirname(__file__)  # 현재 파일 위치 반환
image_path = os.path.join(current_path, "project_game/project2_image") # project_game 속 project2_image 위치 반환

# 배경화면
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 생성
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 생성
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x = (screen_width / 2) - (character_width / 2)
character_y = screen_height - character_height - stage_height

# 무기 생성
weapone = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapone_size = weapone.get_rect().size
weapone_width = weapone_size[0]

# 무기 발사 리스트
weapones = []

# 이동 좌표
to_x = 0

# 캐릭터 속도
character_speed = 5

# 무기 속도
weapone_speed = 10

running = True  
while running:
  dt = clock.tick(60) 

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:   
      running = False  

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x -= character_speed
      elif event.key == pygame.K_RIGHT:
        to_x += character_speed
      elif event.key == pygame.K_SPACE: # 무기 발사
        weapone_x = character_x + (character_width / 2) - (weapone_width / 2)
        weapone_y = character_y
        weapones.append([weapone_x, weapone_y])

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0

  # 3. 게임 캐릭터 위치 정의
  character_x += to_x

  if character_x < 0:
    character_x = 0
  elif character_x > screen_width - character_width:
    character_x = screen_width - character_width
    
  # 무기 위치 조정
  weapones = [ [w[0], w[1] - weapone_speed] for w in weapones if w[1] > 0] # 천장에 닿으면 없애기

  # 4. 충돌 처리

  # 5. 화면 그리기
  screen.blit(background, (0, 0))

  for weapone_x, weapone_y in weapones:   # 리스트이기 때문에 반복문 사용
    screen.blit(weapone, (weapone_x, weapone_y))

  screen.blit(stage, (0, screen_height - stage_height))
  screen.blit(character, (character_x, character_y))

  

  pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) 

# 게임 종료
pygame.quit()