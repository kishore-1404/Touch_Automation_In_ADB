import uiautomator2 as u2
import time
from PIL import Image
import easyocr
import numpy as np
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Users\omkis\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
reader = easyocr.Reader(['en'],gpu=True)

# Connect to the Android device
device = u2.connect('emulator-5574')

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
# Function to perform clicks with delays
def perform_clicks(touches):
    for touch in touches:
        x, y, delay = touch["X"], touch["Y"], touch["Delay"]
        device.click(x, y)  # Click at the specified coordinates
        time.sleep(delay / 1000)  # Convert delay from milliseconds to seconds

# Define the touches for each action
actions = {'Attack': [{'X': 1333, 'Y': 811, 'Delay': 0}], 'Move_Defend': [{'X': 1571, 'Y': 991, 'Delay': 1650}, {'X': 394, 'Y': 400, 'Delay': 1416}, {'X': 958, 'Y': 514, 'Delay': 1467}, {'X': 1093, 'Y': 604, 'Delay': 1483}, {'X': 1129, 'Y': 423, 'Delay': 4250}, {'X': 1149, 'Y': 858, 'Delay': 0}], 'MapWindow': [{'X': 8, 'Y': 91, 'Delay': 414}, {'X': 8, 'Y': 89, 'Delay': 354}, {'X': 8, 'Y': 89, 'Delay': 333}, {'X': 8, 'Y': 88, 'Delay': 333}, {'X': 10, 'Y': 88, 'Delay': 316}, {'X': 10, 'Y': 88, 'Delay': 0}]}
#{'X': 1102, 'Y': 858, 'Delay': 1618}, {'X': 1046, 'Y': 855, 'Delay': 1050}, {'X': 988, 'Y': 860, 'Delay': 1334}, {'X': 925, 'Y': 858, 'Delay': 984}, {'X': 872, 'Y': 856, 'Delay': 1316}, {'X': 814, 'Y': 858, 'Delay': 867}, {'X': 752, 'Y': 858, 'Delay': 1333}, {'X': 697, 'Y': 856, 'Delay': 1350}, {'X': 643, 'Y': 859, 'Delay': 917}, {'X': 583, 'Y': 859, 'Delay': 0}
# Function to select and perform an action
def perform_action(action_name):
    if action_name in actions:
        touches = actions[action_name]
        perform_clicks(touches)
        print(f"Performed action: {action_name}")
    else:
        print(f"Action '{action_name}' not found.")

# Example usage: Perform the "Move_Defend" action
perform_action("MapWindow")
perform_action("Move_Defend")
