from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd

app = FastAPI()

df = pd.read_csv("students_complete.csv")

# Serve UI
@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# API - all students
@app.get("/students")
def get_all_students():
    return df.fillna("").to_dict(orient="records")

# API - limited students
@app.get("/students/{limit}")
def get_limited_students(limit: int):
    return df.head(limit).fillna("").to_dict(orient="records")