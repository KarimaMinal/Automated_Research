import arxiv

def search_arxiv(query, max_results=5):
    search = arxiv.Search(query=query, max_results=max_results)
    results = []
    for result in search.results():
        results.append({"title": result.title, "summary": result.summary})
    return results
