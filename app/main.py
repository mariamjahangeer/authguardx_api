from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AuthGuardX API is up and running!"}
