import cv2
import pytesseract

# Load the invoice image
invoice_image_path = "path/to/your/invoice.jpg"
invoice_image = cv2.imread(invoice_image_path)

# Preprocess the image (you can adjust these steps based on your specific use case)
gray_image = cv2.cvtColor(invoice_image, cv2.COLOR_BGR2GRAY)
threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Use Tesseract to extract text from the preprocessed image
extracted_text = pytesseract.image_to_string(threshold_image)

# Print the extracted text
print("Extracted Text from Invoice:")
print(extracted_text)
