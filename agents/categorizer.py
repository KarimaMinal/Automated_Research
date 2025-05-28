from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

class CategorizerAgent:
    def run(self, summaries):
        print("[CategorizerAgent] Categorizing summaries...")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode([s['summary'] for s in summaries])
        kmeans = KMeans(n_clusters=3, random_state=42)
        labels = kmeans.fit_predict(embeddings)

        clusters = {}
        for i, label in enumerate(labels):
            clusters.setdefault(label, []).append(summaries[i])
        return clusters
