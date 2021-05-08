# import OpenCV library
import cv2

# import matplot library
import matplotlib.pyplot as plt

# configure mobilenet aglorithm location and frozen model location
config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

# load frozen model
model = cv2.dnn_DetectionModel(frozen_model, config_file)

# create a list and load all class labels
classLabels = []
file_name = 'labels.txt'
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')

# pre configure input images to rgb with restricted pixel size
model.setInputSize(320, 320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

# read an image
img = cv2.imread('img_1.jpg')

'''
# view image using matplot library
plt.imshow(img)
plt.show()
'''

# model.detect return 3 values (stored in respective variables)
ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)
print(ClassIndex)

# configure font sclae and box dimensions
font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN
for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
    cv2.rectangle(img, boxes, (255, 0, 0), 2)
    cv2.putText(img, classLabels[ClassInd-1], (boxes[0]+10, boxes[1]+40), font, fontScale=font_scale, color=(0, 255, 0), thickness=3)

# Display final processed image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()