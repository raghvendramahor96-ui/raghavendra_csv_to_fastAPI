from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

print("Current Directory:", os.getcwd())
print("Files:", os.listdir())

df = pd.read_csv(r"C:\Users\Dell\Downloads\students_complete.csv")
@app.get("/")
def home():
    return {"message": "API running 🚀"}

@app.get("/students")
def get_students():
    return df.to_dict(orient="records")