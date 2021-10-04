from joblib import load
import numpy as np


model = load('./model/model_params/bmiRegressor') # 저장된 모델 호출
    
def predict(height: int, weight: int):    # 이용자의 키와 몸무게에 대한 정보를 입력으로 사용
    print("Model Start")
    result = model.predict([[height, weight]])    # 모델의 예측 결과
    print("Model Finish")
    return result.item() # result 딕셔너리의 key, value 쌍을 튜플로 리스트의 원소로 반환
