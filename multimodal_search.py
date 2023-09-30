"""
This file contains the MultiModalSearch class. This class is designed to perform multimodal (text and image) search.
"""
import os

from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes.retriever.multimodal import MultiModalRetriever
from haystack import Document
from haystack import Pipeline

# The MultiModalSearch class is designed to perform multimodal (text and image) search.
# It uses Haystack's InMemoryDocumentStore and MultiModalRetriever for this purpose.
class MultiModalSearch:
    """
    Class to perform multimodal (text and image) search.

    params:
        None

    methods:
        search(query): Search for documents using the query.
    """
    # Initialization
    def __init__(self):
        # Create an InMemoryDocumentStore with an embedding dimension of 512.
        self.document_store = InMemoryDocumentStore(embedding_dim = 512)

        # Directory where document (image) files are stored
        doc_dir = "./data"

        # Read all .jpg image files from the directory and create Document objects for them
        images = [
            Document(content=f"./{doc_dir}/{filename}", content_type="image", meta={"name": filename})
            for filename in os.listdir(doc_dir)
            if filename.endswith(".jpg")
        ]

        # Write these Document objects to the document_store
        self.document_store.write_documents(images)

        self.document_store.progress_bar = True
        # Create a MultiModalRetriever. The retriever is configured to use the CLIP-ViT-B-32 model for both queries and documents.
        self.retriever = MultiModalRetriever(
            query_embedding_model="sentence-transformers/clip-ViT-B-32",
            query_type= "text",
            document_embedding_models={
                "image": "sentence-transformers/clip-ViT-B-32",
            },
            document_store=self.document_store,
        )

        # Update embeddings in the document_store
        self.document_store.update_embeddings(self.retriever)

        # Create a pipeline and add the retriever to it
        self.pipeline = Pipeline()
        self.pipeline.add_node(component=self.retriever, name="Retriever", inputs=["Query"])

    # Function to perform search
    def search(self, query):
        """
        Search for documents using the query.
        """
        # Run the query through the pipeline and get the top 3 results
        prediction = self.pipeline.run(query=query, params={"Retriever": {"top_k": 3}})
        # Sort the results by score in descending order and return
        return sorted(prediction["documents"], key=lambda x: x.score, reverse=True)
