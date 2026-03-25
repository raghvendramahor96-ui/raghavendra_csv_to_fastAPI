from fastapi import FastAPI
#import pandas as pd

app = FastAPI()

#df = pd.read_csv("data.csv")

@app.get("/")
def home():
    return {"message": "API working"}

@app.get("/data")
def get_data():
    return {"message":"Hello now is working"}