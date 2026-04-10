import os
from langchain_openai import ChatOpenAI


class ReflectorAgent:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="qwen-plus",
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0
        )

    def reflect(self, evaluation):

        prompt = f"""
        根据以下评价结果，总结改进建议。

        评价内容：
        {evaluation}

        请给出明确的修改方向，
        帮助生成更高质量的学术摘要。
        """

        response = self.llm.invoke(prompt)

        return response.content
