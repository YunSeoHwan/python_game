import pygame

pygame.init()   # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("YSH Game")

# 배경 이미지 설정
background = pygame.image.load("image/background.png")

# 캐릭터 불러오기
character = pygame.image.load("image/character.png")
character_size = character.get_rect().size  # 이미지 크기 구해옴
character_width = character_size[0]   # 캐릭터 가로크기
character_height = character_size[1]  # 캐릭터 세로크기
character_x = (screen_width / 2) - (character_width / 2)  # 캐릭터 x좌표
character_y = screen_height - character_height  # 캐릭터 y좌표

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True  # 게임 진행 유무
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
      running = False   # 게임 진행중 아님

    if event.type == pygame.KEYDOWN:    # 키보드 입력받았을 때
      if event.key == pygame.K_LEFT:    # 왼쪽
        to_x -= 5
      elif event.key == pygame.K_RIGHT: # 오른쪽
        to_x += 5
      elif event.key == pygame.K_DOWN:  # 아래쪽
        to_y += 5
      elif event.key == pygame.K_UP:    # 위쪽
        to_y -= 5

    if event.type == pygame.KEYUP:    # 키보드 떼면 정지
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0

  character_x += to_x   # 실제 위치 변경
  character_y += to_y

  # 가로 경계값 표시
  if character_x < 0:
    character_x = 0
  elif character_x > screen_width - character_width:    # 캐릿터는 오른쪽 아래로 그려지기 때문
    character_x = screen_width - character_width

  # 세로 경계값 표시
  if character_y < 0:
    character_y = 0
  elif character_y > screen_height - character_height:
    character_y = screen_height - character_height

  screen.blit(background, (0, 0))   # 배경 그리기

  screen.blit(character, (character_x, character_y))    # 캐릭터 그리기

  pygame.display.update()   # 게임화면 그리기

# 게임 종료
pygame.quit()