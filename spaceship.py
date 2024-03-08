import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
#모든컴퓨터에서 같은속도로 실행되기 위해서
image=pygame.image.load('./img/ship.bmp')
rect=image.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
            #sys.exit()->위와 같은 종료문



    screen.fill("lightpink")  

    screen.blit(image, rect)

    pygame.display.flip()  
    clock.tick(60)         