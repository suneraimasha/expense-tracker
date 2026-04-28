from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student Expense Tracker API is running"}