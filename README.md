# 会议网站模板 - 部署指南

## 技术栈

| 功能 | 工具 | 费用 |
|------|------|------|
| 网站展示与托管 | GitHub Pages | 免费 |
| 注册/住宿/发票表单 | Tally.so | 免费版够用 |
| 投稿与审稿 | OpenReview | 免费 |
| 域名（可选） | 自行购买 | ~55 元/年 |

## 文件结构

```
conference-website/
├── index.html          # 主页面（所有内容在此）
├── css/
│   └── style.css       # 样式文件
├── js/
│   └── main.js         # 交互脚本
├── images/             # 图片目录（放背景图、校徽、嘉宾照片等）
└── downloads/          # 下载文件目录（摘要模板、邀请函等）
```

## 自定义步骤

### 1. 替换占位内容

打开 `index.html`，搜索 `[占位]`，逐一替换为实际信息：
- 会议名称、主题、时间、地点
- 主办/协办单位名称及校徽
- 学术委员会成员姓名、职称、单位及照片
- 征稿主题
- 注册费用
- 酒店信息
- 会务组联系方式

### 2. 替换图片

将以下图片放入 `images/` 目录：

| 占位位置 | 建议文件名 | 尺寸建议 |
|----------|-----------|----------|
| 首页横幅背景 | hero-bg.jpg | 1920×600px |
| 校徽 | logo-1.png, logo-2.png | 120×120px |
| 嘉宾照片 | speaker-1.jpg ~ speaker-N.jpg | 200×200px（正方形） |
| 会议地点照片 | venue.jpg | 600×400px |
| 网站Logo | header-logo.png | 36×36px |

然后在 `index.html` 中将占位 div 替换为 `<img>` 标签。

### 3. 配置 Tally.so 表单

1. 访问 [tally.so](https://tally.so) 注册（免费）
2. 创建以下表单：
   - **注册表单**：姓名、单位、身份、邮箱、电话、是否需要住宿、是否需要发票
   - **发票信息表单**：抬头、税号、邮箱、发票类型
   - **住宿需求表单**：入住日期、离店日期、房型偏好
3. 发布表单后点击 **Embed** 获取嵌入代码
4. 在 `index.html` 中搜索 `YOUR_FORM_ID`，将注释中的 iframe 取消注释并替换 ID

### 4. 配置 OpenReview

1. 访问 [openreview.net](https://openreview.net) 注册
2. 创建会议组（Group），设置投稿截止日期、审稿规则等
3. 在 `index.html` 中搜索 `你的会议ID`，替换为实际的 OpenReview 会议链接

### 5. 添加下载文件

将以下文件放入 `downloads/` 目录：
- `abstract-template.docx` - 摘要模板
- `invitation-letter.docx` - 邀请函模板
- `conference-brochure.pdf` - 会议手册
- `registration-guide.pdf` - 参会指南

## 部署到 GitHub Pages

### 方法一：网页上传（无需安装任何工具）

1. 注册/登录 [GitHub](https://github.com)
2. 点击右上角 **+** → **New repository**
3. 仓库名填写：`conference-2026`（或任意名称）
4. 选择 **Public**，点击 **Create repository**
5. 点击 **uploading an existing file** 链接
6. 将 `conference-website/` 目录下的所有文件和文件夹拖入
7. 点击 **Commit changes**
8. 进入仓库 **Settings** → 左侧 **Pages**
9. **Source** 选择 **main** 分支，文件夹选 **/ (root)**
10. 点击 **Save**，等待 1-2 分钟
11. 访问 `https://你的用户名.github.io/conference-2026/`

### 方法二：Git 命令行推送

```bash
# 初始化仓库
cd conference-website
git init
git add .
git commit -m "会议网站初始版本"

# 关联 GitHub 远程仓库
git remote add origin https://github.com/你的用户名/conference-2026.git
git branch -M main
git push -u origin main

# 然后在 GitHub 仓库 Settings → Pages 中开启
```

### 配置自定义域名（可选）

1. 购买域名（如阿里云、腾讯云，约 55 元/年）
2. 在域名 DNS 设置中添加 CNAME 记录：
   - 类型：CNAME
   - 主机记录：www（或 @）
   - 记录值：你的用户名.github.io
3. 在 GitHub 仓库 Settings → Pages → Custom domain 中填入域名
4. 在仓库根目录创建 `CNAME` 文件，内容为你的域名

## 本地预览

```bash
# 在 conference-website/ 目录下
python3 -m http.server 8080

# 浏览器访问 http://localhost:8080
```

## 常见问题

**Q: Tally.so 免费版有什么限制？**
A: 免费版支持无限表单、无限提交、文件上传、条件逻辑，无水印。Pro 版（$29/月）增加支付收款、自定义品牌、去除 Tally logo 等。

**Q: OpenReview 如何设置审稿人？**
A: 在 OpenReview 的会议组设置中，可以批量导入审稿人邮箱，设置每人审稿数量，系统会自动分配并发送邮件通知。

**Q: 网站如何更新内容？**
A: 修改 `index.html` 后，重新 `git push` 到 GitHub，1-2 分钟后自动更新。

**Q: 如何统计访问量？**
A: 可以在 `index.html` 的 `<head>` 中加入 Google Analytics 或百度统计代码。
