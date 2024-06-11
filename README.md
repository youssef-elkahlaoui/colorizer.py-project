# Photo Colorizer

This project is a photo colorization tool that converts grayscale images to color images using a deep learning model. The model is based on a pre-trained convolutional neural network (CNN) that predicts the color values for each pixel in a grayscale image.

## Features

- Load and colorize images from your local filesystem.
- Option to convert images to grayscale before colorization.
- Save colorized images to your filesystem.
- User-friendly graphical interface using PySimpleGUI.

## Installation

### Requirements

- Python 3.x
- OpenCV
- NumPy
- PySimpleGUI

### Steps

1. Clone the repository:
    bash
    git clone https://github.com/youssef-elkahlaoui/colorizer.py-project.git
    cd photo-colorizer
    

2. Install the required packages:
    bash
    pip install -r requirements.txt
    

3. Download the model files:
    - [colorization_deploy_v2.prototxt](https://github.com/richzhang/colorization/blob/caffe/models/colorization_deploy_v2.prototxt)
    - [colorization_release_v2.caffemodel](https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1)
    - [pts_in_hull.npy](https://github.com/richzhang/colorization/blob/caffe/resources/pts_in_hull.npy)

4. Place the model files in the model directory.

## Usage

Run the application using the following command:
```bash
python main.py
```
## Structure:
- pyFinal
  - main.py                  # Main entry point of the application
  - gui.py                   # Contains GUI creation and update functions
  - colorizer.py             # Functions for loading the model and colorizing images
  - utils.py                 # Utility functions for image processing
  - requirements.txt         # Python dependencies
  -  model/                   # Directory for storing model files
      - colorization_deploy_v2.prototxt
      - colorization_release_v2.caffemodel
      - pts_in_hull.npy
  -  README.md                # Project description and instructions
