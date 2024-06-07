import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Background Window")
    
    # 设置背景颜色，RGB值为（0, 0, 255）对应蓝色
    blue_bg_color = (0, 0, 255)
    
    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # 填充屏幕背景颜色
        screen.fill(blue_bg_color)
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
