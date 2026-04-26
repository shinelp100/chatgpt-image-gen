# ChatGPT Image Generation

使用 ChatGPT GPT-4o 的图片生成功能，提供提示词模板和约束条件。

## 功能特点

- 预设提示词模板（信息图风格）
- 支持自定义约束条件
- 适合微信公众号信息图生成

## 重要限制

**Cloudflare Turnstile 拦截**：ChatGPT 使用 Cloudflare 安全验证，自动化浏览器会被检测为机器人。**推荐使用手动模式**。

## 使用方式（手动模式）

### 1. 准备提示词

```bash
# 查看提示词文件
cat ~/.hermes/skills/creative/chatgpt-image-gen/prompt-光模块规格演进.txt

# 快速复制到剪贴板
cat ~/.hermes/skills/creative/chatgpt-image-gen/prompt-光模块规格演进.txt | pbcopy
```

### 2. 手动访问 ChatGPT

1. 在浏览器中打开 https://chatgpt.com
2. 登录 ChatGPT Plus/Pro 账号
3. 选择 **GPT-4o** 模型

### 3. 发送提示词

复制提示词内容，粘贴到输入框，发送等待图片生成。

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

## 前置条件

1. ChatGPT Plus 或 Pro 订阅（图片生成需要 GPT-4o 模型）

## 相关技能

- `flowchart-to-instagram` - 本地信息图生成（无需 ChatGPT）
- `beautiful-mermaid` - Mermaid 图表美化

## 许可证

MIT License

## 作者

shinelp100