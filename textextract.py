from PIL import Image
import easyocr
import numpy as np

def extract_text_from_screen(rect_coords):
    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\screenshot2.png"

    screenshot = Image.open(image_path)

    x, y, width, height = rect_coords["x"], rect_coords["y"], rect_coords["width"], rect_coords["height"]
    region = screenshot.crop((x, y, x + width, y + height))

    # Convert the cropped image to a numpy array
    region_np = np.array(region)

    reader = easyocr.Reader(['en'],gpu=True)
    result = reader.readtext(region_np)

    extracted_text = ""
    for detection in result:
        extracted_text += detection[1] + " "

    return extracted_text.strip()

if __name__ == "__main__":
    rect_coords = {"x":1479,"y":565,"width":190,"height":37}
    extracted_text = extract_text_from_screen(rect_coords)
    print("Extracted Text:", extracted_text)
