from fastapi import FastAPI

app = FastAPI(
    title="Atlas API",
    description="AI-powered Creator Operating System",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "name": "Atlas API",
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }