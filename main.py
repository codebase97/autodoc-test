from fastapi import FastAPI
from dotenv import load_dotenv

from app.routes import router as router
from app.routes_webhook import router as webhook_router
from app.routes_admin import router as admin_router
from app.routes_status import router as status_router  # ✅ Add this

load_dotenv()

app = FastAPI()

app.include_router(router)
app.include_router(webhook_router)
app.include_router(admin_router)
app.include_router(status_router)  # ✅ Include it here

