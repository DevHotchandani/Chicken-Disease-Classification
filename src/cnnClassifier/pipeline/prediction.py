import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = load_model("artifacts/training/model.h5", compile=False)

        test_image = image.load_img(
            self.filename,
            target_size=(224, 224)
        )

        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0

        result = model.predict(test_image)

        predicted_class = np.argmax(result, axis=1)[0]

        if predicted_class == 0:
            prediction = "Coccidiosis"
        else:
            prediction = "Healthy"

        return [{"image": prediction}]