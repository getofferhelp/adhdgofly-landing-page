from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(width, height, text, output_path):
    # 创建一个浅灰色背景的图片
    image = Image.new('RGB', (width, height), '#F3F4F6')
    draw = ImageDraw.Draw(image)
    
    # 绘制网格背景
    for x in range(0, width, 20):
        draw.line([(x, 0), (x, height)], fill='#E5E7EB', width=1)
    for y in range(0, height, 20):
        draw.line([(0, y), (width, y)], fill='#E5E7EB', width=1)
    
    # 添加文字
    try:
        # 尝试加载系统字体
        font = ImageFont.truetype('Arial', 32)
    except:
        # 如果找不到 Arial，使用默认字体
        font = ImageFont.load_default()
    
    # 计算文字位置使其居中
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # 绘制文字背景
    padding = 20
    draw.rectangle([
        (x - padding, y - padding),
        (x + text_width + padding, y + text_height + padding)
    ], fill='#FFFFFF')
    
    # 绘制文字
    draw.text((x, y), text, fill='#4B5563', font=font)
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 保存图片
    image.save(output_path, 'PNG')

def main():
    # 设置图片尺寸（16:9 比例）
    width = 1280
    height = 720
    
    # 生成三个占位图
    placeholders = [
        ('Editor Mode', 'public/images/screenshots/editor.png'),
        ('AI Processing', 'public/images/screenshots/ai.png'),
        ('Focus Mode', 'public/images/screenshots/focus.png')
    ]
    
    for text, path in placeholders:
        create_placeholder(width, height, text, path)
        print(f'Created placeholder image: {path}')

if __name__ == '__main__':
    main() 