from workflow.frame_pipeline import FramePipeline


def main():

    topic = "AI Agents in scientific research"

    pipeline = FramePipeline(iterations=2)

    final_result = pipeline.run(topic)

    print("\n\n===== Final Result =====\n")
    print(final_result)


if __name__ == "__main__":
    main()