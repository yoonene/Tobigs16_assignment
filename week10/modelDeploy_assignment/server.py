from flask import request
from flask import Flask # flask : 웹 개발을 위한 파이썬의 마이크로 프레임워크 (간단하고 가벼움)
from flask_cors import CORS # 외부에서 접속해도 에러가 나지 않게 보안 설정 적용
from model import model
import json # JavaScript Object Notation - 데이터를 저장하거나 전송할 때 사용되는 경량의 DATA 포맷
            #                            - {"key: "value"} 형식
            #                            - 자바스크립트 객체의 형식을 기반으로 만들어졌지만 그냥 텍스트 형식일 뿐
            #                            - 특정 언어에 종속되지 않음
app = Flask(__name__)
CORS(app) # 외부에서 접속해도 에러가 나지 않게 보안 설정 적용

""" status check """
@app.route("/")
def index():
    result = {
        'message': 'Status is OK.'
    }
    return json.dumps(result)

""" ------------ """

""" model predict """
@app.route('/predict', methods=['POST']) # route : 외부 웹브라우져에서 웹서버로 접근 시 해당하는 주소를 입력하면 특정 함수를 실행시킴.
                                         # 엔드포인트 경로를 /predict으로 설정
                                         # 전달하려는 정보를 HTTP body에 포함하여 전달
def predict_model():

    print("Predict method Start..")
    params = request.get_json() # json 데이터를 파이썬 데이터 형식으로 변환해서 가져오기

    pred = model.predict(params['height'], params['weight']) # 받아온 키와 몸무게 정보로 모델이 bmi 예측

    result = {
        'message': 'Succefully Predicted',
        'result': pred
    } # JSON 형식

    print("Predict Finish ..")
    print(result)

    return json.dumps(result)    # flask response를 보내는 법
""" ------------- """


if __name__ == "__main__":
    app.run();
