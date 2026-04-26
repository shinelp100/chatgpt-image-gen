#!/usr/bin/env python3
"""
ChatGPT GPT-image-2 图片生成 API 客户端

使用 OpenAI gpt-image-2 模型生成高质量图片。
适用于本地化广告、信息图、教育内容、设计工具等业务场景。

使用方式:
    python generate_image.py --prompt "内容描述" --output output.png
    python generate_image.py --file prompt.txt --output output.png
"""

import argparse
import os
import sys
import base64
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("请先安装 openai 库: pip install openai")
    sys.exit(1)


def load_prompt(prompt_file: str = None, prompt_text: str = None) -> str:
    """加载提示词"""
    if prompt_file:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    elif prompt_text:
        return prompt_text.strip()
    else:
        print("错误: 请提供 --prompt 或 --file 参数")
        sys.exit(1)


def generate_image_with_chat(client: OpenAI, prompt: str, model: str = "gpt-4o"):
    """使用 Chat Completions API 生成图片"""
    
    # 构建完整提示词
    full_prompt = f"""请根据以下内容生成一张高质量的信息图图片：

{prompt}

图片要求：
1. 清晰的视觉层次和专业排版
2. 适合微信公众号竖屏展示（宽度800px）
3. 渐变背景 + 毛玻璃卡片效果
4. 手绘风教育插画风格
5. 米白纸张背景 + 手绘边框
6. 红色主题色 #E8655A

请直接生成图片，不要返回文字描述。"""
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user", 
                    "content": full_prompt
                }
            ]
        )
        
        message = response.choices[0].message
        return message.content
        
    except Exception as e:
        print(f"Chat API 调用错误: {e}")
        return None


def generate_image_with_images_api(client: OpenAI, prompt: str, model: str = "dall-e-3"):
    """使用 Images API (DALL-E) 生成图片"""
    
    # 构建完整提示词
    full_prompt = f"""Create a high-quality infographic image based on the following content:

{prompt}

Image requirements:
1. Clear visual hierarchy and professional layout
2. Vertical format suitable for WeChat公众号 (800px width)
3. Gradient background with frosted glass card effects
4. Hand-drawn educational illustration style
5. Cream paper background with hand-drawn borders
6. Red theme color #E8655A"""
    
    try:
        response = client.images.generate(
            model=model,
            prompt=full_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        return image_url
        
    except Exception as e:
        print(f"Images API 调用错误: {e}")
        return None


def generate_image_with_gpt_image_2(client: OpenAI, prompt: str):
    """使用 gpt-image-2 模型生成图片"""
    
    full_prompt = f"""生成一张信息图：

{prompt}

要求：
- 渐变背景 + 毛玻璃卡片
- 手绘风教育插画风格
- 米白纸张背景 + 手绘边框
- 红色主题色 #E8655A
- 竖屏 800px 宽度"""
    
    try:
        # gpt-image-2 可能使用 Chat Completions API
        response = client.chat.completions.create(
            model="gpt-image-2",
            messages=[
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            # 请求图片输出
            response_format={"type": "image"}
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"gpt-image-2 API 调用错误: {e}")
        # 尝试备用方案
        print("尝试使用 DALL-E 3...")
        return generate_image_with_images_api(client, prompt)


def save_image(image_data, output_path: str):
    """保存图片"""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    if image_data is None:
        print("错误: 未获取到图片数据")
        sys.exit(1)
    
    # URL 方式
    if isinstance(image_data, str) and image_data.startswith('http'):
        import urllib.request
        print(f"正在下载图片: {image_data}")
        urllib.request.urlretrieve(image_data, output_file)
        print(f"图片已保存: {output_file}")
        return
    
    # Base64 方式
    if isinstance(image_data, str) and 'data:image' in image_data:
        # 提取 base64 数据
        if ',' in image_data:
            base64_data = image_data.split(',')[1]
        else:
            base64_data = image_data
        image_bytes = base64.b64decode(base64_data)
        with open(output_file, 'wb') as f:
            f.write(image_bytes)
        print(f"图片已保存: {output_file}")
        return
    
    # 纯文本响应
    if isinstance(image_data, str):
        # 检查是否包含图片 URL
        import re
        urls = re.findall(r'https?://[^\s<>"]+?\.(png|jpg|jpeg|webp|gif)', image_data)
        if urls:
            print(f"发现图片 URL: {urls[0]}")
            import urllib.request
            urllib.request.urlretrieve(urls[0], output_file)
            print(f"图片已保存: {output_file}")
            return
        
        # 保存为文本
        txt_file = output_file.with_suffix('.txt')
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(image_data)
        print(f"警告: API 返回文本而非图片")
        print(f"文本已保存: {txt_file}")
        print(f"\n内容预览:\n{image_data[:500]}...")
        return
    
    # Bytes 方式
    if isinstance(image_data, bytes):
        with open(output_file, 'wb') as f:
            f.write(image_data)
        print(f"图片已保存: {output_file}")
        return


def main():
    parser = argparse.ArgumentParser(
        description='使用 OpenAI API 生成图片'
    )
    parser.add_argument('--prompt', '-p', help='图片生成提示词')
    parser.add_argument('--file', '-f', help='提示词文件路径')
    parser.add_argument('--output', '-o', default='output.png', help='输出图片路径')
    parser.add_argument('--api-key', help='OpenAI API Key')
    parser.add_argument('--model', '-m', default='gpt-image-2', 
                        choices=['gpt-image-2', 'gpt-4o', 'dall-e-3'],
                        help='生成模型')
    
    args = parser.parse_args()
    
    # 初始化客户端
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("错误: 请设置 OPENAI_API_KEY 环境变量")
        print("获取 API Key: https://platform.openai.com/api-keys")
        sys.exit(1)
    
    client = OpenAI(api_key=api_key)
    
    # 加载提示词
    prompt = load_prompt(args.file, args.prompt)
    
    print("=" * 50)
    print("正在生成图片...")
    print(f"模型: {args.model}")
    print(f"提示词长度: {len(prompt)} 字符")
    print("=" * 50)
    
    # 根据模型选择生成方式
    if args.model == 'gpt-image-2':
        image_data = generate_image_with_gpt_image_2(client, prompt)
    elif args.model == 'dall-e-3':
        image_data = generate_image_with_images_api(client, prompt)
    else:
        image_data = generate_image_with_chat(client, prompt, args.model)
    
    # 保存图片
    save_image(image_data, args.output)


if __name__ == '__main__':
    main()