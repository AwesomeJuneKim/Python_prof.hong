import pygame

class Ship:
    def __init__(self,ai_game):
        #우주선의 시작위치 설정
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        
        #우주선의 이미지 불러옴
        self.image=pygame.image.load('./img/ship.bmp')
        self.rect=self.image.get_rect()
        
        #우주선의 초기위치 하단 중앙
        self.rect.midbottom=self.screen_rect.midbottom
    def blitme(self):
        #우주선을 현재위치에 그린다.
        #rectangle을 그려서 그 안에 image를 넣는 함수
        #블릿메서드를 이용해서 biltme함수를 새로 만듦
        self.screen.blit(self.image,self.rect)