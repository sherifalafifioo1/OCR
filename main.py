import json
from flask import Flask, render_template, jsonify, request
from Authentication import match_user_id_pic ,OCR_pipline  
import cv2

app = Flask(__name__)

@app.route('/predict_image', methods=['POST'])
def predict_image():
    # Check for images
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({"status": 400, "msg": "Missing one or both images (image1, image2)"}), 400

    # Read images
    try:
        image1 = request.files['image1'].read()
        image2 = request.files['image2'].read()
    except Exception as e:
        return jsonify({"status": 500, "msg": f"Error reading images: {str(e)}"}), 500

    # Process and validate (with error handling)
    try:
        ID = OCR_pipline(image1)
        valid = match_user_id_pic(image1, image2)
    except Exception as e:
        return jsonify({"status": 500, "msg": f"Error during processing: {str(e)}"}), 500

    # Return response (consider adding confidence scores, etc.)
    return jsonify({"Id": ID, "Valid": valid})

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8000, threaded=True)
