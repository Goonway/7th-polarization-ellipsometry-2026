#!/usr/bin/env python3
"""
网站更新辅助脚本 - 在添加新图片或修改内容后运行此脚本
功能：
1. 为新增 img 标签自动添加 loading="lazy"
2. 将新增的相对路径资源链接(css/js/images/downloads)替换为 jsDelivr CDN 绝对路径
3. 显示需要清理 jsDelivr CDN 缓存的文件列表

使用方法：
    python3 update_cdn.py

前提条件：
- 已安装 Python 3（macOS 自带）
- 新图片已放入 images/ 目录
- HTML 文件已编辑完成
"""

import os, re, sys

CDN = "https://cdn.jsdelivr.net/gh/Goonway/7th-polarization-ellipsometry-2026@main"
WEBSITE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    os.chdir(WEBSITE_DIR)
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    total_lazy = 0
    total_cdn = 0
    changed_files = []

    for fname in sorted(html_files):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content

        # 1. 为没有 loading 属性的 img 标签添加 loading="lazy"
        def add_lazy(m):
            tag = m.group(0)
            if 'loading=' in tag:
                return tag
            return tag.replace('<img ', '<img loading="lazy" ', 1)
        content = re.sub(r'<img\s[^>]*>', add_lazy, content)
        lazy_count = content.count('loading="lazy"') - original.count('loading="lazy"')

        # 2. 将相对路径替换为 CDN 绝对路径（只处理未被替换的新增内容）
        patterns = [
            (r'href="css/', f'href="{CDN}/css/'),
            (r'src="js/', f'src="{CDN}/js/'),
            (r'src="images/', f'src="{CDN}/images/'),
            (r'href="downloads/', f'href="{CDN}/downloads/'),
        ]
        cdn_count = 0
        for pattern, replacement in patterns:
            content, n = re.subn(pattern, replacement, content)
            cdn_count += n

        if content != original:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(content)
            changed_files.append(fname)
            total_lazy += lazy_count
            total_cdn += cdn_count
            parts = []
            if lazy_count: parts.append(f'+{lazy_count} lazy')
            if cdn_count: parts.append(f'+{cdn_count} CDN')
            print(f'  {fname}: {", ".join(parts)}')
        else:
            print(f'  {fname}: no changes')

    print(f'\n总计: {total_lazy} lazy loading + {total_cdn} CDN URLs')

    # 3. 提示后续操作
    print('\n' + '='*50)
    print('后续操作步骤：')
    print('='*50)
    print('1. 压缩新图片（可选）：')
    print('   sips -Z 320 -s format png input.png --out output.png')
    print('   sips -Z 800 -s formatOptions 70 input.jpg --out output.jpg')
    print()
    print('2. 提交并推送到 GitHub：')
    print('   git add -A && git commit -m "更新内容" && git push')
    print()
    print('3. 清除 jsDelivr CDN 缓存（等待1-2分钟后）：')
    print('   访问 https://purge.jsdelivr.net/gh/Goonway/7th-polarization-ellipsometry-2026@main/')
    print('   在 URL 后面加上需要刷新的文件路径')
    print('   例如: ...@main/images/专题1/张三.png')
    print()
    print('   或者直接在浏览器中访问带新时间戳的 CDN URL 触发刷新')
    print()
    print('4. 验证网站：')
    print('   https://goonway.github.io/7th-polarization-ellipsometry-2026/')

if __name__ == '__main__':
    main()
