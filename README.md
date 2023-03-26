# HandWritten-Recog



This repository contains the code for a Flask web application that uses a pre-trained deep learning model to classify images. 

### Requirements
- Python 3.8 or higher
- Flask
- Tensorflow 
- Keras 

### Usage

1. Clone this repository to your local machine.
2. Install the required packages listed in the requirements.txt file.
3. Run the command `python app.py` to start the Flask application.
4. Open your web browser and navigate to `http://localhost:4555/`.
5. Upload an image and select a prediction option.
6. Click the `Upload` button to submit the form and see the result.

### Files

The following files are included in this repository:

- `app.py`: The main Flask application.
- `main.py`: The script containing the deep learning model.
- `templates/`: The folder containing the HTML templates used by the Flask application.
- `static/`: The folder containing the static files used by the Flask application.


##  Model Usage
### Training
To train the model, run the `python main.py --train` script his will train the model on the IAM dataset and save the trained model parameters in the data directory.





