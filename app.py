import os

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

from carPricePrediction.pipeline.predict import PredictionPipeline

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.model = PredictionPipeline()

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    # os.system("python main.py")
    os.system("dvc repro")
    return "Training done successfully."

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.json
    result = clApp.model.predict(data)
    result = round(result)
    return jsonify({'predictedPrice': result})

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug=True)
