from tools.arxiv_api import search_arxiv

class ResearchAgent:
    def run(self, topic, max_results=5):
        print("[ResearchAgent] Searching for papers...")
        return search_arxiv(topic, max_results)
