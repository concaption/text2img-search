from fastapi import FastAPI
from multimodal_search import MultiModalSearch
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# To handle CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    text: str

@app.post("/search/")
async def search(query: Query):
    if not query.text:
        return JSONResponse(content={"message": "Query should not be empty"}, status_code=400)
    
    multimodal_search = MultiModalSearch()
    results = multimodal_search.search(query.text)
    
    # Convert results to a JSON-serializable format, if necessary
    results_json = [{"score": round(result.score*100, 2), "content": result.content} for result in results]
    
    return {"results": results_json}
