import cv2
import numpy as np


def DistanceBetweenNotes(centroids: list):
    """Calculates the average distance between each connected component"""
    firstCentroid = centroids[0]
    lastCentroid = centroids[len(centroids)-1]
    Distance = lastCentroid[0]-firstCentroid[0]
    averageDistance = Distance/(len(centroids)-7)
    return averageDistance


def getWhiteNotes(centroids: list):
    """Returns list with the the x coordinates of each white note"""
    avgDist = DistanceBetweenNotes(centroids)
    link = 0
    # Create a list to store the white notes
    whiteNotes = []
    A_Notes = []
    AFlat = []
    # Iterate through the black notes to get x coordinates for white notes
    for i in range(1, len(centroids)):
        # Calculate the distance between each black note
        coordinates = centroids[i]
        XCoordinates = coordinates[0]
        prevCoord = centroids[i-1]
        prevXCoord = prevCoord[0]
        difference = XCoordinates - prevXCoord
        if avgDist > (difference):
            link += 1
        else:
            link = 0
        # If the black notes are close then there is 1 white note between them
        if link == 1:
            x = int(prevXCoord+(difference/2))
            whiteNotes.append(x)
        # If the black notes are further apart
        # then there are 2 white notes between them
        elif link == 2:
            x = int(prevXCoord+(difference/2))
            whiteNotes.append(x)
            A_Notes.append(x)
            AFlat.append(prevXCoord)
        elif link == 0:
            x = int(prevXCoord + (difference/4))
            whiteNotes.append(x)
            x = int(XCoordinates-(difference/4))
            whiteNotes.append(x)
        else:
            print("Link error")
    return whiteNotes, A_Notes, AFlat
