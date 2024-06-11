## 用外星人代替雨滴了

import sys

import pygame

class AlienInvasion:
    
    def __init__(self):
        # 初始化游戏
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 

        pygame.display.set_caption("Alien Invasion")
        
        # 这个的作用是创造一个组，把所有的创建的子弹都放进来
        # 可以看成放成了一个列表的形式，然后可以对其中的所有
        # 元素进行调用函数
        
        # 在创建外星人时与创建子弹同理
        self.aliens = pygame.sprite.Group() 
        
        self._create_fleet() 
    
    # 开始游戏的主循环
    def run_game(self):
        """开始主游戏循环"""
        while True:
            self._check_events()
            self._update_aliens() 
            self._update_screen()  
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _create_fleet(self):
        """创建一个外星舰队"""
        
        # 创建一个外星人，再不断添加，直到没有空间添加外星⼈为⽌
        # 外星⼈的间距为外星⼈的宽度和外星⼈的⾼度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        
        current_x = alien_width
               
        while current_x < (self.settings.screen_width - 2*alien_width):
            self._creat_alien(current_x)
            current_x += 2 * alien_width
    
    def _creat_alien(self, x_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)
    
    def _check_fleet_edges(self): 
        """在有外星⼈到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break 
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y = 100
        
        
    def _update_aliens(self): 
        """更新外星舰队中所有外星⼈的位置"""
        self._check_fleet_edges() 
        self.aliens.update() 
        
    def _update_screen(self):
        # 更新屏幕上的图像，并切换到新屏幕
        self.screen.fill(self.settings.bg_color)
        
        # 将编组内的每个元素画到指定的屏幕上
        self.aliens.draw(self.screen) 

        # 让最近绘制的屏幕可见
        pygame.display.flip()
    
if __name__ == 'main':
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()

class Settings: 
    """存储游戏《外星⼈⼊侵》中所有设置的类""" 
    def __init__(self): 
 
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color = (230, 230, 230)
        
        # 外星⼈设置
        self.alien_speed = 1.0 
        #self.fleet_drop_speed = self.screen_height- 150

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_game):
        """初始化外星人并且设置起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # 加载外星人的图像并且设置其rect属性
        self.original_image = pygame.image.load('alien.png')
        
        # 调整图像大小，可以设置想要的宽度和高度
        # 修改为你希望的尺寸
        scale_width, scale_height = 50, 100  
        self.image = pygame.transform.scale(self.original_image, (scale_width, scale_height))
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 储存外行星人的精确水平位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def check_edges(self):
        """如果外星⼈位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect() 
        return (self.rect.bottom >= screen_rect.bottom)
    
    def update(self): 
        """向下移动外星人"""
        self.y += self.settings.alien_speed 
        self.rect.y = self.y 
        
    
