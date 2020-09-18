# Gaze Tracking

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![GitHub stars](https://img.shields.io/github/stars/antoinelame/GazeTracking.svg?style=social)](https://github.com/antoinelame/GazeTracking/stargazers)

NOTE: This repository has been cloned from (https://github.com/antoinelame/GazeTracking/stargazers) and I've added some enhancements like storing the result data & plotting Pie chart as per data. Working on heatMap. Will Update soon...

This is a Python (2 and 3) library that provides a **webcam-based eye tracking system**. It gives you the exact position of the pupils and the gaze direction, in real time.

## Installation

Clone this project:

```
git clone https://github.com/antoinelame/GazeTracking.git
```

Install these dependencies (NumPy, OpenCV, Dlib):

```
pip install -r requirements.txt
```

> The Dlib library has four primary prerequisites: Boost, Boost.Python, CMake and X11/XQuartx. If you doesn't have them, you can [read this article](https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/) to know how to easily install them.

Run the demo:

```
python example.py
```

## Documentation

In the following examples, `gaze` refers to an instance of the `GazeTracking` class.

### Refresh the frame

```python
gaze.refresh(frame)
```

Pass the frame to analyze (numpy.ndarray). If you want to work with a video stream, you need to put this instruction in a loop, like the example above.

### Position of the left pupil

```python
gaze.pupil_left_coords()
```

Returns the coordinates (x,y) of the left pupil.

### Position of the right pupil

```python
gaze.pupil_right_coords()
```

Returns the coordinates (x,y) of the right pupil.

### Looking to the left

```python
gaze.is_left()
```

Returns `True` if the user is looking to the left.

### Looking to the right

```python
gaze.is_right()
```

Returns `True` if the user is looking to the right.

### Looking at the center

```python
gaze.is_center()
```

Returns `True` if the user is looking at the center.

### Horizontal direction of the gaze

```python
ratio = gaze.horizontal_ratio()
```

Returns a number between 0.0 and 1.0 that indicates the horizontal direction of the gaze. The extreme right is 0.0, the center is 0.5 and the extreme left is 1.0.

### Vertical direction of the gaze

```python
ratio = gaze.vertical_ratio()
```

Returns a number between 0.0 and 1.0 that indicates the vertical direction of the gaze. The extreme top is 0.0, the center is 0.5 and the extreme bottom is 1.0.

### Blinking

```python
gaze.is_blinking()
```

Returns `True` if the user's eyes are closed.

### Webcam frame

```python
frame = gaze.annotated_frame()
```

Returns the main frame with pupils highlighted.

## You want to help?

Your suggestions, bugs reports and pull requests are welcome and appreciated. You can also starring ⭐️ the project!

If the detection of your pupils is not completely optimal, you can send me a video sample of you looking in different directions. I would use it to improve the algorithm.

## Licensing

This project is released by Antoine Lamé under the terms of the MIT Open Source License. View LICENSE for more information.
