import random
import cv2
import numpy as np
from Image_Processing2 import Color_filters, getConnectedComponents
from NoteCoordinates2 import getWhiteNotes
from Label_and_Track import LabelNotes, GetNotes
import csv
# from LabelNotes import LabelNotes
# Loop to cycle through the video


def DistanceBetweenNotes(centroids):
    """Calculates the average distance between each connected component"""
    firstCentroid = centroids[0]
    lastCentroid = centroids[len(centroids)-1]
    Distance = lastCentroid[0]-firstCentroid[0]
    averageDistance = Distance/(len(centroids)-2)
    return averageDistance


# LISTS
global Frame_Notes
Frame_Notes = []
Frame_Note_csv = None
# # Pull the video file
cap = cv2.VideoCapture("Synthesiaa.mp4")
frame = 0
img = None
# WHILE LOOP THAT GATHERS DATA
while True:
    frame += 1
    # Loading the Video
    _, vid = cap.read()
    vid = cv2.cvtColor(vid, cv2.COLOR_RGB2GRAY)
    # cv2.imshow("Video", vid)
    # Take a screenshot
    if frame == 209:
        img = vid
# 1. IMAGE PROCESSING
    if img is not None:
        # Take the bottom third of the screenshot to isolate the piano keyboard
        height, width = img.shape
        third = int(height/3)
        half = int(height/2)

        piano = img[height-half: height-10, 0: width]
        # Area of Interest to track falling bars
        aoi = vid[height-third-1:height-third, 0:width]
        cv2.imshow("video", vid)
        # cv2.imshow("Piano", piano)

        # Image process the piano and the aoi to be tracked
        piano_thr, aoi_ero = Color_filters(piano, aoi)
        # cv2.imshow("AOI", aoi_ero)
# ----------------------WORKS------------------------------#
        # Gather the black key notes
# 2. Gather the notes' coordinates
        output, BlackNotes = getConnectedComponents(
            piano_thr)
        cv2.imshow("Connected", output)
# -----------------------------WORKS --------------------------#
        # Generate a list with the white notes' X coordinates
        # and the coordinates for the A and A flat notes
        WhiteNotes, A_Notes, AFlat = getWhiteNotes(BlackNotes)
# 3. Label and track the notes
        CDEFGAB, DEGAB_Flat = LabelNotes(
            WhiteNotes, BlackNotes, A_Notes, AFlat)
        Frame_Note_csv = GetNotes(
            CDEFGAB, DEGAB_Flat, aoi_ero, frame, Frame_Notes)
    # 4. Convert the data gathered to a csv file and export it
    fields = ['Note', 'Frame']
    filename = "Notes_Playedd.csv"
    if Frame_Note_csv is not None:
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields
            csvwriter.writerow(fields)
            # writing the data rows
            csvwriter.writerows(Frame_Note_csv)
    ########################################### TEST CODE ###########################################

        # TEST CONNECTED COMPONENTS
        # j = len(BlackNotes)-1
        Circle = None
        # for i in range(0, len(BlackNotes)-1):
        #     Circle = cv2.circle(vid, (int(BlackNotes[i][0]), int(BlackNotes[i][1])),
        #                         radius=10, color=(0, 255, 0), thickness=5)
        # cv2.imshow("Circle", Circle)
    key = cv2.waitKey(1)
    i = 0
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
