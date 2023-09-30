# Multimodal Search with Haystack: A Step-By-Step Guide

## Introduction

In today's world, data is not limited to text. We have a plethora of multimedia content such as images, audio, and video. Therefore, having a search mechanism that can look into multiple types of media is more useful than ever. In this tutorial, we will focus on creating a multimodal search capability using Haystack's `MultiModalRetriever`. We will be using Python for this tutorial.

## Technology Stack

- Python: The programming language used for this project.
- Haystack: An open-source framework for building search systems.
- Sentence Transformers: For using the CLIP-ViT-B-32 model to get embeddings.

## Step 1: Setup

Firstly, you'll need to install the Haystack library if you haven't already:

\`\`\`bash
pip install farm-haystack
\`\`\`

## Step 2: Import Necessary Modules

```python
import os
from haystack import Document
from haystack import Pipeline
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes.retriever.multimodal import MultiModalRetriever
```

## Step 3: Create the MultiModalSearch Class

Here is the complete code with detailed comments.

```python
class MultiModalSearch:
    def __init__(self):
        self.document_store = InMemoryDocumentStore(embedding_dim = 512)
        doc_dir = "./data"
        images = [
            Document(content=f"./{doc_dir}/{filename}", content_type="image", meta={"name": filename})
            for filename in os.listdir(doc_dir)
            if filename.endswith(".jpg")
        ]
        self.document_store.write_documents(images)
        self.retriever = MultiModalRetriever(
            query_embedding_model="sentence-transformers/clip-ViT-B-32",
            query_type= "text",
            document_embedding_models={
                "image": "sentence-transformers/clip-ViT-B-32",
            },
            document_store=self.document_store,
        )
        self.document_store.update_embeddings(self.retriever)
        self.pipeline = Pipeline()
        self.pipeline.add_node(component=self.retriever, name="Retriever", inputs=["Query"])
    def search(self, query):
        prediction = self.pipeline.run(query=query, params={"Retriever": {"top_k": 3}})
        return sorted(prediction["documents"], key=lambda x: x.score, reverse=True)
```

## Step 4: Use Cases

1. **E-commerce Platforms**: When users want to find products similar to a reference image or description.
2. **Media Libraries**: To search for images or videos based on textual queries or vice versa.
3. **Research**: For tasks like object identification in images based on textual descriptions.

## Conclusion

Multimodal search is becoming increasingly important as we deal with varied types of data. With frameworks like Haystack, building such capabilities has become more straightforward than ever.
