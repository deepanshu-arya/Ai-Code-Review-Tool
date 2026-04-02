from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal, engine
from backend import models, schemas
from backend.ai_engine import review_code
from backend.utils import detect_language
from fastapi.middleware.cors import CORSMiddleware
import os 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/review", response_model=schemas.CodeResponse)
def review(request: schemas.CodeRequest, db: Session = Depends(get_db)):
    
    result = review_code(request.code)
    language = detect_language(request.code)

    review_entry = models.CodeReview(
        code=request.code,
        review=result["review"],
        score=result["score"],
        language=language
    )

    db.add(review_entry)
    db.commit()

    return {
        "review": result["review"],
        "score": result["score"],
        "improved_code": result["improved_code"],
        "language": language
    }


@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    return db.query(models.CodeReview).all()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
