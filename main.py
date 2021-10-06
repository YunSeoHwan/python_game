import pygame

pygame.init()   # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("YSH Game")

# 배경 이미지 설정
background = pygame.image.load("background.png")
# 이벤트 루프
running = True  # 게임 진행 유무
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
      running = False   # 게임 진행중 아님
    
  screen.blit(background, (0, 0))   # 배경 그리기
  pygame.display.update()   # 게임화면 그리기

# 게임 종료
pygame.quit()