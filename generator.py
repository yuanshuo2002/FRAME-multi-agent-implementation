import os
from langchain_openai import ChatOpenAI

class GeneratorAgent:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="qwen-plus",
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0.7
        )

    def generate(self, topic, feedback=None):

        if feedback:
            prompt = f"""
            根据以下反馈优化摘要：

            主题：{topic}

            反馈：
            {feedback}

            请生成改进后的摘要。
            """
        else:
            prompt = f"""
            请为以下主题写一个学术论文摘要：

            主题：{topic}
            """

        response = self.llm.invoke(prompt)

        return response.content