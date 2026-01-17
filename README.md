
Image Name URL Generator (Python Flask)

Steps to run:
1. Extract zip
2. Open folder in VS Code
3. Install requirements:
   pip install -r requirements.txt
4. Run:
   python app.py
5. Upload image using Postman or browser form (POST):
   http://127.0.0.1:5000/upload
   key = image (file)

Response:
{
  "image_name": "cat.jpg",
  "image_url": "http://127.0.0.1:5000/uploads/cat.jpg"
}
