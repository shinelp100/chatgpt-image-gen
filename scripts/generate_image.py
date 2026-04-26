#!/usr/bin/env python3
"""
ChatGPT GPT-4o 图片生成 API 客户端

使用 OpenAI API 的 GPT-4o 模型生成高质量图片。
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


def generate_image(client: OpenAI, prompt: str) -> bytes:
    """使用 GPT-4o API 生成图片"""
    
    # 添加默认要求模板
    full_prompt = f"""{prompt}

请根据以上内容生成一张高质量的信息图图片。
风格要求:
1. 清晰的视觉层次和专业排版
2. 适合微信公众号竖屏展示 (宽度800px)
3. 渐变背景 + 毛玻璃卡片效果
4. 手绘风教育插画风格
5. 米白纸张背景 + 手绘边框"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": full_prompt
                }
            ]
        )
        
        # 检查响应中是否有图片内容
        message = response.choices[0].message
        
        # GPT-4o 图片生成返回图片 URL 或 base64 数据
        if hasattr(message, 'content') and message.content:
            # 如果是文本响应，可能包含图片描述或 URL
            return message.content
        
        # 如果有图片附件
        if hasattr(message, 'image') and message.image:
            return message.image
        
    except Exception as e:
        print(f"API 调用错误: {e}")
        sys.exit(1)


def save_image(image_data: bytes, output_path: str):
    """保存图片"""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # 如果是 base64 数据
    if isinstance(image_data, str) and image_data.startswith('data:image'):
        # 解析 base64
        base64_data = image_data.split(',')[1]
        image_bytes = base64.b64decode(base64_data)
        with open(output_file, 'wb') as f:
            f.write(image_bytes)
    elif isinstance(image_data, str) and image_data.startswith('http'):
        # URL，需要下载
        import urllib.request
        urllib.request.urlretrieve(image_data, output_file)
    elif isinstance(image_data, bytes):
        with open(output_file, 'wb') as f:
            f.write(image_data)
    else:
        # 文本响应，保存为描述文件
        with open(output_file.with_suffix('.txt'), 'w', encoding='utf-8') as f:
            f.write(image_data)
        print(f"警告: API 返回文本而非图片，已保存到 {output_file.with_suffix('.txt')}")
    
    print(f"图片已保存: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='使用 GPT-4o API 生成图片'
    )
    parser.add_argument('--prompt', '-p', help='图片生成提示词')
    parser.add_argument('--file', '-f', help='提示词文件路径')
    parser.add_argument('--output', '-o', default='output.png', help='输出图片路径')
    parser.add_argument('--api-key', help='OpenAI API Key (或设置 OPENAI_API_KEY 环境变量)')
    
    args = parser.parse_args()
    
    # 初始化 OpenAI 客户端
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("错误: 请设置 OPENAI_API_KEY 环境变量或使用 --api-key 参数")
        print("获取 API Key: https://platform.openai.com/api-keys")
        sys.exit(1)
    
    client = OpenAI(api_key=api_key)
    
    # 加载提示词
    prompt = load_prompt(args.file, args.prompt)
    
    print("正在生成图片...")
    print(f"提示词长度: {len(prompt)} 字符")
    
    # 生成图片
    image_data = generate_image(client, prompt)
    
    # 保存图片
    save_image(image_data, args.output)


if __name__ == '__main__':
    main()