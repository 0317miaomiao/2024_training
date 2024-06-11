# 重构
from random import choice

class RandomWalk:
    """生成随机游走数据的类"""
    
    def __init__(self, num_points = 5000):
        # 初始化游走属性
        self.num_points = num_points
        
        # 所有的点从（0，0）出发
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """生成随机游走的点"""
        
        # 不停的走，直到到达指定的长度:
        while len(self.x_values) < self.num_points:
            
            #决定前进的方向与距离
            x_step = self.get_step() 
 
            y_step = self.get_step()
            
            #拒绝原地踏步
            if x_step ==0 and y_step == 0:
                continue
            
            # 计算下一个点的x坐标值与y坐标值
            x = self.x_values[-1] + x_step 
            y = self.y_values[-1] + y_step 

            self.x_values.append(x) 
            self.y_values.append(y)
        
    def get_step(self):
        """确定每步所走的步长"""
        
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        return direction*distance
