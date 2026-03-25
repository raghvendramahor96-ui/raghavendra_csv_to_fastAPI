from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("students_complete.csv")

@app.get("/")
def home():
    return {"message": "Student API is running 🚀"}

@app.get("/students")
def get_all_students():
    return df.fillna("").to_dict(orient="records")

@app.get("/students/{limit}")
def get_limited_students(limit: int):
    return df.head(limit).fillna("").to_dict(orient="records")