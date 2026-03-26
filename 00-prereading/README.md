# 前置阅读：Embeddings

**资源**：[Embeddings - OpenAI Platform](https://platform.openai.com/docs/guides/embeddings)

**目的**：理解向量化与相似度检索的原理，为里程碑五的 RAG 系统构建（子目标3）做概念铺垫。

**预计时间**：30分钟（仅阅读主页面，不跑 notebook）

> **注意**：该页面 Use cases 区域链接了11个 Jupyter Notebook，每个都是完整实操练习。本前置阅读**只需读主页面的概念描述**，理解核心概念即可。相关 notebook 在后续 RAG 子目标学习时按需参考。

## 核心概念

阅读时重点关注：

- 什么是 embedding，为什么可以用向量表示语义
- 余弦相似度的直觉理解
- OpenAI embedding 模型的输入输出格式
- 典型使用场景：语义搜索、聚类、推荐（读概念描述，不需要跑 notebook）

## Use cases Notebooks 参考指引（按需查阅，不在前置阅读范围内）

以下 notebook 在进入对应子目标时再看，不要在前置阅读阶段全部学完：

| Notebook | 建议时机 |
|---|---|
| [Get embeddings from dataset](https://github.com/openai/openai-cookbook/blob/main/examples/Get_embeddings_from_dataset.ipynb) | 开始构建 RAG 前，了解 API 基础调用 |
| [Question answering using embeddings](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb) | 子目标3 RAG 构建阶段，核心参考 |
| [Semantic text search using embeddings](https://github.com/openai/openai-cookbook/blob/main/examples/Semantic_text_search_using_embeddings.ipynb) | 子目标3 RAG 构建阶段，核心参考 |
| [Visualizing embeddings in 2D](https://github.com/openai/openai-cookbook/blob/main/examples/Visualizing_embeddings_in_2D.ipynb) | 可选，有助于直觉理解向量空间 |
| [Clustering](https://github.com/openai/openai-cookbook/blob/main/examples/Clustering.ipynb) | 可选，里程碑六评估阶段参考 |
| Code search / Recommendation / Regression / Classification / Zero-shot / User & product | 暂不需要，超出本里程碑范围 |
