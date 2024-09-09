from typing import Union
from fastapi import FastAPI
import pickle
from fishregression import get_model_path

app = FastAPI()

# 무게 예측 함수
def run_prediction(length:float):
    with open("/home/hahahellooo/code/fishregression/note/model.pkl", "rb") as f:
        fish_model = pickle.load(f)
        prediction = fish_model.predict([[length ** 2, length]])
        return float(prediction[0])

@app.get("/")
def read_root():
    return {"Hello": "fish world"}


@app.get("/lr_api")
def lr_api(length: float):
    """
    물고기의 무게를 예측하는 함수

    Args:
        length(float): 물고기의 길이(cm)
    
    Returns:
        dict:
            weight(float): 물고기 무게(g)
            length(flozt): 물고기 길이(cm)
    """
 ### 예측해서 결과 return
    weight = run_prediction(length)
    return{
            "length":lenght
            "weight":weight
            }
