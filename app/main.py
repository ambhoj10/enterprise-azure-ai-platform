from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Azure AI Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Enterprise Azure AI Platform"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
