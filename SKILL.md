---
name: chatgpt-image-gen
description: 使用 OpenAI GPT-4o Image API 生成高质量图片，适用于本地化广告、信息图、教育内容、设计工具等业务场景
version: 2.0.0
repository: https://github.com/shinelp100/chatgpt-image-gen
depends_on:
  - openai
---

# ChatGPT 图片生成 (API 版)

使用 OpenAI GPT-4o 的图片生成 API，无需浏览器自动化，直接通过 API 生成高质量图片。

## 触发场景

- "用 ChatGPT API 生成图片"
- "GPT-4o 生图"
- "生成信息图"

## 前置条件

1. **OpenAI API Key**：从 https://platform.openai.com/api-keys 获取
2. **GPT-4o 访问权限**：需要 Plus 或 Pro 订阅（API 调用需要付费）
3. **Python 环境**：Python 3.8+ 和 openai 库

### 安装依赖

```bash
pip install openai
```

### 配置 API Key

```bash
# 方式1: 环境变量
export OPENAI_API_KEY="sk-xxx"

# 方式2: 运行时参数
python generate_image.py --api-key "sk-xxx" ...
```

## 工作流程

### 1. 准备提示词

创建提示词文件或直接提供文本：

```bash
# 使用提示词文件
python generate_image.py --file prompt.txt --output image.png

# 直接提供提示词
python generate_image.py --prompt "内容描述..." --output image.png
```

### 2. 提示词模板

使用预设模板格式：

```
内容：[用户填写具体描述]

要求：
1、解析 Mermaid flowchart 语法，生成渐变背景 + 毛玻璃卡片的信息图
2、支持 TD（垂直）和 LR（横向）布局
3、自动水印（题材调研员）、emoji 匹配、品牌定制
4、主题：hand-drawn-edu | 手绘风教育插画 | 米白纸张背景 + 手绘边框 | #E8655A
```

### 3. 执行生成

脚本位置：`~/.hermes/skills/creative/chatgpt-image-gen/scripts/generate_image.py`

**示例用法**：

```bash
# 生成光模块规格演进信息图
python ~/.hermes/skills/creative/chatgpt-image-gen/scripts/generate_image.py \
  --file ~/.hermes/skills/creative/chatgpt-image-gen/prompt-光模块规格演进.txt \
  --output ~/Desktop/光模块规格演进.png
```

## API 说明

### OpenAI GPT-4o Image Generation

GPT-4o 支持图片生成功能，通过 Chat Completions API 调用：

```python
from openai import OpenAI

client = OpenAI(api_key="sk-xxx")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "生成一张信息图..."}
    ]
)
```

### 适用场景

根据 OpenAI 官方说明，GPT-image-2 API 适用于：

- 本地化广告制作
- 信息图生成
- 教育内容创作
- 设计工具集成
- 营销素材自动化

## 提示词模板库

### 信息图模板（公众号风格）

```
内容：[标题]

要求：
1、解析 Mermaid flowchart 语法，生成渐变背景 + 毛玻璃卡片的信息图
2、支持 TD（垂直）和 LR（横向）布局
3、自动水印（题材调研员）、emoji 匹配、品牌定制
4、主题：hand-drawn-edu | 手绘风教育插画 | 米白纸张背景 + 手绘边框 | #E8655A
```

### 简洁风格模板

```
内容：[描述内容]

风格：极简、专业、商务
配色：蓝色系 + 白色背景
尺寸：适合微信公众号（竖屏 800px 宽）
```

### 教育内容模板

```
内容：[知识点描述]

风格：手绘、教育、亲和
配色：暖色调（米黄、橙色、粉色）
元素：手绘图标、涂鸦边框、便利贴
字体：手写体
```

## 注意事项

- API 调用需要付费，按图片生成次数计费
- GPT-4o 图片生成需要 Plus 或 Pro 订阅权限
- 图片生成时间约 10-30 秒
- 生成结果可能包含文字描述而非图片，需根据响应类型处理

## 故障排查

| 问题 | 解决方案 |
|------|---------|
| API Key 无效 | 检查 API Key 是否正确，是否有 GPT-4o 权限 |
| 权限不足 | 确认账号有 Plus/Pro 订阅或 API 付费权限 |
| 返回文本而非图片 | GPT-4o 可能返回图片描述，需要二次请求 |
| 图片质量不佳 | 优化提示词，添加更具体的风格要求 |

## 相关技能

- `flowchart-to-instagram` - 本地信息图生成（无需 API）
- `beautiful-mermaid` - Mermaid 图表美化
- `mcp/chrome-screenshot` - 网页截图