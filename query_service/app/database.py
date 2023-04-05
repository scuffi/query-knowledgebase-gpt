import os
import uuid
import pinecone

class Database:
    def __init__(self) -> None:
        pinecone.init(
            api_key=os.environ["PINECONE_API_KEY"],
            environment=os.environ["PINECONE_ENVIRONMENT"],
        )
        self.index = pinecone.Index("query-example")

    def upload(self, sentences: list[tuple]):
        tuplified = [(str(uuid.uuid4()), sentence[1], {"value": sentence[0]}) for sentence in sentences]
        self.index.upsert(tuplified)

    def query(self, vector):
        response = self.index.query(
            top_k= 10,
            vector=vector,
            include_values=False,
            include_metadata=True,
        )

        return [obj["metadata"]["value"] for obj in response.get("matches")]
    
    def clear(self):
        self.index.delete(delete_all=True)
