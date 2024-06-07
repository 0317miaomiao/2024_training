import sys
import pygame

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    
    # 设置屏幕尺寸
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Key Events")
    
    # 设置背景颜色
    bg_color = (255, 255, 255)  # 白色背景
    
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 打印按键的属性 event.key
                print(f"Key pressed: {event.key}")
        
        # 填充屏幕背景色
        screen.fill(bg_color)
        
        # 刷新图像，使其可见
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
