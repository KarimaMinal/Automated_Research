class WriterAgent:
    def run(self, categories):
        print("[WriterAgent] Writing the report...")
        report = "# AutoScholar Report\n\n"
        for label, items in categories.items():
            report += f"## Category {label}\n\n"
            for item in items:
                report += f"### {item['title']}\n{item['summary']}\n\n"
        with open("data/output/report.md", "w") as f:
            f.write(report)
        return report