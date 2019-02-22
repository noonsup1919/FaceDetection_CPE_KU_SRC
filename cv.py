import cv2
from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()


detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()
def show_webcam(mirror=False):
  cam = cv2.VideoCapture(0)
  while True:
    ret_val, img = cam.read()
    if mirror:
      img = cv2.flip(img, 1)
      custom_objects = detector.CustomObjects(person=True)
      #detections = detector.detectObjectsFromImage(input_type="array", input_image=img , output_image_path=os.path.join(execution_path , "image2custom.jpg"), minimum_percentage_probability=30)
      detected_image_array, detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects,input_type="array", input_image=img , output_type="array")
      
      cv2.imshow('my webcam', detected_image_array)
    
      if cv2.waitKey(1) == 27:
        break # กด esc เพื่อออก
cv2.destroyAllWindows()   
show_webcam(mirror=True)




