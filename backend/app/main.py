from fastapi import FastAPI
from app.routes.videos import router as videos_router
from app.routes.shorts import router as shorts_router
from app.routes.competitor import router as competitor_router

app = FastAPI(title='Tubelens Clone')

app.include_router(videos_router, prefix="/api")
app.include_router(shorts_router, prefix="/api")
app.include_router(competitor_router, prefix="/api")
