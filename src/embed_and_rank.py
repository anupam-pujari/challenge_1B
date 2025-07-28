from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

model = SentenceTransformer('all-MiniLM-L6-v2')  # < 100MB, fast, CPU-friendly

def rank_sections(sections, persona, job, top_n=5):
    query = f"{persona}. Task: {job}"
    query_embedding = model.encode(query)
    ranked = []
    for section in sections:
        combined_text = section["title"] + ". " + section["content"]
        section_embedding = model.encode(combined_text)
        score = cosine_similarity([query_embedding], [section_embedding])[0][0]
        ranked.append({"score": score, **section})
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked[:top_n]
