# GitHub Pages 网站发布详细教程

> 本教程专为首次使用的用户编写，每一步都有详细说明。
> 预计完成时间：15-20 分钟

---

## 前置条件（已完成 ✅）

- Git 已安装，已配置用户名 Goonway 和邮箱 nmgswf@163.com
- 本地仓库已初始化，已创建首次提交（main 分支）
- SSH 密钥已存在（~/.ssh/id_rsa.pub）
- 所有网页资源使用相对路径，适合 GitHub Pages

---

## 第一步：注册 GitHub 账号（如已有账号请跳过）

1. 打开浏览器，访问 **https://github.com/signup**
2. 输入你的邮箱（nmgswf@163.com）
3. 设置密码（至少 15 个字符，或至少 8 个字符包含数字和字母）
4. 输入用户名（英文，如 `goonway` —— 这个名字会出现在你的网站地址中）
5. 完成验证码验证
6. 点击 **Create account**
7. GitHub 会发一封验证邮件到你的邮箱，打开邮件点击验证链接

> **重要**：请记住你的 GitHub 用户名，后面会用到。以下教程中用 `你的用户名` 代替。

---

## 第二步：在 GitHub 上创建新仓库

1. 登录 GitHub 后，点击右上角 **"+"** 号 → 选择 **"New repository"**
   - 或直接访问：https://github.com/new
2. 填写仓库信息：
   - **Repository name**：输入 `polarization-meeting`（仓库名将出现在网址中）
   - **Description**（可选）：`第七届全国偏振与椭偏测量大会宣传网站`
   - **可见性**：选择 **Public**（必须公开，GitHub Pages 免费版仅支持公开仓库）
   - **不要勾选** "Add a README file"
   - **不要勾选** "Add .gitignore"
   - **不要勾选** "Choose a license"
3. 点击绿色的 **"Create repository"** 按钮

> 创建后会跳转到一个页面，显示推送代码的命令 —— **不用管它**，继续下面的步骤。

---

## 第三步：添加 SSH 密钥到 GitHub（一次性操作）

这一步让 GitHub 认识你的电脑，之后就能免密码推送代码。

### 3.1 查看并复制你的 SSH 公钥

在电脑上打开「终端」应用，输入以下命令：

```bash
cat ~/.ssh/id_rsa.pub
```

会输出一行以 `ssh-rsa` 开头的长文本，类似：

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxxxxxxxxxxxxxxx... wanfushen@macbook
```

**完整复制**这一行（从 `ssh-rsa` 一直到末尾）。

### 3.2 添加到 GitHub

1. 在 GitHub 页面，点击右上角头像 → **Settings**
2. 左侧菜单找到 **SSH and GPG keys**（直接访问：https://github.com/settings/keys）
3. 点击 **"New SSH key"** 按钮
4. 填写：
   - **Title**：`我的 MacBook`（随便起名，方便识别）
   - **Key type**：保持 `Authentication Key`
   - **Key**：粘贴刚才复制的公钥内容
5. 点击 **"Add SSH key"**

### 3.3 验证 SSH 连接

在终端输入：

```bash
ssh -T git@github.com
```

第一次连接会提示 `Are you sure you want to continue connecting`，输入 `yes` 然后回车。

如果看到类似以下信息，说明连接成功：

```
Hi 你的用户名! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 第四步：将本地代码推送到 GitHub

在终端中，依次执行以下命令（注意替换 `你的用户名`）：

### 4.1 关联远程仓库

```bash
cd /Users/wanfushen/WorkBuddy/2026-07-05-00-29-22/conference-website
git remote add origin git@github.com:你的用户名/polarization-meeting.git
```

> 如果提示 `remote origin already exists`，先执行 `git remote remove origin`，再重新执行上面的命令。

### 4.2 推送代码

```bash
git push -u origin main
```

推送过程中会显示进度条，完成后会显示类似：

```
To github.com:你的用户名/polarization-meeting.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

> 现在打开你的 GitHub 仓库页面（https://github.com/你的用户名/polarization-meeting），应该能看到所有网站文件。

---

## 第五步：启用 GitHub Pages（关键步骤）

1. 打开你的仓库页面：`https://github.com/你的用户名/polarization-meeting`
2. 点击仓库顶部的 **"Settings"** 标签（不是头像里的 Settings，是仓库里的）
3. 在左侧菜单中，找到 **"Pages"** 选项
   - 左侧菜单很长，Pages 通常在中间偏下位置，Code and automation 分组下面
4. 在 **"Build and deployment"** 区域设置：
   - **Source**：选择 `Deploy from a branch`
   - **Branch**：选择 `main`，旁边选择 `/(root)`
5. 点击 **"Save"** 按钮

> 保存后，页面顶部会出现一个提示："Your site is live at https://你的用户名.github.io/polarization-meeting/"
>
> 首次部署通常需要 1-2 分钟，请耐心等待。如果没出现链接，等一会儿刷新页面。

---

## 第六步：验证网站

1. 等待 1-2 分钟后，在浏览器中访问：

   ```
   https://你的用户名.github.io/polarization-meeting/
   ```

2. 你应该能看到会议网站首页！

3. 检查以下内容是否正常：
   - ✅ 首页横幅图片和文字
   - ✅ 导航栏点击各页面是否正常跳转
   - ✅ 图片是否正常显示（特别是赞助商 Logo）
   - ✅ Tally 注册表单弹窗是否正常
   - ✅ Tally 摘要上传弹窗是否正常
   - ✅ 下载中心的文件是否能正常下载

---

## 日常更新：以后修改网站怎么办？

以后每次修改网站文件后，只需在终端执行以下三步：

```bash
# 1. 进入项目目录
cd /Users/wanfushen/WorkBuddy/2026-07-05-00-29-22/conference-website

# 2. 添加所有修改
git add -A

# 3. 提交修改（引号内写本次改了什么）
git commit -m "更新了XX页面的XX内容"

# 4. 推送到 GitHub
git push
```

推送后，GitHub Pages 会在 1-2 分钟内自动更新网站。

---

## 常见问题

### Q1: 推送代码时提示 "Permission denied (publickey)"

说明 SSH 密钥未正确配置。请重新执行第三步，确保公钥完整复制到 GitHub。

### Q2: 网站打开是空白页或 404

1. 检查 GitHub Pages 设置是否选择了 `main` 分支和 `/(root)` 目录
2. 等待 2-3 分钟后刷新
3. 确认仓库中有 `index.html` 文件且在根目录

### Q3: 图片显示不出来

- 中文文件名在某些情况下可能有问题
- 检查浏览器控制台（F12）看具体报错

### Q4: 推送时提示文件太大

GitHub 限制单个文件 100MB。当前项目最大文件 1.7MB，远在限制内。

### Q5: 想要自定义域名（如 www.polarization-meeting.com）

等网站上线后，可以在 GitHub Pages 设置中配置自定义域名。需要额外购买域名并修改 DNS 记录。

---

## 总结流程图

```
本地修改文件
    ↓
git add -A          ← 将修改添加到暂存区
    ↓
git commit -m "说明"  ← 提交到本地仓库
    ↓
git push             ← 推送到 GitHub
    ↓
GitHub Pages 自动部署  ← 1-2 分钟后网站自动更新
    ↓
访问 https://用户名.github.io/polarization-meeting/  ← 查看结果
```
