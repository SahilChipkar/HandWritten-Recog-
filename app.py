from flask import Flask, render_template, request
from PIL import Image
import io
import os
from datetime import datetime
from utilis import  processor,model
from main import infer_by_web
import logging
import warnings
warnings.filterwarnings("ignore", message=".*deprecated.*")
app = Flask(__name__)
# configure logging
log_dir = os.path.join(app.instance_path, 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_filename = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log")
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # get the uploaded image from the HTML form
        image_file1 = request.files['image']

        # read the uploaded image as bytes and convert it to an image
        image_bytes = image_file1.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # apply processor to the image
        pixel_values = processor(images=image, return_tensors="pt").pixel_values

        # generate text 
        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

        # save the uploaded image to a temporary directory
        tmp_dir = os.path.join(app.instance_path, 'tmp')
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        image_filename = os.path.join(tmp_dir, image_file1.filename)
        image.save(image_filename)

        # render the prediction result page with the generated text and image filename
        return render_template('predict.html', text=generated_text, image_filename=image_filename)
    
    except Exception as e:
        # Log the error
        logging.exception(e)

        # Render the error.html page with the error message
        return render_template('error.html', error=str(e))    

if __name__ == '__main__':
    app.run(debug=True)
