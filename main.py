import json
import base64
from flask import Flask, jsonify, request
from Authentication import match_user_id_pic, OCR_pipline
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/predict_image', methods=['POST'])
def predict_image():
    try:
        # Check if images are present and valid
        if 'image1' not in request.files or 'image2' not in request.files:
            return jsonify({"status": 400, "msg": "Missing one or both images (image1, image2)"}), 400

        # Read images from form data and convert to NumPy arrays
        image1_file = request.files['image1']
        image1_data = np.fromstring(image1_file.read(), np.uint8)
        image1_array = cv2.imdecode(image1_data, cv2.IMREAD_COLOR)

        image2_file = request.files['image2']
        image2_data = np.fromstring(image2_file.read(), np.uint8)
        image2_array = cv2.imdecode(image2_data, cv2.IMREAD_COLOR)

        # Process images
        id_number = OCR_pipline(image1_array)
        is_valid = str(match_user_id_pic(image1_array, image2_array))

        # Return response
        return jsonify({
            "status": 200,
            "data": {
                "id_number": id_number,
                "is_valid": is_valid
            }
        })
    except Exception as e:
        # Handle errors during processing
        return jsonify({"status": 500, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)
