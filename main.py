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
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({"status": 400, "msg": "Missing one or both images (image1, image2)"}), 400

    try:
        # Read images from form data
        image1_file = request.files['image1']
        image2_file = request.files['image2']

        # Process images (requires additional logic to convert to NumPy arrays)
        image1_data = image1_file.read()  # You'll need to convert this to a NumPy array
        image2_data = image2_file.read()  # You'll need to convert this to a NumPy array


        # Process images
        id_number = OCR_pipline(image1_data)
        is_valid =str( match_user_id_pic(image1_data, image2_data))

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
