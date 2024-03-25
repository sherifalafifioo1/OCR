import json
from flask import Flask, render_template, jsonify, request
import Authentaction 
from Authentaction import match_user_id_pic,OCR_pipline 
import cv2

app = Flask(__name__)

@app.route('/predict_image', methods=['POST'])
def predict_image():
  # Check if both images are present
  if 'image1' not in request.files or 'image2' not in request.files:
    return jsonify({"status": 400, "msg": "Missing one or both images (image1, image2)"}), 400

  # Read images from form data
    image1 = request.files['image1']
    image2 = request.files['image2']
    
    ID= OCR_pipline(image1)
    valid=match_user_id_pic(image1,image2)
    
    

    return jsonify({"Id": Id,"Valid":valid})

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8000, threaded=True)
