import pygame
import sys

# 총알 클래스
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 3, 15)  # 총알의 크기와 위치
        self.color = (0, 0, 0)  # 총알 색상

    def move(self, speed):
        self.rect.y -= speed  # 총알을 위로 이동시킴

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)  # 총알을 화면에 그림

# 총알을 관리하는 함수
def handle_bullets(bullets, bullet_speed):
    new_bullets = []

    for bullet in bullets:
        bullet.move(bullet_speed)  # 총알 이동
        if bullet.rect.y >= 0:
            new_bullets.append(bullet)

    return new_bullets

# 게임 실행 함수
def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    image = pygame.image.load('./img/ship.bmp')
    image_rect = image.get_rect()
    screen_rect = screen.get_rect()
    image_rect.midbottom = screen_rect.midbottom

    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False

    bullet_speed = 5
    bullets = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                elif event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_UP:
                    moving_up = True
                elif event.key == pygame.K_DOWN:
                    moving_down = True
                elif event.key == pygame.K_SPACE:
                    bullet_x = image_rect.centerx - 1
                    bullet_y = image_rect.top
                    bullet = Bullet(bullet_x, bullet_y)
                    bullets.append(bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                elif event.key == pygame.K_LEFT:
                    moving_left = False
                elif event.key == pygame.K_UP:
                    moving_up = False
                elif event.key == pygame.K_DOWN:
                    moving_down = False

        screen.fill("lightpink")

        screen.blit(image, image_rect)

        if moving_right:
            image_rect.x += 5
        if moving_left:
            image_rect.x -= 5
        if moving_up:
            image_rect.y -= 5
        if moving_down:
            image_rect.y += 5

        bullets = handle_bullets(bullets, bullet_speed)  # 총알 관리

        for bullet in bullets:
            bullet.draw(screen)  # 총알 그리기

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
