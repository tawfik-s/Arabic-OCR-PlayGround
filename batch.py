import easyocr
import cv2
import os

# Initialize the EasyOCR reader for Arabic and English
reader = easyocr.Reader(['ar', 'en'])  # This loads the OCR model

# Path to the input directory with images and output directory for text files
input_dir = 'input/'
output_dir = 'output/'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through all the files in the input directory
for image_name in os.listdir(input_dir):
    if image_name.endswith('.jpg') or image_name.endswith('.png'):
        img_path = os.path.join(input_dir, image_name)
        img = cv2.imread(img_path)

        # Perform OCR on the image
        result = reader.readtext(img, detail=0, paragraph=True)

        # Define output file name by replacing the image extension with .txt
        output_file = os.path.join(output_dir, os.path.splitext(image_name)[0] + '.txt')

        # Write the results to the individual text file
        with open(output_file, 'w', encoding='utf-8') as f_output:
            for line in result:
                f_output.write(line + '\n')

print("Text extraction completed and saved to individual text files.")
