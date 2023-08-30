from fastapi import FastAPI, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
import joblib 
import numpy as np
import os
from own.preprocess import Preprocess
import sklearn


col_data = joblib.load("./utils/col_meta.z")

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/predict")
async def test():
    return jsonable_encoder(col_data)


@app.post("/predict")
async def provide(data: dict):
    data_main = data["value"]
    output = main(data_main)
    return output


def predict_main(df):
    num_folds =  len(os.listdir("./RandomForest_result"))
    result_li = []
    for fold in range(num_folds):
        print(f"predicting for fold {fold} / {num_folds}")
        model = joblib.load(f"./RandomForest_result/{fold}_model.z")
        print(df.shape)
        result = model.predict(df)
        print(result)
        result_li.append(result)
    return np.mean(result_li)

def main(data):
    df = Preprocess(data)
    res = predict_main(df)
    print(res)
    return {"value": f"{np.float64(res).item():.3f}" if res >=0 else f"{np.float64(0).item()}"}


