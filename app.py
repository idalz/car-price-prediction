import os

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

from carPricePrediction.pipeline.predict import PredictionPipeline
from carPricePrediction.constants.html_content import *

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.model = PredictionPipeline()

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    content = index_dict
    return render_template('index.html', content=content)

@app.route("/predict", methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        data = request.json
        result = clApp.model.predict(data)
        result = round(result)
        return jsonify({'predictedPrice': result})
    else:
        content = predict_dict
        return render_template('predict.html', content=content)

@app.route("/about", methods=['GET'])
@cross_origin()
def about():
    content = about_dict
    return render_template('about.html', content=content)

#@app.route("/train", methods=['GET','POST'])
#def trainRoute():
#    # os.system("python main.py")
#    os.system("dvc repro")
#    return "Training done successfully."

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)
    #app.run(host='0.0.0.0', port=8080, debug=True)
