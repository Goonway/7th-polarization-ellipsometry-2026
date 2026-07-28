# Gitee Pages 网站发布详细教程

> 本教程专为首次使用的用户编写，每一步都有详细说明。
> 预计完成时间：20-30 分钟（含实名认证等待时间）

---

## 前置条件（已完成 ✅）

- Git 已安装，已配置用户名 Goonway 和邮箱 nmgswf@163.com
- 本地仓库已初始化，已创建首次提交（main 分支，50个文件）
- SSH 密钥已存在（~/.ssh/id_rsa.pub）
- 所有网页资源使用相对路径，适合 Gitee Pages

---

## 第一步：注册 Gitee 账号（如已有账号请跳过）

1. 打开浏览器，访问 **https://gitee.com/signup**
2. 输入以下信息：
   - **手机号**：你的手机号码
   - **验证码**：点击获取，输入收到的短信验证码
   - **密码**：设置密码（至少 6 位，含字母和数字）
3. 点击 **注册并登录**
4. 设置个人空间地址（Gitee 会让你选一个英文用户名，如 `goonway`）
   - 这个名字会出现在你的网站地址中，请记住
   - 以下教程中用 `你的用户名` 代替

> **注意**：Gitee 的用户名就是你的个人空间地址，例如 `https://gitee.com/你的用户名`

---

## 第二步：完成实名认证（必须！Gitee Pages 强制要求）

Gitee Pages 服务要求账号通过实名认证，否则无法使用。

### 2.1 进入认证页面

1. 登录 Gitee 后，点击右上角头像 → **设置**
   - 或直接访问：https://gitee.com/profile/realnameauth
2. 左侧菜单找到 **实名认证**

### 2.2 填写实名信息

1. **真实姓名**：输入身份证上的姓名
2. **身份证号**：输入18位身份证号码
3. 点击 **提交认证**

### 2.3 等待审核

- 实名认证通常 **即时通过**（自动校验）
- 少数情况下可能需要人工审核，等待 1-2 个小时
- 认证通过后，页面会显示"已认证"状态

> **重要**：必须等实名认证通过后，才能进行第六步（启用 Gitee Pages）。前几步创建仓库、推送代码可以先做。

---

## 第三步：添加 SSH 密钥到 Gitee

这一步让 Gitee 认识你的电脑，之后就能免密码推送代码。

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

### 3.2 添加到 Gitee

1. 在 Gitee 页面，点击右上角头像 → **设置**
2. 左侧菜单找到 **SSH公钥**
   - 或直接访问：https://gitee.com/profile/sshkeys
3. 在添加公钥区域填写：
   - **标题**：`我的 MacBook`（随便起名，方便识别）
   - **公钥**：粘贴刚才复制的内容
4. 点击 **确定**
5. Gitee 会要求输入密码确认，输入你的 Gitee 密码

### 3.3 验证 SSH 连接

在终端输入：

```bash
ssh -T git@gitee.com
```

第一次连接会提示 `Are you sure you want to continue connecting`，输入 `yes` 然后回车。

如果看到以下信息，说明连接成功：

```
Hi 你的用户名! You've successfully authenticated, but GITEE.COM does not provide shell access.
```

---

## 第四步：在 Gitee 上创建新仓库

1. 登录 Gitee 后，点击页面右上角 **"+"** 号 → 选择 **「新建仓库」**
   - 或直接访问：https://gitee.com/projects/new
2. 填写仓库信息：
   - **仓库名称**：输入 `polarization-meeting`
   - **路径**：自动生成，保持默认即可
   - **仓库介绍**（可选）：`第七届全国偏振与椭偏测量大会宣传网站`
   - **开源/私有**：选择 **「开源」**（必须公开，Gitee Pages 免费版仅支持公开仓库）
   - **不要勾选** "使用 Readme 文件初始化这个仓库"
   - **不要勾选** "设置模型"
   - **不要选择** .gitignore 模板
   - **不要选择** 开源许可证
3. 点击 **「创建」** 按钮

> 创建后会跳转到一个页面，显示推送代码的命令 —— **不用管它**，继续下面的步骤。

---

## 第五步：将本地代码推送到 Gitee

在终端中，依次执行以下命令（注意替换 `你的用户名`）：

### 5.1 关联远程仓库

```bash
cd /Users/wanfushen/WorkBuddy/2026-07-05-00-29-22/conference-website
git remote add origin git@gitee.com:你的用户名/polarization-meeting.git
```

> 如果提示 `remote origin already exists`（之前关联过 GitHub），先执行：
> ```bash
> git remote remove origin
> ```
> 再重新执行上面的命令。

### 5.2 推送代码

```bash
git push -u origin main
```

推送过程中会显示进度条，完成后会显示类似：

```
Enumerating objects: 56, done.
...
To gitee.com:你的用户名/polarization-meeting.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

> 现在打开你的 Gitee 仓库页面（https://gitee.com/你的用户名/polarization-meeting），应该能看到所有网站文件。

---

## 第六步：启用 Gitee Pages（关键步骤）

> **前提**：确保第二步的实名认证已通过！

### 6.1 进入 Gitee Pages 服务

1. 打开你的仓库页面：`https://gitee.com/你的用户名/polarization-meeting`
2. 点击仓库顶部菜单栏的 **「服务」** 标签
3. 在下拉菜单中找到并点击 **「Gitee Pages」**

### 6.2 部署网站

1. 在 Gitee Pages 页面中：
   - **部署分支**：选择 `main`
   - **部署目录**：保持 `/`（根目录）不变
2. 勾选「强制使用 HTTPS」（推荐）
3. 点击 **「启动」** 按钮

### 6.3 等待部署完成

- 部署通常需要 30 秒 - 1 分钟
- 部署成功后，页面会显示你的网站地址：

```
https://你的用户名.gitee.io/polarization-meeting
```

---

## 第七步：验证网站

1. 在浏览器中访问：

   ```
   https://你的用户名.gitee.io/polarization-meeting/
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

### 步骤 1：推送修改到 Gitee

每次修改网站文件后，在终端执行：

```bash
cd /Users/wanfushen/WorkBuddy/2026-07-05-00-29-22/conference-website

git add -A

git commit -m "更新了XX页面的XX内容"

git push
```

### 步骤 2：手动更新 Gitee Pages（重要！）

> Gitee Pages 免费版**不会自动更新**，需要你手动点击。

1. 打开浏览器，访问你的 Gitee 仓库页面
2. 点击 **「服务」** → **「Gitee Pages」**
3. 点击 **「更新」** 按钮
4. 等待 30 秒 - 1 分钟，网站即更新完成

> 如果觉得每次手动更新太麻烦，可以考虑开通 Gitee Pages Pro（99元/年），支持推送后自动部署。

---

## 常见问题

### Q1: 推送代码时提示 "Permission denied (publickey)"

说明 SSH 密钥未正确配置。请重新执行第三步，确保公钥完整复制到 Gitee。
也可以临时用 HTTPS 方式推送：
```bash
git remote set-url origin https://gitee.com/你的用户名/polarization-meeting.git
git push -u origin main
```
推送时输入 Gitee 用户名和密码。

### Q2: Gitee Pages 服务里提示"请先完成实名认证"

说明实名认证未通过或未做。请先完成第二步的实名认证，等待通过后再来启用。

### Q3: 网站打开是空白页或 404

1. 检查 Gitee Pages 部署分支是否选择了 `main`，目录是否为 `/`
2. 确认仓库中有 `index.html` 文件且在根目录
3. 尝试点击 Gitee Pages 页面的「更新」按钮重新部署

### Q4: 推送时提示文件太大

Gitee 限制单个文件 100MB，仓库总大小 500MB。当前项目约 9MB，远在限制内。

### Q5: 图片显示不出来

- 检查浏览器控制台（F12）看具体报错
- 确认图片文件名在 HTML 中的引用与实际文件名完全一致（含大小写）

### Q6: 实名认证一直不通过

- 检查姓名和身份证号是否填写正确
- 确保身份证未过期
- 如持续不通过，联系 Gitee 客服

### Q7: 想要自定义域名（如 www.polarization-meeting.com）

Gitee Pages 免费版不支持自定义域名，需要开通 Gitee Pages Pro（99元/年）。
如果只是用免费版，网站地址就是 `https://你的用户名.gitee.io/polarization-meeting`。

---

## 总结流程图

```
首次部署（只做一次）：
注册Gitee → 实名认证 → 添加SSH密钥 → 创建仓库 → 推送代码 → 启用Gitee Pages → 验证网站

日常更新（每次修改后）：
git add -A → git commit -m "说明" → git push → 登录Gitee点「更新」→ 网站刷新
```
