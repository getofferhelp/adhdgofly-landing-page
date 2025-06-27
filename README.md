# vue-demo

一个基于 Vue 3 + TypeScript 的图标工具集合项目。

## 功能特性

### 1. Font Awesome 图标库

- 支持 Solid、Regular 和 Brands 三种样式的图标
- 实现图标搜索和分类展示
- 支持复制图标名称和 HTML 代码
- 响应式布局设计

### 2. Unicode 字符工具

- 支持多个 Unicode 字符块的展示：
  - 基础拉丁字符
  - 货币符号
  - 箭头符号
  - 数学运算符
  - 制表符
  - 几何图形
  - 其他特殊符号
- 分类浏览和搜索功能
- 支持复制字符和编码

### 3. Unicode Emoji 工具

- 完整的 Unicode Emoji 表情集合
- 按类别分类展示
- 支持关键词搜索
- 支持复制表情和名称

### 4. 主题切换

- 支持亮色/暗色主题切换
- 主题切换动画效果
- 自动保存主题偏好

## 技术栈

- Vue 3
- TypeScript
- Vue Router
- Pinia
- Font Awesome
- Vite

## 项目结构

```
tree
src/
├── components/ # 组件目录
│ ├── BaseIcon.vue # 基础图标组件
│ ├── FontAwesome.vue # Font Awesome 图标展示
│ ├── IconUnicode.vue # Unicode 字符展示
│ └── IconUnicodeEmoji.vue # Emoji 展示
├── data/ # 数据文件
│ ├── icons.ts # 图标相关数据
│ └── unicodeEmojiIcons.ts # Emoji 数据
├── config/ # 配置文件
│ └── icons.ts # 图标配置
├── router/ # 路由配置
└── assets/ # 静态资源
```

## 开发指南

### 安装依赖

```
bash
npm install
```

### 运行项目

```
bash
npm run dev
```

### 代码检查和格式化

```
bash
npm run lint
npm run format
```

## 浏览器支持

- 现代浏览器
- Chrome/Edge/Firefox/Safari 最新版本
- 不支持 IE 浏览器

## 许可证

MIT License

# ADHD GO FLY Landing Page

ADHD GO FLY 官方网站着陆页，为 ADHD 群体提供专业的多语言阅读编辑工具。

## 功能特性

### 🌟 多语言支持
- 支持中文、英文、法文、西班牙文、俄文、日文六种语言
- 动态语言切换，实时更新页面内容
- 完整的国际化配置

### 🎨 响应式设计
- 完美适配桌面端、平板和移动设备
- 支持明暗模式切换
- 响应式背景图片，根据屏幕尺寸自动选择

### 🔍 SEO 优化
- 动态 meta 标签更新
- Open Graph 标签支持
- 结构化数据（Schema.org）
- 多语言 SEO 优化

### ♿ 可访问性
- 键盘导航支持
- 屏幕阅读器友好
- 高对比度设计
- 焦点管理优化

### 📱 PWA 支持
- 自动生成的 favicon 图标
- PWA manifest 配置
- 离线缓存支持

## 技术栈

- Vue 3 + TypeScript
- Vue Router
- Vue I18n
- Tailwind CSS
- Vite
- PostCSS

## 项目结构

```
adhdgofly-landing-page/
├── public/           # 静态资源
│   ├── images/       # 图片资源
│   ├── fonts/        # 字体文件
│   └── manifest.json # PWA 配置
├── src/
│   ├── components/   # Vue 组件
│   ├── views/        # 页面视图
│   ├── locales/      # 国际化文件
│   └── assets/       # 样式和资源
├── scripts/          # 构建脚本
├── _headers          # Cloudflare 安全头
├── _redirects        # Cloudflare 重定向规则
└── index.html        # 入口文件
```

## 开发指南

### 安装依赖

```bash
npm install
```

### 本地开发

```bash
npm run dev
```

### 构建生产版本

```bash
npm run build
```

### 预览构建结果

```bash
npm run preview
```

## 部署到 Cloudflare Pages

### 1. 准备部署

项目已经配置好 Cloudflare Pages 所需的文件：
- `_headers` - 安全头和缓存配置
- `_redirects` - 路由重定向规则
- `public/manifest.json` - PWA 配置

### 2. 部署步骤

1. **创建 GitHub 仓库**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/adhdgofly-landing-page.git
   git push -u origin main
   ```

2. **连接 Cloudflare Pages**
   - 登录 [Cloudflare Dashboard](https://dash.cloudflare.com)
   - 进入 Pages 页面
   - 点击 "Create a project"
   - 选择 "Connect to Git"
   - 选择你的 GitHub 仓库

3. **配置构建设置**
   - **Framework preset**: Vite
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
   - **Root directory**: `/` (留空)

4. **环境变量**（可选）
   - 如果需要，可以添加环境变量

5. **部署**
   - 点击 "Save and Deploy"
   - 等待构建完成

### 3. 自定义域名

部署完成后，可以在 Pages 设置中添加自定义域名：
- 进入项目设置
- 选择 "Custom domains"
- 添加你的域名（如 `adhdgofly.com`）

## 性能优化

- 图片懒加载
- 静态资源缓存
- 代码分割
- 压缩优化
- CDN 加速

## 浏览器支持

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

- 官网：https://adhdgofly.online
- GitHub：https://github.com/yourusername/adhdgofly-landing-page
