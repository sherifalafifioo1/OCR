import json  
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request
from Authentication import match_user_id_pic, OCR_pipline
import cv2

app = Flask(__name__)

@app.route('/predict_image', methods=['POST'])
def predict_image():
  # Check if images are present and valid
  if 'image1' not in request.files or 'image2' not in request.files:
    return jsonify({"status": 400, "msg": "Missing one or both images (image1, image2)"}), 400

  try:
    # Read images with filename sanitization
    image1 = request.files['image1']
    image2 = request.files['image2']
    image1_filename = secure_filename(image1.filename)
    image2_filename = secure_filename(image2.filename)

    # Process images
    id_number = OCR_pipline(image1.read())
    is_valid = match_user_id_pic(image1.read(), image2.read())

    # Return response with sanitized filenames
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
