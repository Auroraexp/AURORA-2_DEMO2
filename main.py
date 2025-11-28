
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run")
def run(payload: dict):
    return {"result": "AURORA-2 demo response", "input": payload}
