from fastapi import FastAPI
app = FastAPI(title="Mock ERP")


@app.get("/health")
def health():
    return {"status": "ok"}
