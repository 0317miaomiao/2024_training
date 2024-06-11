import sys
import pygame
# 飞船撞到外星人后能暂停一会
from time import sleep

class AlienInvasion:
    
    def __init__(self):
        # 初始化游戏
        pygame.init()
        
        # 控制帧率的方法
        self.clock = pygame.time.Clock()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 

        pygame.display.set_caption("Alien Invasion")
        
        # 创建⼀个⽤于存储游戏统计信息的实例
        self.stats = GameStats(self) 
        
        self.ship = Ship(self)
        
        # 这个的作用是创造一个组，把所有的创建的子弹都放进来
        # 可以看成放成了一个列表的形式，然后可以对其中的所有
        # 元素进行调用函数
        self.bullets = pygame.sprite.Group()
        
        # 在创建外星人时与创建子弹同理
        self.aliens = pygame.sprite.Group() 
        
        self._create_fleet() 
        
        # 游戏启动后处于活动状态
        self.game_active = True
    
    # 开始游戏的主循环
    def run_game(self):
        """开始主游戏循环"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens() 
            self._update_screen()           
            self.clock.tick(60)
    
    # 相应按键与鼠标事件
    def _check_events(self):
        # 监听鼠标与键盘
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN: 
                    self._check_keydown_events(event) 
                elif event.type == pygame.KEYUP: 
                    self._check_keyup_events(event) 
    
    # 进行重构
    def _check_keydown_events(self, event): 
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN: 
            self.ship.moving_down = True
        elif event.key == pygame.K_q: 
            sys.exit() 
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event): 
        if event.key == pygame.K_UP: 
            self.ship.moving_up = False 
        elif event.key == pygame.K_DOWN: 
            self.ship.moving_down = False
            
    def _fire_bullet(self):
        """创建子弹并且开火"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """更新子弹位置并且删除已经消失的子弹"""
        # 更新位置
        self.bullets.update() 
            
        # 删除已经消失的子弹
        for bullet in self.bullets.copy(): 
            if bullet.rect.right > self.settings.screen_width:
                self.bullets.remove(bullet) 
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        # 检查是否有⼦弹击中了外星⼈
        # 如果是，就删除相应的⼦弹和外星⼈
        collisions = pygame.sprite.groupcollide( self.bullets, self.aliens, True, True)
        if not self.aliens:
            # 删除现有的⼦弹并创建⼀个新的外星舰队
            self.bullets.empty()
            self._create_fleet()
            
    def _create_fleet(self):
        """创建一个外星舰队"""
        
        # 创建一个外星人，再不断添加，直到没有空间添加外星⼈为⽌
        # 外星⼈的间距为外星⼈的宽度和外星⼈的⾼度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        
        current_x = self.settings.screen_width - alien_width
        current_y = alien_height
        while current_x >  (self.settings.screen_width - 5*alien_width):
            
            while current_y < (self.settings.screen_height - alien_height):
                self._creat_alien(current_x, current_y)
                current_y += 3 * alien_width
            
            # 添加⼀⾏外星⼈后，重置y 值并递减x 值
            current_y = alien_height 
            current_x -= 2 * alien_width
    
    def _creat_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _check_fleet_edges(self): 
        """在有外星⼈到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break 
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _check_aliens_left(self): 
        """检查是否有外星⼈到达了屏幕的下边缘""" 
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0: 
                # 像⻜船被撞到⼀样进⾏处理
                self._ship_hit() 
                break
        
    def _update_aliens(self): 
        """更新外星舰队中所有外星⼈的位置"""
        self._check_fleet_edges() 
        self.aliens.update() 
        
        # 检测外星⼈和⻜船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        # 检查是否有外星⼈到达了屏幕的下边缘
        self._check_aliens_left() 
            
    def _ship_hit(self): 
        """响应⻜船和外星⼈的碰撞""" 
        # 将ships_left 减1
        if self.stats.ships_left > 0: 
            self.stats.ships_left -= 1 

            # 清空外星⼈列表和⼦弹列表
            self.bullets.empty()
            self.aliens.empty()

            # 创建⼀个新的外星舰队，并将⻜船放在屏幕底部的中央
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        
        else:
            self.game_active = False
        
        
    def _update_screen(self):
        # 更新屏幕上的图像，并切换到新屏幕
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites(): 
            bullet.draw_bullet()
        self.ship.blitme() 
        
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
        self.ship_speed = 1.5
        self.ship_limit = 3 
        
        # 加入子弹设置
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # 外星⼈设置
        self.alien_speed = 1.0 
        self.fleet_drop_speed = 10 
        
        # fleet_direction 为1 表⽰向上移动，为-1 表⽰向下移动
        self.fleet_direction = 1

import pygame

class Ship: 
    def __init__(self, ai_game):
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()
        
        # 加载⻜船图像并获取其外接矩形
        self.original_image = pygame.image.load('image.png')
        
        # 调整图像大小，可以设置想要的宽度和高度
        # 修改为你希望的尺寸
        scale_width, scale_height = 50, 100  
        self.image = pygame.transform.scale(self.original_image, (scale_width, scale_height))
        
        # 顺时针转90度
        self.image = pygame.transform.rotate(self.image, -90)
        
        self.rect = self.image.get_rect()
        
        
        
        # 每艘新⻜船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midleft
        
        # 在⻜船的属性x 中存储⼀个浮点数
        self.y = float(self.rect.y)
        
        # 移动标志（⻜船⼀开始不移动）
        self.moving_up = False
        self.moving_down = False 
        
        self.settings = ai_game.settings
        
    def update(self): 
        # 更新⻜船⽽不是rect对象的 x 值
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed 
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed 
         # 根据self.y更新rect对象
        self.rect.y = self.y
        
        # 根据移动标志调整⻜船的位置
        if self.moving_down: 
            self.rect.y += self.settings.ship_speed 
        if self.moving_up: 
            self.rect.y -= self.settings.ship_speed
        
        # 根据self.y 更新rect 的值对象
        self.rect.y = self.y 

    def blitme(self):
        # 在指定位置绘制⻜船
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """将⻜船放在屏幕底部的中央"""
        self.rect.midbottom = self.screen_rect.midleft
        self.y = float(self.rect.y)

import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船所有发射的子弹类"""
    
    def __init__(self, ai_game):
        """在飞船当前位置创建子弹"""
        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color
        
        # 在(0,0)处创建⼀个表⽰⼦弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0,self.settings.bullet_height,self.settings.bullet_width )
        self.rect.midtop = ai_game.ship.rect.midright
        
        # 存储⽤浮点数表⽰的⼦弹位置
        self.x = float(self.rect.x)
        
    def update(self):
        """更新子弹的位置"""
        self.x += self.settings.bullet_speed
        # 更新表⽰⼦弹的 rect 的位置
        self.rect.x = self.x
        
    def draw_bullet(self):
        """在屏幕上绘制⼦弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

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
        self.rect.x = ai_game.settings.screen_width - 50
        self.rect.y = self.rect.height
        
        # 储存外行星人的精确水平位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def check_edges(self):
        """如果外星⼈位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect() 
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0) 
    
    def update(self): 
        """向下移动外星人"""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y

class GameStats:
    """跟踪游戏的统计信息"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """初始化在游戏运⾏期间可能变化的统计信息""" 
        self.ships_left = self.settings.ship_limit
