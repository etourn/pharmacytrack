from fastapi import FastAPI

app = FastAPI(title="PharmacyTrack API")

@app.get("/")
def read_root():
    return {"message": "Welcome to PharmacyTrack API"}
