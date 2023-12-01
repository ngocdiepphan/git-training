#import
import pygame,random,time,sys
pygame.init()

# load hình ảnh
m = 20 # kích thước chiều cao và chiều rộng
Imgbody = pygame.transform.scale(pygame.image.load('body.jpg'),(m,m))
Imghead = pygame.transform.scale(pygame.image.load('head.jpg'),(m,m))
Imgfood = pygame.transform.scale(pygame.image.load('covid.png'),(m,m))

pygame.mixer.init()
pygame.mixer.music.load("nhac.mp3")
pygame.mixer.music.play()

# tạo cửa sổ
gameSurface = pygame.display.set_mode((735,475))
pygame.display.set_caption('Snake Covid-19!')

# màu sắc
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
gray = pygame.Color(128,128,128)

# khai báo biến
snakepos = [100,60]
snakebody = [[100,60],[80,60],[60,60]]
foodx = random.randrange(1,71)
foody = random.randrange(1,45)
if foodx % 2 != 0: foodx += 1
if foody % 2 != 0: foody += 1
foodpos = [foodx * 10, foody * 10]
foodflat = True
direction = 'RIGHT'
changeto = direction
score = 0
#Font
font = pygame.font.SysFont('sans',30)
t_quit = font.render('Quit',1,(0,0,0))
t_start = font.render('Start',1,(255,0,0))

# hàm gameover
def game_sure(click):
    global game_over,snakepos,snakebody,foodx,foody,direction,changeto,score

    r1 = pygame.draw.rect(gameSurface,(255,0,0),(735 / 2 - 100/2 + 100,475 / 2 - 50/2,100,50))
    gameSurface.blit(t_quit,((735 / 2 - 100/2 + 100) + 100/2 - t_quit.get_width()/2,(475 / 2 - 50/2) + 50/2 - t_quit.get_height()/2))
    r2 = pygame.draw.rect(gameSurface,(0,0,0),(735 /2 - 100/2 - 100,475 / 2 - 50/2,100,50))
    gameSurface.blit(t_start,((735 / 2 - 100/2 - 100) + 100/2 - t_start.get_width()/2,(475 / 2 - 50/2) + 50/2 - t_start.get_height()/2))
    if click:
        pos = pygame.mouse.get_pos()
        if r1.collidepoint(pos):
            pygame.quit()
        elif r2.collidepoint(pos):
            game_over = False
            foodx = random.randrange(1,71)
            foody = random.randrange(1,45)
            if foodx % 2 != 0: foodx += 1
            if foody % 2 != 0: foody += 1
            foodpos = [foodx * 10, foody * 10]
            snakepos = [100,60]
            snakebody = [[100,60],[80,60],[60,60]]
            direction = 'RIGHT'
            changeto = direction
            score = 0

# hàm show_score
def show_score(choice = 1):
    sfont = pygame.font.SysFont('consolas',20)
    ssurf = sfont.render('Score: {0}'.format(score),True,black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (70,20)
    else:
        srect.midtop = (360,230)
    gameSurface.blit(ssurf,srect)
game_over = False
def draw_button(surface,click):
    global start
    r1 = pygame.draw.rect(surface,(255,0,0),(735 / 2 - 100/2 + 100,475 / 2 - 50/2,100,50))
    surface.blit(t_quit,((735 / 2 - 100/2 + 100) + 100/2 - t_quit.get_width()/2,(475 / 2 - 50/2) + 50/2 - t_quit.get_height()/2))
    r2 = pygame.draw.rect(surface,(0,0,0),(735 /2 - 100/2 - 100,475 / 2 - 50/2,100,50))
    surface.blit(t_start,((735 / 2 - 100/2 - 100) + 100/2 - t_start.get_width()/2,(475 / 2 - 50/2) + 50/2 - t_start.get_height()/2))
    if click: 
        pos = pygame.mouse.get_pos()
        if r1.collidepoint(pos):
            pygame.quit()
        elif r2.collidepoint(pos):
            start = True
clicked = False
start = False
isPause = False
delaySpeed = 200

# vòng lặp chính
while True:
    pygame.time.delay(delaySpeed) # tốc độ chơi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
        # xử lý phím
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeto = 'LEFT'
            if event.key == pygame.K_UP:
                changeto = 'UP'
            if event.key == pygame.K_DOWN:
                changeto = 'DOWN'
            
            if event.key == pygame.K_SPACE:
                isPause = not isPause
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.evet.Event(pygame.QUIT))

    # hướng đi
    if start and game_over == False and isPause == False:
        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeto == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeto == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'
        # cập nhật vị trí mới
        if direction == 'RIGHT':
            snakepos[0] += m
        if direction == 'LEFT':
            snakepos[0] -= m
        if direction == 'UP':
            snakepos[1] -= m
        if direction == 'DOWN':
            snakepos[1] += m
        #cơ chế thêm khúc dài ra
        snakebody.insert(0,list(snakepos))
        if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
            score += 1
            if score % 4 == 0:
                delaySpeed -= 40
            foodflat = False
        else:
            snakebody.pop()
        # sản sinh covid
        if foodflat == False:
            foodx = random.randrange(1,71)
            foody = random.randrange(1,45)
            if foodx %2 != 0: foodx += 1
            if foody %2 != 0: foody += 1
            foodpos = [foodx * 10, foody * 10]
    foodflat = True
    #  cập nhật lên cửa sổ
    gameSurface.fill((255,255,255))

    if start:
        for pos in snakebody:
            gameSurface.blit(Imgbody,pygame.Rect(pos[0],pos[1],m,m))
            #pygame.draw.rect(gameSurface,blue,pygame.Rect(pos[0],pos[1],m,m))
        gameSurface.blit(Imghead,pygame.Rect(snakebody[0][0],snakebody[0][1],m,m)) # head
        gameSurface.blit(Imgfood,pygame.Rect(foodpos[0],foodpos[1],m,m))
        #pygame.draw.rect(gameSurface,gray,pygame.Rect(foodpos[0],foodpos[1],m,m))

        # xử lý di chuyển đụng 4 cạnh biên
        if snakepos[0] > 710 or snakepos[0] < 10:
            game_over = True
            delaySpeed = 200
        if snakepos[1] > 450 or snakepos[1] < 10:
            game_over = True
            delaySpeed = 200
        # xử lý tự ăn chính mình
        for b in snakebody[1:]:
            if snakepos[0] == b[0] and snakepos[1] == b[1]:
                game_over = True
                delaySpeed = 200
        # đường viền
        pygame.draw.rect(gameSurface,gray,(10,10,715,455),2)
        show_score()
    else:
        draw_button(gameSurface,clicked)
    
    if game_over == True:
        sfont = pygame.font.SysFont('consolas',80)
        ssurf = sfont.render('Game Over'.format(score),True,(200,0,0))
        gameSurface.blit(ssurf,(735 / 2 - ssurf.get_width()/2,475 / 2 - ssurf.get_height()/2 - 100))
        game_sure(clicked)
    
    if isPause == True:
        sfont = pygame.font.SysFont('consolas',80)
        ssurf = sfont.render('Game Pause',True,(200,0,0))
        gameSurface.blit(ssurf,(735 / 2 - ssurf.get_width()/2,475 / 2 - ssurf.get_height()/2 - 100))
        
    clicked = False
    pygame.display.update()