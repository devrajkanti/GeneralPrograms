import os
arr = os.listdir("D:\\Dashcam\\Logs\DontDelete_24022020\\FFC_CalibrationTest\\Six\\videos")
print(arr)

for root, dirs, files in os.walk("D:\\Dashcam\\Logs\DontDelete_24022020\\FFC_CalibrationTest\\Six\\videos", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))