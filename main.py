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

# 이벤트 루프
running = True  # 게임 진행 유무
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
      running = False   # 게임 진행중 아님
    
  screen.blit(background, (0, 0))   # 배경 그리기

  screen.blit(character, (character_x, character_y))    # 캐릭터 그리기

  pygame.display.update()   # 게임화면 그리기

# 게임 종료
pygame.quit()