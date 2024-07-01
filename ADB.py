import uiautomator2 as u2

# Replace 'emulator-5574' with the name of your emulator
DEF_DEVICE = 'emulator-5574'  # Replace with your emulator's name
ATK_DEVICE = 'emulator-5584'
# ATK = u2.connect(DEF_DEVICE)
DEF = u2.connect(ATK_DEVICE)
# print(ATK.info)
# print(DEF.info)
screen_size = DEF.window_size()

# Dump the UI hierarchy
hierarchy = DEF.dump_hierarchy()

print(hierarchy)