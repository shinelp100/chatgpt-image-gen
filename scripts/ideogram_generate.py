#!/usr/bin/env python3
"""
Ideogram API 图片生成客户端

Ideogram 文字渲染能力最强，最适合信息图生成。
API 文档: https://ideogram.ai/api

使用方式:
    python ideogram_generate.py --prompt "描述" --output output.png
    python ideogram_generate.py --file prompt.txt --output output.png
"""

import argparse
import os
import sys
import requests
import base64
from pathlib import Path
from datetime import datetime


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


def generate_image(api_key: str, prompt: str, aspect_ratio: str = "ASPECT_RATIO_10_16"):
    """
    使用 Ideogram API 生成图片
    
    Args:
        api_key: Ideogram API Key
        prompt: 图片描述
        aspect_ratio: 图片比例
            - ASPECT_RATIO_1_1 (正方形)
            - ASPECT_RATIO_10_16 (竖屏，适合公众号)
            - ASPECT_RATIO_16_10 (横屏)
            - ASPECT_RATIO_9_16 (竖屏手机)
            - ASPECT_RATIO_16_9 (横屏视频)
    
    Returns:
        图片 URL 或 base64 数据
    """
    
    # Ideogram API endpoint
    url = "https://api.ideogram.ai/generate"
    
    headers = {
        "Api-Key": api_key,
        "Content-Type": "application/json"
    }
    
    # 构建请求
    data = {
        "image_request": {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "model": "V_2",  # V_2 是最新高质量模型
            "magic_prompt_option": "ON",  # 自动优化提示词
            "style_type": "GENERAL",  # 通用风格
        }
    }
    
    try:
        print("正在调用 Ideogram API...")
        response = requests.post(url, headers=headers, json=data, timeout=120)
        
        if response.status_code == 200:
            result = response.json()
            
            # 提取图片数据
            if "created" in result and "data" in result:
                images = result["data"]
                if len(images) > 0:
                    # 获取第一张图片
                    image_info = images[0]
                    
                    # 图片可能返回 URL 或 base64
                    if "url" in image_info:
                        return {"type": "url", "data": image_info["url"]}
                    elif "base64" in image_info:
                        return {"type": "base64", "data": image_info["base64"]}
            
            print(f"API 返回格式异常: {result}")
            return None
            
        elif response.status_code == 401:
            print("错误: API Key 无效或未设置")
            print("获取 API Key: https://ideogram.ai/settings/api")
            return None
            
        elif response.status_code == 402:
            print("错误: 余额不足或订阅已过期")
            return None
            
        elif response.status_code == 429:
            print("错误: 请求频率超限，请稍后再试")
            return None
            
        else:
            print(f"API 调用失败: {response.status_code}")
            print(f"响应: {response.text}")
            return None
            
    except requests.exceptions.Timeout:
        print("错误: API 请求超时 (120秒)")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"网络请求错误: {e}")
        return None


def save_image(image_data: dict, output_path: str):
    """保存图片"""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    if image_data is None:
        print("错误: 未获取到图片数据")
        sys.exit(1)
    
    if image_data["type"] == "url":
        # 下载图片
        print(f"正在下载图片: {image_data['data']}")
        response = requests.get(image_data["data"], timeout=30)
        if response.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"图片已保存: {output_file}")
        else:
            print(f"下载失败: {response.status_code}")
            sys.exit(1)
            
    elif image_data["type"] == "base64":
        # 解码 base64
        image_bytes = base64.b64decode(image_data["data"])
        with open(output_file, 'wb') as f:
            f.write(image_bytes)
        print(f"图片已保存: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='使用 Ideogram API 生成图片'
    )
    parser.add_argument('--prompt', '-p', help='图片生成提示词')
    parser.add_argument('--file', '-f', help='提示词文件路径')
    parser.add_argument('--output', '-o', default='ideogram_output.png', help='输出图片路径')
    parser.add_argument('--api-key', help='Ideogram API Key')
    parser.add_argument('--aspect', '-a', default='10_16',
                        choices=['1_1', '10_16', '16_10', '9_16', '16_9'],
                        help='图片比例 (默认 10_16 竖屏公众号)')
    
    args = parser.parse_args()
    
    # 获取 API Key
    api_key = args.api_key or os.getenv('IDEOGRAM_API_KEY')
    if not api_key:
        print("=" * 60)
        print("错误: 请设置 Ideogram API Key")
        print("=" * 60)
        print("\n获取方式:")
        print("1. 注册 Ideogram 账号: https://ideogram.ai")
        print("2. 进入设置页面: https://ideogram.ai/settings/api")
        print("3. 生成 API Key")
        print("\n使用方式:")
        print("  export IDEOGRAM_API_KEY='your-api-key'")
        print("  python ideogram_generate.py --prompt '...' --output output.png")
        sys.exit(1)
    
    # 加载提示词
    prompt = load_prompt(args.file, args.prompt)
    
    # 转换比例格式
    aspect_map = {
        '1_1': 'ASPECT_RATIO_1_1',
        '10_16': 'ASPECT_RATIO_10_16',
        '16_10': 'ASPECT_RATIO_16_10',
        '9_16': 'ASPECT_RATIO_9_16',
        '16_9': 'ASPECT_RATIO_16_9',
    }
    aspect_ratio = aspect_map[args.aspect]
    
    print("=" * 60)
    print("Ideogram 图片生成")
    print("=" * 60)
    print(f"提示词长度: {len(prompt)} 字符")
    print(f"图片比例: {args.aspect} ({aspect_ratio})")
    print(f"输出路径: {args.output}")
    print("=" * 60)
    
    # 生成图片
    image_data = generate_image(api_key, prompt, aspect_ratio)
    
    # 保存图片
    if image_data:
        save_image(image_data, args.output)
    else:
        print("生成失败")
        sys.exit(1)


if __name__ == '__main__':
    main()