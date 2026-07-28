# Tally.so 注册表单创建与嵌入网站教程

> 本教程以"第七届全国偏振与椭偏测量大会"注册表单为例，介绍如何用 Tally.so 创建表单并嵌入到网站中。

---

## 第一步：注册 Tally 账号

1. 打开 https://tally.so ，点击右上角 **"Sign up"**
2. 可以用 Google 账号一键注册，也可以用邮箱注册（免费，无需信用卡）
3. 注册后进入工作台（Workspace），点击 **"Create new form"**

---

## 第二步：设计表单内容

Tally 的操作界面类似 Notion —— 直接在页面上打字就是问题，输入 `/` 可以选择题型。

### 会议注册表单推荐字段

| 序号 | 问题内容 | 推荐题型 | 是否必填 |
|------|---------|---------|---------|
| 1 | 姓名 | 短文本（Short text） | ✅ |
| 2 | 单位/学校 | 短文本 | ✅ |
| 3 | 职称/职务 | 短文本 | 选填 |
| 4 | 联系电话 | 短文本 | ✅ |
| 5 | 电子邮箱 | 邮箱（Email） | ✅ |
| 6 | 参会类型 | 选择题（Choice）→ 教师/企业代表、学生代表 | ✅ |
| 7 | 是否住宿 | 选择题 → 单住、合住、不住宿 | ✅ |
| 8 | 入住日期 | 日期（Date） | 选填 |
| 9 | 离店日期 | 日期（Date） | 选填 |
| 10 | 是否提交报告 | 选择题 → 是/否 | 选填 |
| 11 | 报告题目 | 长文本（Long text） | 选填 |
| 12 | 报告类型 | 选择题 → 邀请报告、口头报告、张贴报告 | 选填 |
| 13 | 报告摘要上传 | 文件上传（File upload） | 选填 |
| 14 | 是否需要发票 | 选择题 → 是/否 | 选填 |
| 15 | 发票抬头 | 短文本 | 选填 |
| 16 | 税号 | 短文本 | 选填 |
| 17 | 发票接收邮箱 | 邮箱 | 选填 |

### 操作技巧

- 输入 `/` 会弹出题型菜单，选择你需要的类型
- 每个问题右侧有个齿轮图标，可以设置"必答"（Required）
- 可以用条件逻辑（Conditional logic）：比如第14题选"否"，则15-17题自动隐藏

---

## 第三步：美化表单

1. 点击页面上方的 **"Design"** 标签
2. 建议设置：
   - 主题色改为蓝色 `#185FA5`（和网站主色一致）
   - 上传会议 Logo 或天津大学校徽作为顶部图片
   - 字体保持默认即可

---

## 第四步：发布表单

1. 点击右上角 **"Publish"** 按钮
2. 发布后会弹出一个分享链接，类似：`https://tally.so/r/3qDpEY`
3. 你可以先点这个链接预览一下表单效果

---

## 第五步：获取嵌入代码

1. 在表单页面点击 **"Share"**（分享图标）
2. 选择 **"Embed"**
3. 选择 **"Standard embed"**（标准嵌入）
4. 在嵌入选项中，建议开启：
   - ✅ **Dynamic height**（动态高度，让表单完整显示不出现滚动条）
   - ✅ **Hide form title**（隐藏标题，因为网页上已有标题）
   - ✅ **Transparent background**（透明背景，融入网页）
5. 点击 **"Copy code"**，会复制一段类似这样的代码：

```html
<iframe
    src="https://tally.so/embed/3qDpEY?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1"
    frameborder="0"
    marginheight="0"
    marginwidth="0"
    title="会议注册表单">
</iframe>
```

---

## 第六步：嵌入到网站

拿到嵌入代码后，替换到 `registration.html` 中的表单占位区域。

### 具体操作

1. 打开 `conference-website/registration.html`
2. 找到 `<!-- 方式二：占位提示 -->` 下面的 `<div class="form-placeholder">...</div>`
3. 把整个占位 div 替换为 iframe 代码，并加上 `class="form-embed"`：

```html
<iframe
    class="form-embed"
    src="https://tally.so/embed/你的表单ID?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1"
    frameborder="0"
    marginheight="0"
    marginwidth="0"
    title="会议注册表单">
</iframe>
```

> 注意：把 `你的表单ID` 替换为 Tally 生成的实际 ID（如 `3qDpEY`）

---

## 补充说明

### 免费版限制
- Tally 免费版不限表单数量和提交数量，基本够用
- 文件上传单个文件限 10MB，够放摘要

### 查看提交数据
- 注册数据在 Tally 后台的 **"Submissions"** 页面查看
- 可以导出 Excel

### 后续修改
- 表单内容在 Tally 后台修改后会**自动同步**到网站，无需重新嵌入代码（除非改了嵌入样式选项）

---

*本教程创建于 2026年7月27日，适用于第七届全国偏振与椭偏测量大会网站项目。*
