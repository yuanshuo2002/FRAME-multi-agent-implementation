import os
from langchain_openai import ChatOpenAI


class EvaluatorAgent:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="qwen-plus",
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0
        )

    def evaluate(self, text):

        prompt = f"""
        请评价下面摘要的质量。

        从以下方面评分（1-10）：

        1. 逻辑性
        2. 学术性
        3. 完整性

        摘要：
        {text}

        请按如下格式输出：

        Score:
        Feedback:
        """

        response = self.llm.invoke(prompt)

        return response.content
