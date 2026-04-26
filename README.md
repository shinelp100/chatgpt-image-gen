# ChatGPT Image Generation

使用 ChatGPT GPT-4o 的图片生成功能，提供提示词模板和约束条件。

## 功能特点

- 预设提示词模板（信息图风格）
- 支持自定义约束条件
- 适合微信公众号信息图生成

## 重要限制

**Cloudflare Turnstile 拦截**：ChatGPT 使用 Cloudflare 安全验证，自动化浏览器会被检测为机器人。**推荐使用手动模式或 API 方案**。

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

## 替代方案

### Ideogram API（推荐）

Ideogram 文字渲染能力最强，最适合信息图生成。

```bash
# 获取 API Key: https://ideogram.ai/settings/api
export IDEOGRAM_API_KEY="your-api-key"

# 生成图片
python ~/.hermes/skills/creative/chatgpt-image-gen/scripts/ideogram_generate.py \
  --file prompt.txt --output output.png --aspect 10_16
```

**优势**：
- 文字渲染最强（信息图核心需求）
- 每日免费额度（约 10-20 张）
- API 可自动化调用
- 中文支持良好

### 其他推荐模型

| 模型 | 特点 | 免费 | 推荐度 |
|------|------|------|--------|
| 通义万相 | 中文理解最佳 | ✅ 新用户额度 | ⭐⭐⭐⭐⭐ |
| Bing Image Creator | DALL-E 3 质量 | ✅ 每日 15 张 | ⭐⭐⭐⭐ |
| Stable Diffusion 本地 | 完全免费无限制 | ✅✅ | ⭐⭐⭐⭐⭐ |
| FLUX.1 本地 | 高质量开源 | ✅✅ | ⭐⭐⭐⭐ |

### 本地渲染（flowchart-to-instagram）

完全自动化，无 Cloudflare 问题：

```bash
python ~/.hermes/skills/flowchart-to-instagram/scripts/flowchart_renderer.py \
  input.mmd --output output.png
```

## Cloudflare 检测说明

Chrome DevTools MCP 被 Cloudflare Turnstile 拦截的原因：

- `navigator.webdriver === true`（自动化标志）
- CDP 远程调试端口开放
- 浏览器指纹异常
- 用户行为机械化

**重要**：Host 配置无法绕过 Cloudflare，检测基于浏览器特征而非资源加载。

## 相关技能

- `flowchart-to-instagram` - 本地信息图生成（无需 ChatGPT）
- `beautiful-mermaid` - Mermaid 图表美化

## 许可证

MIT License

## 作者

shinelp100