# ChatGPT Image Generation

使用 ChatGPT GPT-4o 的图片生成功能，通过 Chrome DevTools MCP 自动化生成高质量信息图。

## 功能特点

- 自动化浏览器操作（Chrome DevTools MCP）
- 预设提示词模板（信息图风格）
- 支持自定义约束条件
- 适合微信公众号信息图生成

## 使用方式

### 1. 触发命令

```
用 ChatGPT 生成图片
```

### 2. 提供内容描述

```
内容：股票研报工作流

要求：
1、解析 Mermaid flowchart 语法，生成渐变背景 + 毛玻璃卡片的信息图
2、支持 TD（垂直）和 LR（横向）布局
3、自动水印（题材调研员）、emoji 匹配、品牌定制
4、主题：hand-drawn-edu
```

### 3. 自动执行流程

1. 打开 Chrome 浏览器，导航到 chatgpt.com
2. 选择 GPT-4o 生图模式
3. 填充提示词模板
4. 发送请求，等待图片生成
5. 下载生成的图片

## 提示词模板

### 信息图模板（公众号风格）

```
内容：[描述内容]

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

1. Chrome 浏览器已安装
2. Chrome DevTools MCP 已配置
3. ChatGPT Plus 或 Pro 订阅（图片生成功能）

## 安装

作为 Hermes skill 使用：

```bash
# 已内置在 Hermes skills 中
# 位置：~/.hermes/skills/creative/chatgpt-image-gen/
```

## 相关技能

- `mcp/chrome-screenshot` - 截取网页内容
- `flowchart-to-instagram` - 本地信息图生成
- `beautiful-mermaid` - Mermaid 图表美化

## 许可证

MIT License

## 作者

shinelp100