# OpenReview 投稿审稿系统搭建教程

> 本教程基于 OpenReview 官方文档整理，适用于首次使用 OpenReview 的会议组织者。
> 官方文档：https://docs.openreview.net

---

## 概述

OpenReview 是一个开源的在线投稿与审稿管理平台，被 ICLR、NeurIPS、MICCAI 等顶级学术会议广泛使用。主要功能包括：

- 在线投稿（支持 PDF 上传、元数据填写）
- 审稿人分配（自动匹配 + 手动调整）
- 在线审稿与讨论
- 录用决策与通知
- 全程邮件自动推送

**完全免费**，适合中小型学术会议使用。

---

## 第一步：注册 OpenReview 账号

1. 打开 https://openreview.net/signup
2. 使用**机构邮箱**注册（如学校 .edu.cn 邮箱），审核最快
   - 公共邮箱（Gmail、QQ 邮箱等）也可以注册，但审核可能需要数天甚至两周
3. 填写个人信息：姓名、机构、研究方向等
4. 检查邮箱，点击验证链接激活账号
5. 登录后完善 Profile（添加机构信息、发表论文等），**完整的 Profile 是后续操作的前提**

> **重要提示**：所有参与投稿的作者和审稿人都需要注册 OpenReview 账号并完善 Profile。建议提前通知参会人员。

---

## 第二步：提交 Venue Request Form（会议创建申请）

这是创建会议的第一步，相当于向 OpenReview 平台申请开通一个会议投稿入口。

### 2.1 进入申请页面

1. 登录 OpenReview：https://openreview.net
2. 在首页底部找到 **"Host a Venue"**（或在搜索栏搜索 "Host a Venue"）
3. 或直接访问：https://openreview.net/group?id=OpenReview.net/Support
4. 页面会显示两个表单选项：
   - **Request Form**（标准申请表单）— 功能最全，推荐使用 ✅
   - **Conference Review Workflow**（会议审稿工作流）— 适合简单流程，仍在开发中
5. 点击 **"OpenReview Support Request Form"**

> **测试用途**：如果只是想先试用熟悉流程，可以使用测试环境：https://dev.openreview.net/group?id=OpenReview.net/Support

### 2.2 填写表单字段

以下是表单中需要填写的主要内容，以本会议为例给出推荐值：

#### 基本信息

| 字段 | 说明 | 推荐填写值 |
|------|------|-----------|
| **Title**（标题） | 会议简称 | 第七届全国偏振与椭偏测量大会 |
| **Official Venue Name**（正式会议名称） | 完整英文名称 | The 7th National Conference on Polarization and Ellipsometry Measurement |
| **Abbreviated Venue Name**（缩写） | 会议缩写 | NCEM2026 或 Polarization2026 |
| **Official Website URL**（官方网站） | 你的网站链接 | https://你的用户名.github.io/conference-website |
| **Program Chair Emails**（程序主席邮箱） | 主席的 OpenReview 注册邮箱，多个用逗号分隔 | 你的邮箱（可填多个主席邮箱） |
| **Contact Email**（联系邮箱） | 会议咨询邮箱 | 你的联系邮箱 |

#### 角色设置

| 字段 | 说明 | 推荐选择 |
|------|------|---------|
| **Area Chairs (Metareviewers)** | 是否需要领域主席（元审稿人） | 小型会议选 "No"；中大型会议选 "Yes, our venue has Area Chairs" |
| **Senior Area Chairs** | 是否需要高级领域主席 | 一般选 "No"（小型会议不需要） |
| **Reviewers Name** | 审稿人角色名称 | Reviewers（默认即可，不能含空格，用下划线） |

#### 时间设置

| 字段 | 说明 | 推荐填写值 |
|------|------|-----------|
| **Venue Start Date** | 会议开始日期 | 2026/08/26 |
| **Submission Start Date**（投稿开始日期） | 投稿系统开放时间，留空则部署后立即开放 | 2026/07/01 00:00 |
| **Submission Deadline**（投稿截止日期）⚠️必填 | 主要截稿时间 | 2026/08/15 23:59 |
| **Full Submission Deadline**（全文截止日期） | 如果有摘要+全文两个截稿日期，此处填全文截稿 | 留空（本会议只收摘要） |

#### 匿名性与可见性

| 字段 | 说明 | 推荐选择 |
|------|------|---------|
| **Author and Reviewer Anonymity** | 作者和审稿人匿名性 | **No anonymity**（非匿名，适合国内会议摘要投稿）。如果需要双盲审稿选 "Double-blind" |
| **Reviewer Identity Visibility** | 审稿人身份可见性（仅双盲时需设） | "Assigned reviewers only"（仅分配的审稿人可见） |
| **submission_readers** | 投稿可见范围 | "All program committee"（所有委员会可见）或 "Everyone"（公开，适合会议摘要展示） |

#### 其他设置

| 字段 | 说明 | 推荐填写值 |
|------|------|-----------|
| **Paper Matching** | 论文-审稿人匹配方式 | 勾选 "OpenReview Affinity"（基于发表记录的自动匹配） |
| **Expected Submissions**（预期投稿数）⚠️必填 | 预估投稿量，用于容量规划 | 50（根据实际情况填写） |
| **Other Important Information** | 其他重要信息 | "Single deadline; abstract only; no rebuttal; Chinese conference." |
| **Previous Venue** | 上届会议的 OpenReview 链接 | 留空（如果是首次举办） |

### 2.3 提交表单

1. 仔细检查所有字段
2. 勾选底部的 **Venue Organizer Agreement**（会议组织者协议）
3. 点击 **Submit** 提交

### 2.4 等待审核与部署

- 提交后，OpenReview 团队会审核你的申请（通常 1-3 个工作日）
- 审核过程中可能会邮件联系你确认或修改某些设置
- 审核通过后，你会收到一封标题为 **"Your Venue is Deployed"** 的邮件

---

## 第三步：部署完成后的操作

部署完成后，OpenReview 会自动创建以下内容：

### 3.1 会议主页

- 获得一个 **Venue ID**，格式类似：`NCEM.org/2026/Conference`
- 会议主页地址：`https://openreview.net/group?id=NCEM.org/2026/Conference`
- 主页包含会议信息和 **"Submit"** 投稿按钮

### 3.2 委员会角色组

| 角色组 | 组 ID 格式 | 功能 |
|--------|-----------|------|
| Program Chairs（程序主席） | `NCEM.org/2026/Conference/Program_Chairs` | 管理全流程，分配审稿人，做录用决策 |
| Area Chairs（领域主席） | `NCEM.org/2026/Conference/Area_Chairs` | 元审稿，管理审稿人（如有） |
| Reviewers（审稿人） | `NCEM.org/2026/Conference/Reviewers` | 审阅论文，提交审稿意见 |
| Authors（作者） | `NCEM.org/2026/Conference/Authors` | 自动加入，查看自己的投稿状态 |

### 3.3 Program Chair 控制台

登录后，在首页 **"Active Consoles"** 下可以看到你的 PC Console，包含：
- **Workflow Timeline** — 工作流时间线，可编辑各阶段设置
- **Venue Request Form** — 修改会议设置
- **Committee Consoles** — 管理各委员会成员
- **Edge Browser** — 查看和管理论文-审稿人分配关系

---

## 第四步：招募审稿人

1. **准备审稿人邮箱列表** — 从学术委员、组织委员会、专题主席中确定审稿人
2. 在 PC Console 中找到 **Reviewers** 组
3. 点击 **"Add Members"**，输入审稿人的 OpenReview 注册邮箱
4. 系统会自动发送邀请邮件给审稿人
5. 审稿人需要：
   - 注册 OpenReview 账号（如尚未注册）
   - 完善 Profile（至少填写机构信息）
   - 确认接受审稿邀请

> **提示**：审稿人必须在 OpenReview 上有完整 Profile 才能被分配论文。建议提前 2-3 周开始招募。

---

## 第五步：投稿阶段

### 5.1 作者投稿流程

1. 作者访问会议主页：`https://openreview.net/group?id=你的VenueID`
2. 点击 **"Submit"** 按钮
3. 填写投稿信息：
   - 标题
   - 摘要
   - 作者列表（每位作者需有 OpenReview Profile）
   - 关键词/主题分类（对应你的6个专题）
   - 上传 PDF 文件（摘要模板）
4. 点击提交

### 5.2 管理投稿

- 在 PC Console 可以查看所有投稿
- 可以修改截稿日期（如有需要延期）
- 可以查看投稿统计（数量、主题分布等）

---

## 第六步：审稿阶段

### 6.1 分配审稿人

1. 在 PC Console 中运行 **Paper Matching Setup**（论文匹配设置）
2. 系统会基于发表记录计算每篇论文与每位审稿人的匹配度
3. 分配方式：
   - **自动分配**：系统根据匹配度自动分配
   - **手动分配**：在 Edge Browser 中逐篇分配
   - **混合模式**：先自动分配，再手动微调

### 6.2 审稿人操作

审稿人登录后在自己的 Console 中可以：
- 查看分配给自己的论文
- 下载论文 PDF
- 在线填写审稿意见（评分 + 文字评价）
- 提交审稿意见

### 6.3 审稿监控

- PC Console 可以实时查看审稿进度
- 可以给未完成审稿的审稿人发送提醒邮件
- 可以添加紧急审稿人（如果有人退出）

---

## 第七步：录用决策

1. 所有审稿完成后，在 PC Console 中查看审稿意见汇总
2. 程序主席根据审稿意见做出录用决策：
   - **Accept (Oral)** — 录用为口头报告
   - **Accept (Poster)** — 录用为张贴报告
   - **Reject** — 拒稿
3. 在系统中设置决策结果
4. 系统自动发送录用/拒稿通知邮件给作者

---

## 第八步：将 OpenReview 链接嵌入网站

部署完成后，你会获得会议的 OpenReview 主页链接。将其告诉我，我帮你替换到 cfp.html 中的投稿按钮。

替换位置在 `cfp.html` 第 108 行：

```html
<!-- 替换前 -->
<a href="https://openreview.net/group?id=[你的会议ID]" target="_blank" class="btn btn-accent btn-large">
    前往 OpenReview 投稿
</a>

<!-- 替换后（示例） -->
<a href="https://openreview.net/group?id=NCEM.org/2026/Conference" target="_blank" class="btn btn-accent btn-large">
    前往 OpenReview 投稿
</a>
```

---

## 常见问题

### Q1: OpenReview 收费吗？
**完全免费。** OpenReview 是由微软资助的开源项目，对会议组织者和作者都不收费。

### Q2: 审核需要多长时间？
提交 Venue Request Form 后，通常 **1-3 个工作日**内完成审核部署。

### Q3: 作者必须注册 OpenReview 吗？
是的。所有投稿作者都需要注册 OpenReview 账号并完善 Profile。建议在投稿指南中提前告知作者。

### Q4: 可以修改截稿日期吗？
可以。在 PC Console 的 Venue Request Form 中找到 Submission Deadline 字段，修改后保存即可。

### Q5: 支持中文吗？
OpenReview 界面是英文的，但投稿内容可以包含中文（标题、摘要等）。审稿意见也支持中文输入。

### Q6: 如何测试整个流程？
在提交正式申请前，可以在测试环境 https://dev.openreview.net 先创建一个测试会议，熟悉所有操作。测试环境的邮件功能有限（仅支持注册和密码重置）。

### Q7: 投稿人需要 OpenReview Profile 吗？
默认设置允许作者用姓名+邮箱投稿，但建议在表单中开启 "force profile" 选项，要求所有作者都有 Profile，这样审稿匹配更准确。

---

## 本会议推荐配置汇总

| 设置项 | 推荐值 |
|--------|--------|
| Abbreviated Venue Name | NCEM2026 |
| Program Chair Emails | 你的邮箱 |
| Area Chairs | No（小型会议不需要） |
| Author and Reviewer Anonymity | No anonymity（非匿名投稿） |
| Submission readers | Everyone（公开展示摘要） |
| Submission Start Date | 2026/07/01 |
| Submission Deadline | 2026/08/15 23:59 |
| Expected Submissions | 50 |
| Paper Matching | OpenReview Affinity |

---

## 官方资源

- **官方文档**：https://docs.openreview.net
- **Venue 创建指南**：https://docs.openreview.net/getting-started/hosting-a-venue-on-openreview/creating-your-venue-instance-submitting-a-venue-request-form
- **常见问题**：https://openreview.net/faq
- **工作流示例**：https://docs.openreview.net/venue-request-workflow/conferences
- **表单自定义**：https://docs.openreview.net/getting-started/hosting-a-venue-on-openreview/customizing-your-submission-form
- **联系支持**：info@openreview.net
