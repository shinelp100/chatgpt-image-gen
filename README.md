# ChatGPT Image Generation (API 版)

使用 OpenAI GPT-4o Image API 生成高质量图片，无需浏览器自动化。

## 功能特点

- **API 直接调用**：无需浏览器，无 Cloudflare 拦截问题
- **开发者友好**：适用于本地化广告、信息图、教育内容、设计工具等业务场景
- **预设模板**：信息图、教育内容、商务风格等多种模板
- **微信适配**：竖屏 800px 宽度，适合公众号发布

## 快速开始

### 1. 安装依赖

```bash
pip install openai
```

### 2. 配置 API Key

```bash
export OPENAI_API_KEY="sk-xxx"
```

或从 https://platform.openai.com/api-keys 获取

### 3. 生成图片

```bash
# 使用提示词文件
python ~/.hermes/skills/creative/chatgpt-image-gen/scripts/generate_image.py \
  --file prompt.txt \
  --output image.png

# 直接提供提示词
python ~/.hermes/skills/creative/chatgpt-image-gen/scripts/generate_image.py \
  --prompt "生成一张信息图..." \
  --output image.png
```

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

## API 适用场景

根据 OpenAI 官方说明，GPT-image-2 API 支持：

- 本地化广告制作
- 信息图生成
- 教育内容创作
- 设计工具集成
- 营销素材自动化

## 相关技能

- `mcp/chrome-screenshot` - 截取网页内容
- `flowchart-to-instagram` - 本地信息图生成
- `beautiful-mermaid` - Mermaid 图表美化

## 许可证

MIT License

## 作者

shinelp100