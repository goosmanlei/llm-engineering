# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目背景

这是一个 LLM 工程入门学习仓库，目标是能用 API 和主流框架构建实际的 LLM 应用。这是一个**构建导向**的里程碑，主要产出是 Jupyter Notebook 笔记和 `projects/` 下的验收项目。

## 环境

- mamba 环境名：`llm-eng`，Python 3.11
- 创建：`mamba env create -f environment.yml -y`
- 激活：`mamba activate llm-eng`
- 注册 Jupyter kernel：`python -m ipykernel install --user --name llm-eng --display-name "llm-eng"`
- API keys 存放在项目根目录的 `.env` 文件（已 gitignore），用 `python-dotenv` 加载

## 目录结构

每个 `0X-*/` 目录对应一个学习模块，内容为 Jupyter Notebook。`projects/` 下是三个验收项目（RAG、Agent、Bot），尚未开始开发。

## 协作原则

- **文档**：保持简洁，只写当前需要的内容，不为假设的未来场景做额外说明
- **代码**：保持版本统一，修复兼容性问题后直接呈现最终代码，不保留旧版本写法，不在注释中解释版本差异
- **注释与输出**：用中文写适度详细的注释和 print 输出，帮助理解 LLM 相关概念和 API 用法

## 依赖管理

- `environment.yml` 只负责创建 Python 3.11 环境，不声明 pip 包
- `requirements.txt` 管理所有 pip 依赖，环境创建后用 `pip install -r requirements.txt` 安装
- 新增依赖时只需更新 `requirements.txt`
