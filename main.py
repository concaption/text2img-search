# !/.venv/bin/python
"""
Main file for the FastAPI server
"""

from fastapi import FastAPI
from multimodal_search import MultiModalSearch
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Multimodal Search API", description="API to search for images and videos using text", version="1.0.0", )

# To handle CORS
app.add_middleware( CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], )

class Query(BaseModel):
    """
    Query model
    """
    text: str

@app.post("/search/")
async def search(query: Query):
    """
    Search for a query and return the results
    """
    if not query.text:
        return JSONResponse(content={"message": "Query should not be empty"}, status_code=400)

    multimodal_search = MultiModalSearch()
    results = multimodal_search.search(query.text)

    # Convert results to a JSON-serializable format, if necessary
    results_json = [{"score": round(result.score*100, 2), "content": result.content} for result in results]

    return {"results": results_json}


@app.get("/")
async def root():
    """
    Root endpoint
    """
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
