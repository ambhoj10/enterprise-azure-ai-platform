from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="Enterprise Azure AI Platform",
    description="Enterprise Azure AI Platform built with FastAPI, Azure OpenAI, Azure AI Search, Azure Blob Storage, and Azure Observability.",
    version="1.0.0"
)

# Register API routes
app.include_router(router)


@app.get("/")
def root():
    return {
        "platform": "Enterprise Azure AI Platform",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "services": {
            "azure_openai": "configured",
            "azure_ai_search": "configured",
            "blob_storage": "configured"
        }
    }
