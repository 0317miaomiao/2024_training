import pygame

class Settings:
    """存储游戏的所有设置的类"""
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 屏幕背景色设为浅灰色

class GameCharacter:
    """管理游戏角色的类"""
    def __init__(self, ai_game):
        """初始化角色并设置其起始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # 加载角色图像并获取其外接矩形
        self.image = pygame.image.load('character.png')
        self.rect = self.image.get_rect()
        
        # 将每个新角色放在屏幕底部中央
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        """在指定位置绘制角色"""
        self.screen.blit(self.image, self.rect)

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Game Character Display")

    # 创建一个游戏角色
    character = GameCharacter(ai_settings)
    
    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        character.blitme()
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
