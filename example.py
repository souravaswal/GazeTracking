"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import csv
import cv2
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from gaze_tracking import GazeTracking
from collections import Counter

gaze = GazeTracking()
webcam = cv2.VideoCapture("Resources/video1.mp4")

filename = "Resources/output.csv"
csvFile = open(filename, 'w')
# creating a csv writer object
csvwriter = csv.writer(csvFile)
# writing the fields
fields = ['Horizontal_Ratio', 'Vertical_Ratio', 'Gaze', 'Section in which person looking']
csvwriter.writerow(fields)

sectionDict = {
    'AX': 'Section 1',
    'AY': 'Section 2',
    'AZ': 'Section 3',
    'BX': 'Section 4',
    'BY': 'Section 5',
    'BZ': 'Section 6',
    'CX': 'Section 7',
    'CY': 'Section 8',
    'CZ': 'Section 9'}

count = 1
sentiment = []
try:
    while True:
        # We get a new frame from the webcam
        _, frame = webcam.read()

        if count % 2 == 0:
            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)

            frame = gaze.annotated_frame()
            horizontal_ratio = gaze.horizontal_ratio()
            vertical_ratio = gaze.vertical_ratio()

            lookingAtSection: str = ''
            if vertical_ratio > 0.66:
                lookingAtSection = 'C'  # extreme bottom
            elif vertical_ratio > 0.33:
                lookingAtSection = 'B'
            elif vertical_ratio >= 0:
                lookingAtSection = 'A'

            if horizontal_ratio > 0.66:
                lookingAtSection = lookingAtSection + 'X'  # extreme left
            elif horizontal_ratio > 0.33:
                lookingAtSection = lookingAtSection + 'Y'
            elif horizontal_ratio >= 0:
                lookingAtSection = lookingAtSection + 'Z'

            row = []
            row.append(round(horizontal_ratio, 2))
            row.append(round(vertical_ratio, 2))
            row.append(lookingAtSection)
            row.append(sectionDict.get(lookingAtSection))

            sentiment.append(sectionDict.get(lookingAtSection))
            csvwriter.writerow(row)

            cv2.putText(frame, "Left pupil:  " + str(gaze.pupil_left_coords()), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9,
                        (147, 58, 31), 1)
            cv2.putText(frame, "Right pupil: " + str(gaze.pupil_right_coords()), (90, 165), cv2.FONT_HERSHEY_DUPLEX,
                        0.9, (147, 58, 31), 1)
            cv2.imshow("Demo", frame)

            if cv2.waitKey(1) == 27:
                break
        count = count + 1
except Exception as ex:
    print(ex)

# To plot the data in pie chart
counts = Counter(sentiment[:-1])
plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%',)
plt.axis('equal')
plt.savefig('Ouput1.png')


csvFile.close()