from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "🚀 OCR API - THÀNH CÔNG!", "status": "working"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/test")
def test():
    return {"test": "success"}
