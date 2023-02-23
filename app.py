from flask import Flask, request, jsonify
import cv2
import numpy as np
from keras.models import load_model

# load the pre-trained deep learning model
model = load_model('detector.h5')
class_label = ['Bed', 'Chair', 'Sofa']

app = Flask(__name__)

# define the route for the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # check if the request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'no file uploaded'})
    
    # read the input image file from the request
    file = request.files['file']
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)

    # preprocess the input image for the model
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (128, 128))
    image = np.expand_dims(image, axis=0)

    # make a prediction using the model
    predictions = model.predict(image)
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_label[predicted_class_index]

    # return the prediction results as a JSON response
    return jsonify({'predictions': predicted_class_label})

if __name__ == '__main__':
    app.run(debug=True)