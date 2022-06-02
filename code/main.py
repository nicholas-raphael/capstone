"""Sample API for capstone project"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    """Root endpoint"""
    return {"Hello": "World"}
