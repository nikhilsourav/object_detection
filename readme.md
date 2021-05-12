# Python Object detection

This project uses TensorFlow based frozen model and OpenCV python library for object detection of static images.

## Demo:

<img src = './images/demo.png' width = '550' height = '360'>

## Programming language:

- [Python](https://www.python.org/)

## Algorithm:

- [Single-Shot multibox Detection (SSD-MoblieNet version 3)](https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API)

## Dataset:

- [coco (80 classes)](https://github.com/nikhilsourav/object_detection/blob/main/labels.txt)

## Dependencies:

- [OpenCV](https://opencv.org/)
- [mathplotlib](https://matplotlib.org/)

## How to run?

- clone the repository to your local machine
- navigate to this cloned directory
- from the terminal install dependencies using these commands:
  - python -m pip install opencv-python
  - python -m pip install matplotlib
- after installing the dependencies run the <span>main.py</span> file from terminal using this command:
  - python <span>main.py</span>
- To analyze a different image change the image number in <span>main.py</span> line 27 to any number between 1 to 5
  - example: <br/>
    `img = cv2.imread('images/img_1.jpg')` for first image <br/>
    `img = cv2.imread('images/img_2.jpg')` for second image <br/>
    and so on..

## Feel free to contribute to this project by providing more relevant images

<br/>

# Thank you