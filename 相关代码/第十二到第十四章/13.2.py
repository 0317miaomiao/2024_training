import sys
import pygame
from random import randint 

class All_star:
    
    def __init__(self):
        # 初始化游戏
        pygame.init()
        
        # 控制帧率的方法
        self.clock = pygame.time.Clock()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 

        pygame.display.set_caption("Stars")
        
        # 创建星星编组
        self.stars = pygame.sprite.Group()
        
        # 设置随机放置的星星的数量
        self.star_number = 10
        
        self._create_fleet()   
    
    # 开始游戏的主循环
    def run_game(self):
        """开始主游戏循环"""
        while True:        
            self._update_screen()           
            self.clock.tick(60)
                
    def _create_fleet(self):
        """创建星星"""
        
        # 创建一个外星人，再不断添加，直到没有空间添加外星⼈为⽌
        # 外星⼈的间距为外星⼈的宽度和外星⼈的⾼度
        star = Star(self)
        star_width, star_height = star.rect.size 
        
        current_x = star_width
        current_y = star_height
        self.stars.add(star)
        
        for s in range(self.star_number):
            new_star = Star(self)
            # 随机设置x 与 y的位置
            x_position = randint(0, self.settings.screen_width - current_x)
            y_position = randint(0, self.settings.screen_height - current_y)
            new_star.x = x_position
            new_star.rect.x = x_position
            new_star.rect.y = y_position
            self.stars.add(new_star)
        
    def _update_screen(self):
        # 更新屏幕上的图像，并切换到新屏幕
        self.screen.fill(self.settings.bg_color)
        
        # 将编组内的每个元素画到指定的屏幕上
        self.stars.draw(self.screen) 

        # 让最近绘制的屏幕可见
        pygame.display.flip()
    
if __name__ == 'main':
    # 创建游戏实例并运行
    ai = All_star()
    ai.run_game()

import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """表示单个星星的类"""
    
    def __init__(self, ai_game):
        """初始化星星并且设置起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        
        # 加载星星的图像并且设置其rect属性
        self.original_image = pygame.image.load('star.png')
        
        # 调整图像大小，可以设置想要的宽度和高度
        # 修改为你希望的尺寸
        scale_width, scale_height = 50, 100  
        self.image = pygame.transform.scale(self.original_image, (scale_width, scale_height))
        self.rect = self.image.get_rect()
        
        # 每个星星最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 储存星星的精确水平位置
        self.x = float(self.rect.x)

class Settings: 
    """存储游戏《外星⼈⼊侵》中所有设置的类""" 
    def __init__(self): 
 
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color = (230, 230, 230)
