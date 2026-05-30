# autocpy

一个基于 GitHub Action 的自动化静态网页抓取工具。

## 功能特性

- **定期抓取**: 使用 GitHub Actions 定期运行爬虫脚本。
- **自动存档**: 抓取的内容会自动提交并推送回 GitHub 仓库。
- **历史追溯**: 每次抓取都会生成带时间戳的文件，方便查看历史版本。
- **简单配置**: 通过环境变量即可更改抓取目标。

## 快速开始

### 1. 配置目标 URL
在 GitHub 仓库的 **Settings -> Secrets and variables -> Actions -> Variables** 中添加：
- `TARGET_URL`: 你想要抓取的网页地址（例如 `https://example.com`）。

### 2. 启用权限
为了让 GitHub Action 能够自动提交代码，请前往：
**Settings -> Actions -> General -> Workflow permissions**
选择 **Read and write permissions** 并保存。

### 3. 查看结果
抓取到的页面将保存在 `data/` 目录中。

## 本地开发

安装依赖：
```bash
pip install -r requirements.txt
```

运行爬虫：
```bash
python main.py
```

## 许可证
MIT
