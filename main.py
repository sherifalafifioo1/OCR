#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
from flask import Flask, render_template, jsonify, request
import model1 
import cv2
app = Flask(__name__)

@app.route('/predict_image', methods=['POST'])
def predict_image():
    if 'Password' not in request.json:
        return jsonify({"status": 400, "msg": "Missing 'Password' in request"})

    password = request.json['Password']
    
    print(password)
    

    return jsonify({"id": "123", "valid": "well done"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)


# In[ ]:




