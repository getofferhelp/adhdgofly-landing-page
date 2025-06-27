from PIL import Image
import cairosvg
import io
import os

def svg_to_png(svg_path, size):
    """将 SVG 转换为指定尺寸的 PNG"""
    # 使用 cairosvg 将 SVG 转换为 PNG
    png_data = cairosvg.svg2png(url=svg_path, output_width=size, output_height=size)
    return Image.open(io.BytesIO(png_data))

def create_favicon():
    """创建 favicon 文件"""
    svg_path = 'public/images/logo.svg'
    
    # 确保输出目录存在
    os.makedirs('public', exist_ok=True)
    
    # 生成不同尺寸的图标
    sizes = [16, 32, 48, 64, 128, 256]
    images = []
    
    print("正在生成不同尺寸的图标...")
    
    for size in sizes:
        try:
            img = svg_to_png(svg_path, size)
            images.append(img)
            print(f"✓ 生成 {size}x{size} 图标")
        except Exception as e:
            print(f"✗ 生成 {size}x{size} 图标失败: {e}")
            return
    
    # 保存 ICO 文件（包含多个尺寸）
    try:
        # 保存为 ICO 文件
        ico_path = 'public/favicon.ico'
        images[0].save(ico_path, format='ICO', sizes=[(size, size) for size in sizes])
        print(f"✓ 保存 favicon.ico 到 {ico_path}")
        
        # 保存为 PNG 文件（用于现代浏览器）
        png_path = 'public/favicon.png'
        images[-1].save(png_path, format='PNG')  # 使用最大尺寸
        print(f"✓ 保存 favicon.png 到 {png_path}")
        
        # 生成不同尺寸的 PNG 文件
        for i, size in enumerate(sizes):
            png_file = f'public/favicon-{size}x{size}.png'
            images[i].save(png_file, format='PNG')
            print(f"✓ 保存 {png_file}")
            
    except Exception as e:
        print(f"✗ 保存文件失败: {e}")

def create_apple_touch_icon():
    """创建 Apple Touch Icon"""
    svg_path = 'public/images/logo.svg'
    
    try:
        # 生成 180x180 的 Apple Touch Icon
        img = svg_to_png(svg_path, 180)
        apple_icon_path = 'public/apple-touch-icon.png'
        img.save(apple_icon_path, format='PNG')
        print(f"✓ 保存 Apple Touch Icon 到 {apple_icon_path}")
        
    except Exception as e:
        print(f"✗ 生成 Apple Touch Icon 失败: {e}")

def create_manifest_icons():
    """创建 PWA manifest 图标"""
    svg_path = 'public/images/logo.svg'
    
    # PWA 需要的图标尺寸
    pwa_sizes = [192, 512]
    
    for size in pwa_sizes:
        try:
            img = svg_to_png(svg_path, size)
            manifest_icon_path = f'public/icon-{size}x{size}.png'
            img.save(manifest_icon_path, format='PNG')
            print(f"✓ 保存 PWA 图标 {size}x{size} 到 {manifest_icon_path}")
            
        except Exception as e:
            print(f"✗ 生成 PWA 图标 {size}x{size} 失败: {e}")

def main():
    print("开始生成 favicon 文件...")
    
    # 检查 SVG 文件是否存在
    if not os.path.exists('public/images/logo.svg'):
        print("✗ 找不到 logo.svg 文件")
        return
    
    # 生成所有图标
    create_favicon()
    create_apple_touch_icon()
    create_manifest_icons()
    
    print("\n🎉 所有图标生成完成！")
    print("\n生成的文件:")
    print("- favicon.ico (多尺寸 ICO 文件)")
    print("- favicon.png (高分辨率 PNG)")
    print("- favicon-16x16.png 到 favicon-256x256.png (不同尺寸)")
    print("- apple-touch-icon.png (iOS 设备)")
    print("- icon-192x192.png 和 icon-512x512.png (PWA 支持)")

if __name__ == '__main__':
    main() 