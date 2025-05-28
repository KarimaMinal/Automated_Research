from tools.text_processing import summarize_text

class SummarizerAgent:
    def run(self, papers):
        print("[SummarizerAgent] Summarizing papers...")
        return [{"title": p['title'], "summary": summarize_text(p['summary'])} for p in papers]
