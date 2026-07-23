from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sentiment_engine import analyze_arabic_sentiment


# ============================================================
# APP
# ============================================================

app = FastAPI(
    title="Arabic Sentiment Analysis API",
    description="Arabic NLP sentiment analysis engine",
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# REQUEST MODEL
# ============================================================

class AnalyzeRequest(BaseModel):
    text: str


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():

    return {
        "status": "online",
        "message": "Arabic Sentiment Analysis API is running",
    }


# ============================================================
# ANALYZE
# ============================================================

@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    result = analyze_arabic_sentiment(
        request.text
    )

    return result