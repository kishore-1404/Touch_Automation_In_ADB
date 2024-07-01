from PIL import Image
import easyocr
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\omkis\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
reader = easyocr.Reader(['en'],gpu=True)
def extract_text_from_screen(rect_coords,image_path,time=0):
    screenshot = Image.open(image_path)

    x, y, width, height = rect_coords["x"], rect_coords["y"], rect_coords["width"], rect_coords["height"]
    region = screenshot.crop((x, y, x + width, y + height))
    # region.show()

    # Convert the cropped image to a numpy array
    region_np = np.array(region)

    if time==1:
        _text = pytesseract.image_to_string(region_np, config='--psm 13')
        return _text.strip()
    result = reader.readtext(region_np,decoder='beamsearch',allowlist='0123456789mMkKGThs.',paragraph = False,width_ths=50)
    extracted_text = ""
    for detection in result:
        extracted_text += detection[1] + " "

    return extracted_text.strip()

if __name__ == "__main__":

    rects = {
        'MainCityTroops':{"x":718,"y":369,"width":182,"height":57},
        'City1Troops':{"x":719,"y":465,"width":179,"height":57},
        'City2Troops':{"x":719,"y":565,"width":184,"height":57},
        'City3Troops':{"x":722,"y":657,"width":127,"height":57},
        "step0Troops": {"x": 1071, "y": 718, "width": 169, "height": 52},
        "step0Time": {"x": 1090, "y": 776, "width": 120, "height": 32},
        "step1Troops": {"x": 1013, "y": 718, "width": 169, "height": 52},
        "step1Time": {"x": 1032, "y": 776, "width": 120, "height": 32},
        "step2Troops": {"x": 955, "y": 718, "width": 169, "height": 52},
        "step2Time": {"x": 974, "y": 776, "width": 120, "height": 32},
        "step3Troops": {"x": 897, "y": 718, "width": 169, "height": 52},
        "step3Time": {"x": 916, "y": 776, "width": 120, "height": 32},
        "step4Troops": {"x": 839, "y": 718, "width": 169, "height": 52},
        "step4Time": {"x": 858, "y": 776, "width": 120, "height": 32},
        "step5Troops": {"x": 781, "y": 718, "width": 169, "height": 52},
        "step5Time": {"x": 800, "y": 776, "width": 120, "height": 32},
        "step6Troops": {"x": 723, "y": 718, "width": 169, "height": 52},
        "step6Time": {"x": 742, "y": 776, "width": 120, "height": 32},
        "step7Troops": {"x": 665, "y": 718, "width": 169, "height": 52},
        "step7Time": {"x": 684, "y": 776, "width": 120, "height": 32},
        "step8Troops": {"x": 607, "y": 718, "width": 169, "height": 52},
        "step8Time": {"x": 626, "y": 776, "width": 120, "height": 32},
        "step9Troops": {"x": 549, "y": 718, "width": 169, "height": 52},
        "step9Time": {"x": 568, "y": 776, "width": 120, "height": 32},
        "step10Troops": {"x": 491, "y": 718, "width": 169, "height": 52},
        "step10Time": {"x": 510, "y": 776, "width": 120, "height": 32}

    }
    
    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\t2.png"
    rect_coords = rects['MainCityTroops']
    extracted_text = extract_text_from_screen(rect_coords,image_path)
    print("Extracted Text:", extracted_text)
    rect_coords = rects['City1Troops']
    extracted_text = extract_text_from_screen(rect_coords,image_path)
    print("Extracted Text:", extracted_text)
    rect_coords = rects['City2Troops']
    extracted_text = extract_text_from_screen(rect_coords,image_path)
    print("Extracted Text:", extracted_text)
    rect_coords = rects['City3Troops']
    extracted_text = extract_text_from_screen(rect_coords,image_path)
    print("Extracted Text:", extracted_text)
    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\0.png"
    rect_coords = rects['step10Time']
    extracted_text = extract_text_from_screen(rect_coords,image_path,1)
    print("Extracted Text:", extracted_text)
    rect_coords = rects['step10Troops']
    extracted_text = extract_text_from_screen(rect_coords,image_path)
    print("Extracted Text:", extracted_text)
    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\10.png"
    rect_coords = rects['step0Time']
    extracted_text = extract_text_from_screen(rect_coords,image_path,1)
    print("Extracted Text:", extracted_text)
    rect_coords = rects['step0Troops']
    extracted_text = extract_text_from_screen(rect_coords,image_path)
    print("Extracted Text:", extracted_text)
    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\9.png"
    rect_coords = rects['step1Time']
    extracted_text = extract_text_from_screen(rect_coords,image_path,1)
    print("Extracted Text:", extracted_text)
    rect_coords = rects['step1Troops']
    extracted_text = extract_text_from_screen(rect_coords,image_path)
    print("Extracted Text:", extracted_text)
    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\8.png"
    rect_coords = rects['step2Time']
    extracted_text = extract_text_from_screen(rect_coords, image_path, 1)
    print("Extracted Text for step 2 Time:", extracted_text)

    rect_coords = rects['step2Troops']
    extracted_text = extract_text_from_screen(rect_coords, image_path)
    print("Extracted Text for step 2 Troops:", extracted_text)

    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\7.png"
    rect_coords = rects['step3Time']
    extracted_text = extract_text_from_screen(rect_coords, image_path, 1)
    print("Extracted Text for step 3 Time:", extracted_text)

    rect_coords = rects['step3Troops']
    extracted_text = extract_text_from_screen(rect_coords, image_path)
    print("Extracted Text for step 3 Troops:", extracted_text)
    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\6.png"
    rect_coords = rects['step4Time']
    extracted_text = extract_text_from_screen(rect_coords, image_path, 1)
    print("Extracted Text for step 4 Time:", extracted_text)

    rect_coords = rects['step4Troops']
    extracted_text = extract_text_from_screen(rect_coords, image_path)
    print("Extracted Text for step 4 Troops:", extracted_text)

    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\5.png"
    rect_coords = rects['step5Time']
    extracted_text = extract_text_from_screen(rect_coords, image_path, 1)
    print("Extracted Text for step 5 Time:", extracted_text)

    rect_coords = rects['step5Troops']
    extracted_text = extract_text_from_screen(rect_coords, image_path)
    print("Extracted Text for step 5 Troops:", extracted_text)
    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\4.png"
    rect_coords = rects['step6Time']
    extracted_text = extract_text_from_screen(rect_coords, image_path, 1)
    print("Extracted Text for step 6 Time:", extracted_text)

    rect_coords = rects['step6Troops']
    extracted_text = extract_text_from_screen(rect_coords, image_path)
    print("Extracted Text for step 6 Troops:", extracted_text)

    image_path = r"C:\Users\omkis\Downloads\MillionLords\Trading\adb\3.png"
    rect_coords = rects['step7Time']
    extracted_text = extract_text_from_screen(rect_coords, image_path, 1)
    print("Extracted Text for step 7 Time:", extracted_text)

    rect_coords = rects['step7Troops']
    extracted_text = extract_text_from_screen(rect_coords, image_path)
    print("Extracted Text for step 7 Troops:", extracted_text)

    


