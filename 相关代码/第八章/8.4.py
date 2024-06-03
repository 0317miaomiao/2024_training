def make_shirt(size='L', message='I love Python'):
    """显示T恤的尺码和要印的字样"""
    print(f"制作一件尺码为{size}的T恤，上面印着：“{message}”。")

# 制作一件默认字样的大号T恤
make_shirt()

# 制作一件默认字样的中号T恤
make_shirt(size='M')

# 制作一件印有其他字样的T恤（尺码不关紧要）
make_shirt(message='Coding Rocks!', size='S')
