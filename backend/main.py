from fastapi import FastAPI
from backend.routes import auth, tasks
from backend.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Tasks API",
    description="API for managing tasks and authentication",
    version="1.0.0",
    docs_url="/docs",        # Swagger UI
    redoc_url="/redoc",      # ReDoc
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://taskstp.vercel.app/"],  # مؤقت (للتجربة فقط)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/", tags=["Root"])
def root():
    return {"message": "API is running"}