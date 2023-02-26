import json
import cv2
import torch
import numpy as np
from fastapi import FastAPI, File
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

@app.get("/")
def index():
    return {"message": "Hello YOLO World"}


@app.post("/predict")
def predict(file: bytes = File(...)):
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    results = model(img)
    results_json = json.loads(results.pandas().xyxy[0].to_json(orient="records"))
    return {"result" : results_json}

