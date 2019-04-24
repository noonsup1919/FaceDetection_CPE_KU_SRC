from imageai.Detection import VideoObjectDetection
from imageai.Detection import ObjectDetection

import numpy as np
import cv2
import os


from dialog import Ui_Dialog
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import Qt, QThread, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication


class StartWindows(QMainWindow):
    def __init__(self,camera=None, parent=None):
        
        super(StartWindows, self).__init__(parent=parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.detector = ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.execution_path = os.getcwd()
        self.detector.setModelPath( os.path.join(self.execution_path , "yolo.h5"))
        self.detector.loadModel(detection_speed="faster")
        
        self.camera = cv2.VideoCapture(0)
        
        self.ui.pushButton_3.clicked.connect(self.stop_movie)
        self.ui.pushButton_2.clicked.connect(self.start_movie)

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_movie)

    def start_movie(self):
        self.movie_thread = MovieThread(self.camera)
        #self.movie_thread.start()
        self.update_timer.start(30)

    def stop_movie(self):
        self.update_timer.stop()

    def update_movie(self):
        ret, frame = self.camera.read()
        detected_image_array, detections = self.detector.detectCustomObjectsFromImage(output_type="array",input_type="array", input_image= frame,display_percentage_probability=False, display_object_name=True)# For numpy array inpu

        for eachObject in detections:
            print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
            print("--------------------------------")

        
        detected_image_array = cv2.resize(detected_image_array,(self.ui.label.frameGeometry().height(),self.ui.label.frameGeometry().width()))
        height, width, channel = detected_image_array.shape
        bytesPerLine = 3 * width
        qImg = QImage(detected_image_array.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap01 = QPixmap.fromImage(qImg)
        pixmap_image = QPixmap(pixmap01)
        self.ui.label.setPixmap(pixmap_image)
        self.ui.label.show();
    
class MovieThread(QThread):
    def __init__(self, camera):
        super().__init__()
        self.camera = camera

    def run(self):
        print("time")

   
if __name__ == '__main__':
    app = QApplication([])
    window = StartWindows()
    window.show()
    app.exit(app.exec_())
