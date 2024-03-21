from imageai.Detection import ObjectDetection
# from time import time
import os

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolov3.pt")
detector.loadModel()

def detect(image_name):
    return detector.detectObjectsFromImage(input_image=image_name, output_image_path="imagenew.jpg", minimum_percentage_probability=30)

def saver(name, org):  
  #Getting image path
  # name = input("please input image name : ")
  BTU = 0
  p = 0
  # org = int(input("Please input the person BTU : "))
  #getting date and time
  # current_time = time() / 60 / 60 % 24

  



  #if current_time > 18 or current_time < 6:
  folder_path = os.getcwd()
  file_path = os.path.join(folder_path,'image',name)
  
  detected = detect(file_path)

  for i in detected:
    if i['name'] in ['person']:
      p = p + 1

  BTU = p*org
  return BTU



# saver()
        
