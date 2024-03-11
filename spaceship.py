import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
#모든컴퓨터에서 같은속도로 실행되기 위해서
image=pygame.image.load('./img/ship.bmp')
image_rect=image.get_rect()
#이미지를 사각형에 대입

#2+ 비행선을 하단중앙에 놓기위한 코드
screen_rect=screen.get_rect()
image_rect.midbottom=screen_rect.midbottom

moving_right=False
moving_left=False
moving_up=False
moving_down=False

bullet_speed=2.0
bullet_width=3
bullet_height=15
bullet_color=(0, 0, 0)
#bullet_rect=pygame.Rect(screen.get_width()/2,screen.get_height(),bullet_width,bullet_height)
#screen_bullet=screen.get_rect()
#bullet_rect.midbottom=screen_bullet.midbottom
bullets=[]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
            #sys.exit()->위와 같은 종료문
        elif event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                moving_right=True
                # image_rect.x +=10
            elif event.key ==pygame.K_LEFT:
                moving_left=True
            elif event.key==pygame.K_UP:
                moving_up=True
            elif event.key==pygame.K_DOWN:
                moving_down=True
            elif event.key==pygame.K_SPACE:
                bullet_x=image_rect.centerx-bullet_width/2
                bullet_y=image_rect.top
                bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))
        elif event.type ==pygame.KEYUP:
            if event.key ==pygame.K_RIGHT:
                moving_right=False
            elif event.key==pygame.K_LEFT:
                moving_left=False
            elif event.key==pygame.K_UP:
                moving_up=False
            elif event.key==pygame.K_DOWN:
                moving_down=False
        



    screen.fill("lightpink")  

    screen.blit(image, image_rect)
    # screen.fill(settings.bg_color)
    if moving_right:
        image_rect.x +=5
    if moving_left:
        image_rect.x -=5
    if moving_up:
        image_rect.y -=5
    if moving_down:
        image_rect.y +=5

    pygame.display.flip()  
    clock.tick(60)  

    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet) 
        bullet.y-=bullet_speed
        if bullet.y<0:
            bullets.remove(bullet)