from agents.generator import GeneratorAgent
from agents.evaluator import EvaluatorAgent
from agents.reflector import ReflectorAgent


class FramePipeline:

    def __init__(self, iterations=2):

        self.generator = GeneratorAgent()
        self.evaluator = EvaluatorAgent()
        self.reflector = ReflectorAgent()

        self.iterations = iterations

    def run(self, topic):

        feedback = None
        text = None

        for i in range(self.iterations):

            print(f"\n===== Iteration {i+1} =====")

            # 1 生成摘要
            text = self.generator.generate(topic, feedback)

            print("\nGenerated Text:\n")
            print(text)

            # 2 评价摘要
            evaluation = self.evaluator.evaluate(text)

            print("\nEvaluation:\n")
            print(evaluation)

            # 3 生成反馈
            feedback = self.reflector.reflect(evaluation)

            print("\nReflection / Suggestions:\n")
            print(feedback)

        return text