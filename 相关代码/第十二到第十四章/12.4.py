class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.rocket_speed = 1.5

import pygame

class Rocket:
    """管理火箭的类"""
    def __init__(self, ai_game):
        """初始化火箭并且设置起始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # 加载火箭图像并获取其rect
        self.image = pygame.image.load('image.png')
        self.rect = self.image.get_rect()
        
        # 每个新火箭都放在屏幕中央
        self.rect.center = self.screen_rect.center
        
        # 在火箭中的属性储存最小值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """根据移动标志调整火箭位置"""
        # 更新火箭的x和y值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
            
        # 根据self.x和self.y更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image, self.rect)


import sys
import pygame

class Rocket_main:
    
    def __init__(self):
        # 初始化游戏
        pygame.init()
        
        # 控制帧率的方法
        self.clock = pygame.time.Clock()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 

        pygame.display.set_caption("Rocket")
        
        self.rocket = Rocket(self)
    
    # 开始游戏的主循环
    def run_game(self):
        """开始主游戏循环"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()           
            self.clock.tick(60)
    
    # 相应按键与鼠标事件
    def _check_events(self):
        # 监听鼠标与键盘
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN: 
                    self._check_keydown_events(event) 
                elif event.type == pygame.KEYUP: 
                    self._check_keyup_events(event) 
    
    # 进行重构
    def _check_keydown_events(self, event): 
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT: 
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q: 
            sys.exit() 
    
    def _check_keyup_events(self, event): 
        if event.key == pygame.K_RIGHT: 
            self.rocket.moving_right = False 
        elif event.key == pygame.K_LEFT: 
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
            
    def _update_screen(self):
        # 更新屏幕上的图像，并切换到新屏幕
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme() 

        # 让最近绘制的屏幕可见
        pygame.display.flip()
    
if __name__ == 'main':
    # 创建游戏实例并运行
    ai = Rocket_main()
    ai.run_game()
