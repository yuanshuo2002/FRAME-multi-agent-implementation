# FRAME Agent 项目

基于多智能体系统的 FRAME（Feedback-Refined Agent Methodology）框架的 Python 实现，用于迭代式内容优化。

## 📋 项目概述

本项目实现了 FRAME 系统的简化版本，通过多智能体架构模拟学术论文写作流程。系统由三个专业智能体组成，在反馈循环中协作生成和优化学术论文摘要。

### 核心架构

```
Generator  →  Evaluator  →  Reflector
      ↑_______________________|
```

## 🏗️ 系统组件

### 1. 生成器智能体 (Generator Agent)
- **功能**：根据给定主题生成学术论文摘要
- **职责**：创建初始内容并根据反馈进行优化
- **模型**：通过 DashScope API 使用 Qwen-Plus 大语言模型

### 2. 评估器智能体 (Evaluator Agent)  
- **功能**：评估生成摘要的质量
- **评估标准**： 
  - 逻辑性 (1-10分)
  - 学术性 (1-10分)
  - 完整性 (1-10分)
- **模型**：使用 Qwen-Plus 模型，temperature=0 确保评估一致性

### 3. 反思器智能体 (Reflector Agent)
- **功能**：分析评估结果并提供可操作的反馈
- **职责**：为生成器总结改进建议
- **模型**：使用 Qwen-Plus 模型，temperature=0 确保反馈专注

## 🔄 工作流程

1. **初始生成**：生成器为给定主题创建摘要
2. **质量评估**：评估器评估摘要并提供评分
3. **反馈生成**：反思器分析评估结果并建议改进
4. **迭代优化**：过程重复指定的迭代次数（默认：2次）

## 🚀 快速开始

### 前置要求
- Python 3.8+
- DashScope API 密钥（来自阿里云）

### 安装步骤

1. 克隆仓库：
```bash
git clone <repository-url>
cd frame-agent-project
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 设置环境变量：
```bash
export DASHSCOPE_API_KEY="your-dashscope-api-key"
```

### 使用方法

运行主流程：
```bash
python main.py
```

系统将为主题"AI Agents in scientific research"生成并优化学术论文摘要。

## 📁 项目结构

```
frame-agent-project/
├── agents/           # 智能体实现
│   ├── generator.py     # 内容生成智能体
│   ├── evaluator.py     # 质量评估智能体
│   └── reflector.py     # 反馈生成智能体
├── workflow/         # 流程编排
│   └── frame_pipeline.py  # 主流程控制器
├── main.py          # 入口文件
├── requirements.txt # 依赖项
└── README.md        # 本文件
```

## 🔧 配置说明

### 模型设置
所有智能体通过 DashScope API 使用 Qwen-Plus 模型。可以在每个智能体的 `__init__` 方法中修改配置：

- **生成器**：temperature=0.7 用于创造性生成
- **评估器**：temperature=0 用于一致性评估
- **反思器**：temperature=0 用于专注反馈

### 迭代控制
在 `main.py` 中修改优化迭代次数：
```python
pipeline = FramePipeline(iterations=3)  # 修改迭代次数
```

## 🎯 示例输出

系统生成输出显示每次迭代的进展：

```
===== Iteration 1 =====
Generated Text:
[摘要内容...]

Evaluation:
Score: 7/10
Feedback: [评估反馈...]

Reflection / Suggestions:
[改进建议...]
```

## 📚 依赖项

- **langchain**：构建 LLM 应用的框架
- **langchain-openai**：OpenAI 兼容的 LLM 集成
- **openai**：OpenAI API 客户端
- **python-dotenv**：环境变量管理

## 🔬 技术细节

### 框架
- 使用 LangChain 进行智能体编排
- 实现具有专业提示的自定义智能体类
- 使用 OpenAI 兼容的 API 端点访问模型

### 提示工程
每个智能体使用精心设计的提示：
- **生成器**：主题特定的摘要生成，集成反馈
- **评估器**：结构化评分系统，标准明确
- **反思器**：可操作的反馈总结

## 🎓 学术背景

本项目实现了 FRAME（Feedback-Refined Agent Methodology）研究的核心概念，展示了：
- 多智能体协作进行内容优化
- 通过反馈循环进行迭代改进
- 内容创建工作流中的专业智能体角色

## 🔮 未来增强

潜在改进包括：
- 支持多个 LLM 提供商
- 可自定义的评估标准
- 使用 Streamlit 的 Web 界面
- 多主题批量处理
- 与学术数据库集成

## 📄 许可证

本项目创建用于教育和研究目的。

## 🤝 贡献

这是一个研究复现项目。如有建议或改进，请提交 issue 或 pull request。

---

**注意**：本项目需要有效的阿里云 DashScope API 密钥才能正常运行。