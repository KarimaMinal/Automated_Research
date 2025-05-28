from agents.researcher import ResearchAgent
from agents.summarizer import SummarizerAgent
from agents.categorizer import CategorizerAgent
from agents.writer import WriterAgent
from agents.critic import CriticAgent


def run_autoscholar(topic: str, max_papers: int = 5):
    print(f"[System] Starting AutoScholar on topic: '{topic}' with max {max_papers} papers")

    # Step 1: Research papers
    papers = ResearchAgent().run(topic, max_results=max_papers)

    # Step 2: Summarize papers
    summaries = SummarizerAgent().run(papers)

    # Step 3: Categorize summaries
    categories = CategorizerAgent().run(summaries)

    # Step 4: Generate report
    report = WriterAgent().run(categories)

    # Step 5: Critique report
    CriticAgent().run(report)

    print("[System] AutoScholar process complete!")


if __name__ == "__main__":
    user_topic = input("Enter a topic to research: ")
    try:
        user_max = int(input("Enter max number of papers to summarize (default 5): "))
    except ValueError:
        user_max = 5

    run_autoscholar(user_topic, max_papers=user_max)
