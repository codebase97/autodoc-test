from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "ok", "message": "Webhook is live!"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

