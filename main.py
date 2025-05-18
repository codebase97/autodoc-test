from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "ok", "message": "Webhook is live!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

