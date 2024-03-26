import json
import base64
from flask import Flask, jsonify, request
from Authentication import match_user_id_pic, OCR_pipline
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/predict_image', methods=['POST'])
def predict_image():
    # Check if images are present and valid
    if 'image1' not in request.json or 'image2' not in request.json:
        return jsonify({"status": 400, "msg": "Missing one or both images (image1, image2)"}), 400

    try:
        # Retrieve and decode base64-encoded images
        image1_base64 = request.json['image1']
        image2_base64 = request.json['image2']
        image1_data = base64.b64decode(image1_base64)
        image2_data = base64.b64decode(image2_base64)

        # Convert image data to numpy arrays
        image1_array = np.frombuffer(image1_data, np.uint8)
        image2_array = np.frombuffer(image2_data, np.uint8)

        # Read images using OpenCV
        image1 = cv2.imdecode(image1_array, cv2.IMREAD_COLOR)
        image2 = cv2.imdecode(image2_array, cv2.IMREAD_COLOR)

        # Process images
        id_number = OCR_pipline(image1)
        is_valid = match_user_id_pic(image1, image2)

        # Return response
        return jsonify({
            "status": 200,
            "data": {
                "id_number": id_number,
                "is_valid": str(is_valid)
            }
        })
    except Exception as e:
        # Handle errors during processing
        return jsonify({"status": 500, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)
