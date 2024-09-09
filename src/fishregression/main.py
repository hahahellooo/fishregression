from typing import Union
from fastapi import FastAPI
import pickle

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/lr_api")
def lr_api(length: float):
 ### 모델 불러오기
    with open("/home/hahahellooo/code/fishregression/note/model.pkl", "rb") as f:
        fish_model = pickle.load(f)

    prediction = fish_model.predict([[length]])

    return {
                "prediction": prediction,
                "length": length, 
                "weight": weight
            }

