# Ad Creative Detector & Text Classifier

This project utilizes Computer Vision and Generative AI to detect ad creatives in images and classify text. The solution leverages OpenCV, Tesseract OCR, OpenAI's GPT-3.5, and Streamlit for the web interface. This README file will guide you through the setup and usage of the application.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License](#license)

## Features
- **Ad Creative Detection**: Detects text, logos, and specific color schemes in images to identify ad creatives.
- **Text Classification**: Classifies user-input text as 'AD Creative' or 'Not AD Creative'.
- **User-Friendly Interface**: Interactive web application built with Streamlit.
- **Customizable**: Easy to extend and customize for additional detection features.

## Installation

### Prerequisites
- Python 3.7 or higher
- Tesseract OCR
- OpenAI API Key

### Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/ad-creative-detector.git
    cd ad-creative-detector
    ```

2. **Install required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Tesseract OCR**:
    - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
    - Note the installation path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`).

4. **Set up OpenAI API Key**:
    - Sign up for an API key from [OpenAI](https://openai.com/).
    - Replace `'your_openai_api_key'` in the code with your actual OpenAI API key.

## Usage

1. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with the application**:
    - Upload images to detect ad creatives.
    - Enter text to classify it as 'AD Creative' or 'Not AD Creative'.

## How It Works

### Image Processing with OpenCV
- The uploaded image is processed to detect text, logos, and specific color schemes.
- Edge detection and color masking are applied to identify potential ad creatives.

### Text Detection with Tesseract OCR
- Tesseract OCR is used to extract text from the uploaded images.
- The presence of text helps determine if the image is an ad creative.

### Generative AI with OpenAI's GPT-3.5
- User-input text is classified using OpenAI's GPT-3.5 model.
- The text is categorized as either 'AD Creative' or 'Not AD Creative' based on context.

### Streamlit Interface
- A user-friendly web interface allows users to upload images and input text for classification.
- Custom CSS is applied for a polished and professional look.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to contribute to this project by submitting issues or pull requests. If you have any questions, please reach out to me at saivighneshivaturi.97@gmail.com.
