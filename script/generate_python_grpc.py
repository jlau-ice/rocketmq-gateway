#!/usr/bin/env python3
"""
生成Python gRPC代码的脚本
"""

import subprocess
import sys
import os

def generate_grpc_code():
    """生成Python gRPC代码"""
    print("🔧 生成Python gRPC代码...")
    
    # 检查protoc是否安装
    try:
        result = subprocess.run(['protoc', '--version'], capture_output=True, text=True)
        print(f"✅ 找到protoc: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ 未找到protoc，请先安装Protocol Buffers编译器")
        print("   Windows: 下载 https://github.com/protocolbuffers/protobuf/releases")
        print("   或使用: choco install protoc")
        return False
    
    # 创建输出目录
    os.makedirs('python_grpc', exist_ok=True)
    
    # 生成Python代码
    cmd = [
        'protoc',
        '--python_out=python_grpc',
        '--grpc_python_out=python_grpc',
        'proto/mq.proto'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Python gRPC代码生成成功!")
            print("   生成的文件:")
            for file in os.listdir('python_grpc'):
                print(f"   - {file}")
            return True
        else:
            print(f"❌ 生成失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ 执行错误: {e}")
        return False

if __name__ == "__main__":
    if generate_grpc_code():
        print("\n🎉 现在可以运行Python客户端测试了!")
        print("   python test_python_client.py")
    else:
        print("\n❌ 生成失败，请检查protoc安装")
        sys.exit(1)
