import pysbd
from sentence_transformers import SentenceTransformer

class Vectoriser:
    
    def __init__(self) -> None:
        self._embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
    def sentencise_chunk(self, text: list[str]):
        seg = pysbd.Segmenter(language="en", clean=False)
        sentences = seg.segment(text)
        return sentences
        
        
    def vectorise_sentences(self, sentences: list[str]):
        embeddings = self._embedding_model.encode(sentences)
        return list(zip(sentences, embeddings.tolist()))