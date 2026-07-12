# Efficient Monkeypox Diagnosis Using Attention-Based MobileNetV2

## Project Overview
This project is a deep learning-based web application developed to detect Monkeypox from skin images. The application uses an Attention-Based MobileNetV2 model for image classification and a Flask web framework to provide an easy-to-use web interface. Users can upload a skin image, and the application predicts the corresponding disease class.

## Features
- Upload skin images for prediction
- Deep learning-based disease classification
- Simple and user-friendly web interface
- Fast and accurate prediction results
- Flask backend integrated with the trained model

## Technologies Used
- Python
- Flask
- TensorFlow
- Keras
- HTML
- CSS
- JavaScript

## Project Structure
```
 flask/project/
│   ├── static/
│   │   └── DB9 Team Document 1.pdf
│   │
│   └── templates/
│       ├── about.html
│       ├── contact.html
│       └── home.html
│
├── app.py
├── monkeypox_model.h5
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Singuvamsivamsi/Monkeypox
```

### 2. Move to the Project Directory
```bash
cd Monkeypox

```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Open in Browser
```
http://127.0.0.1:5000
```

## Dataset
The model was trained on a skin disease image dataset containing multiple classes, including Monkeypox and other similar skin conditions, to improve classification performance.

## Model
- Architecture: Attention-Based MobileNetV2
- Framework: TensorFlow / Keras
- Task: Multi-class skin disease classification


## Project  Documentation
The complete project documentation is available in **DB9 Team Document 1.pdf**.

## Note
The trained model file is not included in this repository if it exceeds GitHub's file size limit. The repository focuses on the web application and project implementation.

## Future Improvements
- Deploy the application to the cloud
- Improve model accuracy with more data
- Add support for additional skin diseases
- Develop a mobile-friendly interface

## Author

**Vamsy Singu**

- B.Tech – Computer Science and Engineering
- Python Developer 

---
⭐ If you found this project useful, consider giving it a star on GitHub.
