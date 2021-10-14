import pygame
import random
#########################################################
# 기본 초기화(반드시 해야 할 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("YSH Game")

# FPS
clock = pygame.time.Clock()
#########################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트 등)

# 배경화면
background = pygame.image.load("image/paper_bg.jpg")

# 플레이어 설정
player = pygame.image.load("image/1.png")
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height

player_speed = 10

# 장애물 설정
enemy = pygame.image.load("image/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_hegiht = enemy_size[1]
enemy_x = random.randint(0, screen_width-enemy_width) # x좌표 랜덤
enemy_y = 0

enemy_speed = 10

# 이동 좌표
to_x = 0
to_y = 0

running = True  
while running:
  dt = clock.tick(30) 

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:   
      running = False  

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x -= player_speed
      elif event.key == pygame.K_RIGHT:
        to_x += player_speed
      
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
    

  # 3. 게임 캐릭터 위치 정의
  player_x += to_x

  if player_x < 0:
    player_x = 0
  elif player_x > screen_width - player_width:
    player_x = screen_width - player_width

  enemy_y += enemy_speed

  if enemy_y > screen_height:
    enemy_y = 0
    enemy_x = random.randint(0, screen_width-enemy_width)

  # 4. 충돌 처리
  player_rect = player.get_rect()   # 캐릭터 rect 값 자체에 위치를 설정
  player_rect.left = player_x       # blit는 그리기 값만 준것이지 실제로는 고정 값
  player_rect.top = player_y        # 직접 rect 좌표에 값 입력

  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x
  enemy_rect.top = enemy_y

  if player_rect.colliderect(enemy_rect):
    print("충돌했어요")
    running = False

  # 5. 화면 그리기
  screen.blit(background, (0, 0))
  screen.blit(player, (player_x, player_y))
  screen.blit(enemy, (enemy_x, enemy_y))
  
  pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) 

# 게임 종료
pygame.quit()