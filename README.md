# Basic Image Processing and Shape Detection using OpenCV

## Project overview

This is a small command-line Computer Vision project for demonstrating common image processing steps. It uses OpenCV and NumPy rather than machine learning.

## Problem statement

Before using advanced Computer Vision methods, it is important to understand how an image is represented and how simple operations change it. This project applies those operations to a local image and saves the results.

## Objectives and features

- Load images and report width, height, channels, and pixel statistics.
- Resize, crop, rotate, and convert BGR images to grayscale.
- Apply Gaussian blur, median blur, sharpening, and binary thresholding.
- Detect edges with Canny and find simple shapes using contours.

Grayscale reduces three BGR channels to one intensity channel. Blurring reduces small noise, thresholding separates foreground from background, and Canny finds strong intensity changes. Contours are boundaries; approximating a contour with polygons makes basic shape naming possible.

## Technologies

Python, OpenCV, NumPy, and pytest.

## Project structure

```text
main.py                 Command-line entry point
cv_modules/             Small processing modules
images/                 Sample inputs (generated locally)
output/                 Saved results
tests/                  Basic automated tests
docs/                   Simple academic diagrams
statement.md            Short project statement
```

## Installation

Create and activate a virtual environment:

```text
python -m venv venv
venv\\Scripts\\Activate.ps1
source venv/bin/activate
```

Install requirements with `pip install -r requirements.txt`.

The included sample files can be recreated with `python create_samples.py` if needed.

## Running the project

```text
python main.py --image images/sample.jpg --operation grayscale
python main.py --image images/sample.jpg --operation resize
python main.py --image images/sample.jpg --operation gaussian
python main.py --image images/sample.jpg --operation edges
python main.py --image images/shapes.jpg --operation shapes
python main.py --image images/sample.jpg --operation stats
```

Results are written to `output/`. Available operations are `grayscale`, `resize`, `crop`, `rotate`, `gaussian`, `median`, `sharpen`, `threshold`, `edges`, `shapes`, and `stats`.

## Tests

Run `python -m pytest`. The tests check grayscale output, resize dimensions, and that shape detection runs.

## Sample results

For `images/shapes.jpg`, the shape operation creates `output/shapes.png` and prints the shapes found.

## Limitations and future improvements

The detector works best with clear, high-contrast shapes and may misclassify noisy or overlapping objects. User-selectable thresholds, better rotated-shape handling, and batch processing could be added later.
