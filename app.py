from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------- Direct image URLs ----------
@app.route('/cat')
def cat_image():
    return send_from_directory(UPLOAD_FOLDER, 'cat.jpg')

@app.route('/dog')
def dog_image():
    return send_from_directory(UPLOAD_FOLDER, 'dog.jpg')

@app.route('/table')
def table_image():
    return send_from_directory(UPLOAD_FOLDER, 'table.jpg')

# ---------- Optional: list all images ----------
@app.route('/images')
def list_images():
    images = os.listdir(UPLOAD_FOLDER)
    urls = {
        img: f"http://127.0.0.1:5000/uploads/{img}"
        for img in images
    }
    return jsonify(urls)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
