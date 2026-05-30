import os
import requests
from datetime import datetime

def scrape():
    # 从环境变量获取目标 URL，默认为 example.com
    url = os.environ.get("TARGET_URL", "https://example.com")
    output_dir = "data"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"正在抓取: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # 记录抓取时间
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"page_{timestamp}.html"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response.text)
            
        # 同时更新一个最新的版本
        latest_path = os.path.join(output_dir, "latest.html")
        with open(latest_path, "w", encoding="utf-8") as f:
            f.write(response.text)
            
        print(f"抓取成功！保存至: {filepath}")
        
    except Exception as e:
        print(f"抓取失败: {e}")
        exit(1)

if __name__ == "__main__":
    scrape()
