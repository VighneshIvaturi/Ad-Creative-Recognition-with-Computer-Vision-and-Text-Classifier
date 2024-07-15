import streamlit as st
import cv2
import numpy as np
import pytesseract
import openai

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set the OpenAI API key
openai.api_key = 'sk-proj-Jdt8YH0nk1Hz6f7B'

# Function to detect ad creatives
def detect_ad_creative(image_file):
    try:
        # Read image file
        img_array = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        img_cv = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        
        # Convert to grayscale and apply edge detection for text overlay detection
        gray_img = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_img, 100, 200)
        
        # Use Tesseract to detect text
        text = pytesseract.image_to_string(gray_img)
        contains_text = len(text.strip()) > 0
        
        # Example: Placeholder for logo detection logic (to be replaced with an actual logo detection model)
        contains_logo = False  # Implement your logo detection logic here
        
        # Color detection for specific color schemes
        hsv_img = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        mask = cv2.inRange(hsv_img, lower_red, upper_red)
        red_pixels = cv2.countNonZero(mask)
        contains_specific_colors = red_pixels > 1000  # Example threshold for red pixels
        
        is_ad_creative = contains_text or contains_logo or contains_specific_colors
        
        return is_ad_creative, img_cv, contains_text, contains_logo, contains_specific_colors
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None, None, False, False, False

# Custom CSS
custom_css = """
<style>
body {
    font-family: 'Helvetica Neue', sans-serif;
    background-color: #f4f4f4;
    color: #333333;
}
.title {
    font-size: 48px;
    font-weight: 700;
    color: #2980B9;  /* Dark blue */
    text-align: center;
    margin-bottom: 30px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);  /* Light shadow for depth */
}
.description {
    font-size: 20px;
    color: #34495E;  /* Medium dark blue */
    margin-bottom: 20px;
    text-align: center;
}
.upload-section, .text-section {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}
.image-preview, .text-preview {
    margin-top: 20px;
    text-align: center;
}
.image-preview img {
    max-width: 100%;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.button-section {
    text-align: center;
    margin-top: 20px;
}
.button-section button {
    background-color: #3498DB;  /* Blue */
    color: #ffffff;
    font-weight: bold;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.button-section button:hover {
    background-color: #2980B9;  /* Darker blue */
}
.result {
    margin-top: 20px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: #E74C3C;  /* Red */
}
.footer {
    text-align: center;
    font-size: 12px;
    color: #888888;
    margin-top: 30px;
}
</style>
"""

# Streamlit app layout
def main():
    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    
    st.markdown('<div class="title">Ad Creative Detector & Text Classifier</div>', unsafe_allow_html=True)
    
    # Image Upload Section
    st.markdown('<div class="description">Upload one or more images to detect ad creatives:</div>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader("Upload Images...", type=["jpg", "png"], accept_multiple_files=True)
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            st.markdown('<hr>', unsafe_allow_html=True)
            st.markdown('<div class="upload-section">', unsafe_allow_html=True)
            
            # Display uploaded image and processed image
            col1, col2 = st.columns([1, 1])
            with col1:
                st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
            with col2:
                if st.button(f'Classify Image {uploaded_files.index(uploaded_file) + 1}'):
                    with st.spinner('Detecting ad creative...'):
                        is_ad_creative, img_cv, contains_text, contains_logo, contains_specific_colors = detect_ad_creative(uploaded_file)
                        if is_ad_creative is not None:
                            st.markdown('<div class="result">', unsafe_allow_html=True)
                            st.success("Ad Creative Detected!" if is_ad_creative else "Not an Ad Creative")
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            # Display detected elements
                            st.markdown('<div class="result">', unsafe_allow_html=True)
                            st.write(f"Contains Text: {'Yes' if contains_text else 'No'}")
                            st.write(f"Contains Logo: {'Yes' if contains_logo else 'No'}")
                            st.write(f"Contains Specific Colors: {'Yes' if contains_specific_colors else 'No'}")
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            # Display processed image next to uploaded image
                            st.markdown('<div class="image-preview">', unsafe_allow_html=True)
                            st.image(img_cv, caption='Processed Image', use_column_width=True)
                            st.markdown('</div>', unsafe_allow_html=True)
                        else:
                            st.warning("Unable to detect ad creative.")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Text Classification Section
    st.markdown('<div class="description">Enter text to classify:</div>', unsafe_allow_html=True)
    user_input = st.text_area("Enter text to classify:")
    
    if st.button("Classify Text"):
        if user_input:
            content = f"""Classify the text into one of the classes.
            Classes: [`AD Creative`, `Not AD Creative`]
            Text: {user_input}
            Class: """

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=0.6,
                messages=[
                    {"role": "user", "content": content},
                ]
            )

            result = response['choices'][0]['message']['content']
            st.write("Classification Result:", result)
        else:
            st.write("Please enter some text to classify.")

if __name__ == '__main__':
    main()
