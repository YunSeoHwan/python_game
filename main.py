import pygame

pygame.init()   # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("YSH Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 설정
background = pygame.image.load("image/background.png")

# 캐릭터 불러오기
character = pygame.image.load("image/character.png")
character_size = character.get_rect().size  # 이미지 크기 구해옴
character_width = character_size[0]   # 캐릭터 가로크기
character_height = character_size[1]  # 캐릭터 세로크기
character_x = (screen_width / 2) - (character_width / 2)  # 캐릭터 x좌표
character_y = screen_height - character_height  # 캐릭터 y좌표

# 적 캐릭터 생성
enemy = pygame.image.load("image/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]   
enemy_height = enemy_size[1]  
enemy_x = (screen_width / 2) - (enemy_width / 2) 
enemy_y = (screen_height / 2) - (enemy_height / 2) 

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()   # 시작 tick을 받아옴(for문 밖에 있으므로 고정값))
 
# 이동할 좌표
to_x = 0
to_y = 0

# 캐릭터 속도
character_speed = 0.6

# 이벤트 루프
running = True  # 게임 진행 유무
while running:
  dt = clock.tick(60)   # 초당 게임화면 프레임 수

  for event in pygame.event.get():
    if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
      running = False   # 게임 진행중 아님

    if event.type == pygame.KEYDOWN:    # 키보드 입력받았을 때
      if event.key == pygame.K_LEFT:    # 왼쪽
        to_x -= character_speed
      elif event.key == pygame.K_RIGHT: # 오른쪽
        to_x += character_speed
      elif event.key == pygame.K_DOWN:  # 아래쪽
        to_y += character_speed
      elif event.key == pygame.K_UP:    # 위쪽
        to_y -= character_speed

    if event.type == pygame.KEYUP:    # 키보드 떼면 정지
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0
  
  character_x += to_x * dt  # 실제 위치 변경
  character_y += to_y * dt  # dt 값을 곱해줌으로써 속도를 일정하게 유지

  # 가로 경계값 표시
  if character_x < 0:
    character_x = 0
  elif character_x > screen_width - character_width:    # 캐릭터는 오른쪽 아래로 그려지기 때문
    character_x = screen_width - character_width

  # 세로 경계값 표시
  if character_y < 0:
    character_y = 0
  elif character_y > screen_height - character_height:
    character_y = screen_height - character_height

  # 충돌 처리
  character_rect = character.get_rect()   # 캐릭터 rect 값 자체에 위치를 설정
  character_rect.left = character_x       # blit는 그리기 값만 준것이지 실제로는 고정 값
  character_rect.top = character_y        # 직접 rect 좌표에 값 입력

  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x
  enemy_rect.top = enemy_y

  # 충돌 체크
  if character_rect.colliderect(enemy_rect):
    print("충돌했어요")
    running = False

  screen.blit(background, (0, 0))   # 배경 그리기

  screen.blit(character, (character_x, character_y))    # 캐릭터 그리기

  screen.blit(enemy, (enemy_x, enemy_y))  # 적 캐릭터 그리기

  # 경과 시간 계산
  elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 초 단위로 표시, 반복문을 통해 지속적으로 값이 변함
 
  timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
  # 출력할 글자, True, 색상
  if total_time - elapsed_time <= 0:
    print("타임 아웃")
    running = False

  screen.blit(timer, (10,10))
  pygame.display.update()   # 게임화면 그리기

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기

# 게임 종료
pygame.quit()