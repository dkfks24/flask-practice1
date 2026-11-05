from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
import pandas as pd

app = Flask(__name__)
app.config["RESTX_JSON"] = {"ensure_ascii": False}

api = Api(
    app,
    version="1.0",
    title="Iris API",
    description="Iris 측정값 넷을 받아 품종을 돌려준다",
    doc="/api/docs",
    prefix="/api",
)
ns = api.namespace("iris", description="Iris 품종 예측")

@app.route("/")
def page():
    return app.send_static_file("index.html") # static/index.html 을 그대로

# 서버를 켤 때 한 번만 읽는다. 요청마다 다시 읽지 않는다.
model = joblib.load("iris_model.pkl")
COLUMNS = ["sepal length (cm)", "sepal width (cm)",
    "petal length (cm)", "petal width (cm)"]
NAMES = ["setosa", "versicolor", "virginica"]