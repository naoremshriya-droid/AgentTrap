
from fastapi import FastAPI

app = FastAPI(
    title="AgentTrap",
    description="AI Agent Security Gateway",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "AgentTrap",
        "status": "running",
        "message": "AI Security Gateway is online!"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
