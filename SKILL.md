---
name: chatgpt-image-gen
description: 使用 ChatGPT GPT-4o 生成高质量图片（手动模式），提供提示词模板和约束条件模板
version: 1.1.0
repository: https://github.com/shinelp100/chatgpt-image-gen
depends_on:
  - chrome-devtools-mcp
---

# ChatGPT 图片生成

使用 ChatGPT GPT-4o 图片生成功能，提供预设提示词模板和约束条件。

## 重要限制

**Cloudflare Turnstile 拦截**：ChatGPT 使用 Cloudflare 安全验证，Chrome DevTools MCP 控制的浏览器会被检测为机器人，自动化方案**无法工作**。

**ChatGPT 官网 vs OpenAI API 计费差异**：

| 对比项 | ChatGPT 官网 (chatgpt.com) | OpenAI API (platform.openai.com) |
|--------|---------------------------|----------------------------------|
| 计费模式 | 订阅制 (Free/Plus/Pro) | 按量付费（必须绑卡） |
| 免费额度 | Free 用户每天几张图片 | **没有免费额度** |
| 付款方式 | Free 用户不需要绑卡 | 必须绑定信用卡 |
| 适用场景 | 个人使用 | 开发者集成 |

**结论**：即使 ChatGPT 官网可以免费生成图片，API 平台也需要绑定付款方式才能使用。

**推荐模式**：手动操作 + 提示词模板文件

## 触发场景

- "用 ChatGPT 生成图片"
- "GPT-4o 生图"
- "ChatGPT 图片生成"

## 前置条件

1. ChatGPT Plus 或 Pro 订阅（图片生成需要 GPT-4o 模型）
2. Chrome DevTools MCP 已配置（手动模式可选）

## 工作流程（手动模式）

### 1. 准备提示词

```bash
# 查看提示词文件
cat ~/.hermes/skills/creative/chatgpt-image-gen/prompt-光模块规格演进.txt
```

或使用模板生成新提示词：

```bash
# 提示词模板位置
cat ~/.hermes/skills/creative/chatgpt-image-gen/templates/prompts.md
```

### 2. 手动访问 ChatGPT

1. 在真实浏览器中打开 https://chatgpt.com
2. 登录 ChatGPT Plus/Pro 账号
3. 选择 **GPT-4o** 模型（支持图片生成）

### 3. 发送提示词

复制提示词内容，粘贴到输入框，发送等待图片生成（约 1-2 分钟）。

### 4. 下载图片

右键图片 → 保存到本地

## 提示词模板

### 信息图模板（公众号风格）

```
内容：[Mermaid flowchart 代码或描述内容]

要求：
1、解析 Mermaid flowchart 语法，生成渐变背景 + 毛玻璃卡片的信息图
2、支持 TD（垂直）和 LR（横向）布局
3、自动水印（题材调研员）、emoji 匹配、品牌定制
4、主题：hand-drawn-edu | 手绘风教育插画 | 米白纸张背景 + 手绘边框 | #E8655A
```

### 简洁商务模板

```
内容：[描述内容]

风格：极简、专业、商务
配色：蓝色系 + 白色背景
尺寸：适合微信公众号（竖屏 800px 宽）
```

## 示例用法

**输入**：
```
用 ChatGPT 生成图片，内容是：[Mermaid flowchart 代码]
```

**执行步骤**：
1. 读取提示词模板
2. 保存提示词到文件（方便复制）
3. 用户手动访问 ChatGPT
4. 复制粘贴提示词，生成图片

## 注意事项

- 图片生成需要 ChatGPT Plus 或 Pro 订阅
- 每次生成约 1-2 分钟
- 提示词中明确风格、配色、尺寸要求
- Cloudflare 拦截导致自动化无法工作

## 故障排查

| 问题 | 解决方案 |
|------|---------|
| Cloudflare "正在验证..." 卡住 | **无法绕过**，改用手动模式 |
| 模型选择器找不到 GPT-4o | 检查账号是否有 Plus 订阅 |
| 图片生成失败 | 简化提示词，避免敏感内容 |
| 提示词太长 | 分段发送或简化 Mermaid 代码 |

## 相关技能

- `mcp/chrome-screenshot` - 截取网页内容
- `flowchart-to-instagram` - 本地信息图生成（无需 Cloudflare）
- `beautiful-mermaid` - Mermaid 图表美化