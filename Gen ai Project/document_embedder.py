from pinecone import Pinecone, PodSpec
from sentence_transformers import SentenceTransformer
from config import settings

class DocumentEmbedder:
    def __init__(self):
        self.api_key = settings.PINECONE_API_KEY
        self.environment = settings.PINECONE_ENV
        self.index_name = settings.INDEX_NAME
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        self.pc = Pinecone(api_key=self.api_key)

        # Check if index exists
        existing_indexes = [index["name"] for index in self.pc.list_indexes()]
        if self.index_name not in existing_indexes:
            self.pc.create_index(
                name=self.index_name,
                dimension=384,
                spec=PodSpec(environment=self.environment)
            )

        self.index = self.pc.Index(self.index_name)

    def embed_texts(self, texts):
        return self.model.encode(texts).tolist()

    def upsert_documents(self, docs):
        vectors = [{"id": doc_id, "values": self.model.encode(text).tolist()} for doc_id, text in docs]
        self.index.upsert(vectors=vectors)

    def query(self, query_text, top_k=5):
        query_vec = self.model.encode(query_text).tolist()
        results = self.index.query(vector=query_vec, top_k=top_k, include_metadata=True)
        return results["matches"] if "matches" in results else []

document_embedder = DocumentEmbedder()
