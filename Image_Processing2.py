import cv2
import numpy as np


def Color_filters(piano, aoi):
    """Collects an image and converts it to a binary image"""
    kernel = np.ones((1, 7), np.uint8)
    # Apply an RGB filter and grayscale to both images
    piano_rgb = cv2.cvtColor(piano, cv2.COLOR_BGR2RGB)
    piano_gray = cv2.cvtColor(piano_rgb, cv2.COLOR_RGB2GRAY)
    aoi_rgb = cv2.cvtColor(aoi, cv2.COLOR_BGR2RGB)
    aoi_gray = cv2.cvtColor(aoi_rgb, cv2.COLOR_RGB2GRAY)
    # Apply an inverted binary threshhold to the piano
    _, piano_thr = cv2.threshold(piano_gray, 50, 255, cv2.THRESH_BINARY_INV)
    # Apply a binary threshhold to the aoi and then erode to reduce margin of error
    _, aoi_thr = cv2.threshold(aoi_gray, 100, 255, cv2.THRESH_BINARY)
    aoi_ero = cv2.erode(aoi_thr, kernel)
    return piano_thr, aoi_ero


def getConnectedComponents(piano_thr):
    """This function takes a binary  image
    and returns the connected components,
    centroid(Blacknote) coordinates, and notewidth"""
    analysis = cv2.connectedComponentsWithStats(piano_thr,
                                                4,
                                                cv2.CV_32S)
    (totalLabels,  # Number of labels (int)
     label_ids,
     values,  # (X,Y,width,height,area)
     centroid  # (X,Y) Center coordinates
     ) = analysis
    output = np.zeros(piano_thr.shape, dtype="uint8")
    centroids = []
    # Iterate through the list of connected components
    for i in range(1, totalLabels):
        area = values[i, cv2.CC_STAT_AREA]
        NoteWidth = values[i, cv2.CC_STAT_WIDTH]
        NoteStart = values[i, cv2.CC_STAT_LEFT]
        # Only take into account the components with a certain area
        if (area > 1000) and (area < 3000):
            # Gather the centroid of the components
            # and the notewidths and their coordinates
            (X, Y) = centroid[i]
            centroids.append((X, Y))
            # Convert the components color to WHITE
            componentMask = (label_ids == i).astype("uint8") * 255
            # Generate the image to be read later
            output = cv2.bitwise_or(output, componentMask)
    # centroids.pop(0)
    # centroids.pop(0)
    return output, centroids
