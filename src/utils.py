from nltk.tokenize import sent_tokenize
from collections import Counter
import re

def summarize_text(text, top_n=2):
    try:
        sentences = sent_tokenize(text)
        words = re.findall(r'\w+', text.lower())
        freq = Counter(words)
        ranked = sorted(sentences, key=lambda s: sum(freq[w] for w in re.findall(r'\w+', s.lower())), reverse=True)
        return ' '.join(ranked[:top_n])
    except Exception:
        return text[:500]  # fallback
