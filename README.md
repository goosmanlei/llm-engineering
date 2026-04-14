# llm-engineering

里程碑五：LLM 工程入门的学习记录仓库。

> 目标：能用 API 和主流框架构建实际的 LLM 应用，具备基本的工程化能力。
>
> 注意：这是第一个"构建"导向的里程碑，和前四个"理解"导向的里程碑不同——遇到的主要障碍是"调不通为什么"而不是"听不懂理论"，需要主动查文档、在报错中学习。

## 子目标

- 子目标1：LLM API 熟练集成（调参、roles设计、token管理、流式输出、错误重试）
- 子目标2：Prompt Engineering 基础（zero-shot/few-shot、CoT、多步骤链、结构化输出）
- 子目标3：RAG 系统完整构建（分块、Embedding、向量库、检索策略、带来源的生成）
- 子目标4：简单 Agent 构建（ReAct模式、工具定义、多步骤推理、终止条件）
- 子目标5：LLM 应用框架使用（用 LangChain 作为工具实现链式组合、对话记忆、调试；框架是手段，不是目标）
- 子目标6：基础评估能力（测试集构建、定量对比、LLM-as-judge思路）

## 目录结构

```
llm-engineering/
├── 00-prereading/              # 前置阅读：Embeddings 概念
├── 01-prompt-engineering/      # ChatGPT Prompt Engineering for Developers
├── 02-fullstack-llm-bootcamp/  # Full Stack LLM Bootcamp
├── 03-langchain/               # Introduction to LangChain - Python
├── 04-intro-langgraph/         # Introduction to LangGraph - Python
├── 05-intro-langsmith/         # Introduction to LangSmith
├── 06-deep-agents/             # Project: Deep Agents with LangGraph
├── 07-deep-research/           # Project: Deep Research with LangGraph
├── 08-ambient-agents/          # Project: Ambient Agents with LangGraph
├── 09-advanced-rag/            # Building and Evaluating Advanced RAG
├── 10-context-engineering/     # Effective Context Engineering（选读）
└── projects/                   # 验收项目
    ├── 01-doc-qa-rag/          # 项目一：文档问答 RAG 系统
    ├── 02-research-agent/      # 项目二：带工具调用的研究助手 Agent
    └── 03-learning-assistant/  # 项目三：个人学习助手 Bot
```

## 学习资源（按顺序）

| # | 资源 | 说明 | 对应子目标 |
|---|------|------|-----------|
| 前置 | [Embeddings - OpenAI Platform](https://platform.openai.com/docs/guides/embeddings) | 约30分钟，只读主页面概念部分，不跑 Use cases notebook；相关 notebook 在子目标3阶段按需参考 | — |
| 1 | [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) | 1小时，免费 | 1、2 |
| 2 | [Full Stack LLM Bootcamp - Full Stack Deep Learning](https://www.youtube.com/playlist?list=PL1T8fO7ArWleyIqOy37OVXsP4hFXymdOZ) | 视野型课程，重点学安全、成本、UX、产品化思路 | — |
| 3 | [Introduction to LangChain - Python](https://academy.langchain.com/courses/foundation-introduction-to-langchain-python) | LCEL 现代语法，系统学习 | 3、4、5 |
| 4 | [Introduction to LangGraph - Python](https://academy.langchain.com/courses/intro-to-langgraph) | LangGraph 核心基础：State、Node、Edge、Graph | 4、5 |
| 5 | [Introduction to LangSmith](https://academy.langchain.com/courses/intro-to-langsmith) | LLM 应用的追踪、调试与评估，建立可观测性 | 5、6 |
| 6 | [Project: Deep Agents with LangGraph](https://academy.langchain.com/courses/deep-agents-with-langgraph) | 构建单 Agent + Tool 执行图，理解 state 管理与 loop / planning | 4、5 |
| 7 | [Project: Deep Research with LangGraph](https://academy.langchain.com/courses/deep-research-with-langgraph) | Agent 叠加 RAG + 多步推理，复杂任务分解 | 3、4 |
| 8 | [Project: Ambient Agents with LangGraph](https://academy.langchain.com/courses/ambient-agents) | 长生命周期 Agent、事件驱动、持续上下文管理 | 4 |
| 9 | [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) | 1小时，免费，专项强化 RAG 构建与评估 | 3、6 |
| 10 | [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 选读，了解趋势即可 | 4 |

## 环境配置

**一键创建 mamba 环境（Python 3.11）**

```bash
mamba env create -f environment.yml
mamba activate llm-eng
pip install -r requirements.txt
```


## 验收项目

- **项目一**：文档问答 RAG 系统（验收子目标1、2、3、5）
- **项目二**：带工具调用的研究助手 Agent（验收子目标1、2、4、5）
- **项目三**：个人学习助手 Bot（验收全部子目标）
