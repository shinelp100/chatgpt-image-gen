---
name: chatgpt-image-gen
description: 使用 ChatGPT GPT-4o image generation 功能生成图片，通过 Chrome DevTools MCP 自动化浏览器操作
version: 1.0.0
depends_on:
  - chrome-devtools-mcp
---

# ChatGPT 图片生成

使用 Chrome DevTools MCP 控制 ChatGPT 生成高质量图片。

## 触发场景

- "用 ChatGPT 生成图片"
- "GPT-4o 生图"
- "ChatGPT 图片生成"

## 前置条件

1. Chrome 浏览器已安装
2. Chrome DevTools MCP 已配置（见 `mcp/native-mcp` skill）
3. 已登录 ChatGPT 账号（Plus 或 Pro 可用图片生成功能）

## 工作流程

### 1. 打开 ChatGPT 并选择模式

```bash
# 导航到 ChatGPT
mcp_chrome_devtools_navigate_page url="https://chatgpt.com"
```

### 2. 选择 GPT-4o 生图模型

1. 点击左上角模型选择器
2. 选择 "GPT-4o" 或 "DALL·E" 模式

### 3. 填充提示词模板

使用以下模板格式：

```
内容：[用户填写具体描述]

要求：
1、解析 Mermaid flowchart 语法，生成渐变背景 + 毛玻璃卡片的信息图
2、支持 TD（垂直）和 LR（横向）布局
3、自动水印（题材调研员）、emoji 匹配、品牌定制
4、主题：`hand-drawn-edu` | 手绘风教育插画 | 米白纸张背景 + 手绘边框 | `#E8655A` |
```

### 4. 发送并等待生成

点击发送按钮，等待图片生成完成。

### 5. 下载图片

右键图片 → 保存图片到本地

## 示例用法

**输入**：
```
用 ChatGPT 生成一张信息图，内容是：

内容：股票研报工作流
要求：
1、解析 Mermaid flowchart 语法，生成渐变背景 + 毛玻璃卡片的信息图
2、支持 TD（垂直）布局
3、自动水印（题材调研员）
4、主题：hand-drawn-edu
```

**执行步骤**：
1. 打开 Chrome，导航到 chatgpt.com
2. 选择 GPT-4o 模型
3. 在输入框填入提示词
4. 发送请求，等待图片生成
5. 下载生成的图片

## 提示词模板库

### 信息图模板（公众号风格）

```
内容：[标题]

要求：
1、解析 Mermaid flowchart 语法，生成渐变背景 + 毛玻璃卡片的信息图
2、支持 TD（垂直）和 LR（横向）布局
3、自动水印（题材调研员）、emoji 匹配、品牌定制
4、主题：`hand-drawn-edu` | 手绘风教育插画 | 米白纸张背景 + 手绘边框 | `#E8655A` |
```

### 简洁风格模板

```
内容：[描述内容]

风格：极简、专业、商务
配色：蓝色系 + 白色背景
尺寸：适合微信公众号（竖屏 800px 宽）
```

## 注意事项

- 图片生成需要 ChatGPT Plus 或 Pro 订阅
- 每次生成消耗约 1-2 分钟
- 需要保持浏览器窗口活跃状态
- 建议在提示词中明确风格、配色、尺寸要求

## 故障排查

| 问题 | 解决方案 |
|------|---------|
| 模型选择器找不到 GPT-4o | 检查账号是否有 Plus 订阅 |
| 图片生成失败 | 简化提示词，避免敏感内容 |
| 浏览器超时 | 增加等待时间，检查网络连接 |
| MCP 连接失败 | 重启 Chrome DevTools MCP 服务 |

## 相关技能

- `mcp/chrome-screenshot` - 截取网页内容
- `flowchart-to-instagram` - 本地信息图生成
- `beautiful-mermaid` - Mermaid 图表美化