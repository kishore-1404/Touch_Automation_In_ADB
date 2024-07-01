import json


# Function to extract touch information

def extract_touch_info(data):
    touch_info = {}
    for entry in data:
        action_name = entry["name"]
        record_list = entry.get("recordList", [])
        if record_list:
            touches = []
            for i, record in enumerate(record_list):
                touch = {
                    "X": record["point"]["x"],
                    "Y": record["point"]["y"],
                    "Delay": record["delay"]
                }
                touches.append(touch)
                if i == len(record_list) - 1:  # For the last touch, set delay to 0
                    touch["Delay"] = 0
            touch_info[action_name] = touches
        else:
            print(f"Skipping entry {action_name} as recordList is empty")
    return touch_info

# Read JSON data from file
with open('script.txt', 'r') as file:
    json_data = file.read()

# Parse JSON data
data = json.loads(json_data)

# Extract touch information
touch_info = extract_touch_info(data)
print(touch_info)

# # Print touch information
# for action, touches in touch_info.items():
#     print(f"For {action}:")
#     for touch in touches:
#         print(f"X: {touch['X']}, Y: {touch['Y']}, Delay: {touch['Delay']}")
#     print()
