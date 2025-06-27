from PIL import Image, ImageDraw
import os

def create_hero_background(width, height, output_path, is_dark=False):
    """创建简洁的矩阵方格风格 hero 背景图片"""
    # 根据模式选择背景色
    if is_dark:
        bg_color = '#1F2937'  # 深色背景
        small_grid_color = '#374151'  # 深色小网格
        main_grid_color = '#4B5563'   # 深色主网格
    else:
        bg_color = '#F3F4F6'  # 浅色背景
        small_grid_color = '#E5E7EB'  # 浅色小网格
        main_grid_color = '#D1D5DB'   # 浅色主网格
    
    # 创建背景图片
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # 绘制网格背景
    grid_size = 12  # 网格大小（从20改为12，更细密）
    
    # 绘制垂直线
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill=small_grid_color, width=1)
    
    # 绘制水平线
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill=small_grid_color, width=1)
    
    # 添加一些稍微深一点的网格线作为主网格
    main_grid_size = grid_size * 6  # 每6个小格一个大格
    
    # 绘制主垂直线
    for x in range(0, width, main_grid_size):
        draw.line([(x, 0), (x, height)], fill=main_grid_color, width=2)
    
    # 绘制主水平线
    for y in range(0, height, main_grid_size):
        draw.line([(0, y), (width, y)], fill=main_grid_color, width=2)
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 保存图片
    image.save(output_path, 'PNG', quality=95)
    mode_text = "dark" if is_dark else "light"
    print(f'Created {mode_text} hero background: {output_path} ({width}x{height})')

def main():
    # 定义不同的尺寸
    sizes = [
        (1920, 1080),  # Full HD
        (1440, 900),   # 常见笔记本分辨率
        (1366, 768),   # 常见笔记本分辨率
        (1280, 720),   # HD
        (1024, 768),   # 平板
        (768, 1024),   # 平板竖屏
        (375, 812),    # iPhone X
        (414, 896),    # iPhone 11
    ]
    
    # 生成不同尺寸的 hero 背景（明暗两种模式）
    for width, height in sizes:
        # 生成浅色模式
        filename_light = f'hero-bg-{width}x{height}.png'
        output_path_light = f'public/images/{filename_light}'
        create_hero_background(width, height, output_path_light, is_dark=False)
        
        # 生成深色模式
        filename_dark = f'hero-bg-{width}x{height}-dark.png'
        output_path_dark = f'public/images/{filename_dark}'
        create_hero_background(width, height, output_path_dark, is_dark=True)
    
    # 生成默认的 hero-bg.png（浅色模式）
    create_hero_background(1920, 1080, 'public/images/hero-bg.png', is_dark=False)
    
    # 生成默认的深色模式
    create_hero_background(1920, 1080, 'public/images/hero-bg-dark.png', is_dark=True)

if __name__ == '__main__':
    main() 