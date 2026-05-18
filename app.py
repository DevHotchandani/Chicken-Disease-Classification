from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from cnnClassifier.pipeline.prediction import PredictionPipeline

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homePage():
    return render_template("index.html")


@app.route("/train", methods=["GET"])
def training():
    os.system("python main.py")
    return "Training Done Successfully!"


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        image = request.files["image"]

        filename = secure_filename(image.filename)

        image_path = os.path.join("static/uploads", filename)

        image.save(image_path)

        obj = PredictionPipeline(filename=image_path)

        result = obj.predict()

        prediction = result[0]["image"]

        return render_template(
            "result.html",
            prediction=prediction
        )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)