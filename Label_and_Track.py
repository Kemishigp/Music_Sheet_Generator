import cv2
import numpy as np


def LabelNotes(WhiteNotes: list, BlackNotes: list, A_Notes: list, AFlat: list):
    """Takes 4 parameters and uses them to generate 2 dictionaries 
    where the pixel is the key and the note is the value"""
    Octave = 0
    CDEFGAB = {}
    DEGAB_Flat = {}
    for i in range(0, len(WhiteNotes)-1):
        if WhiteNotes[i] in A_Notes:
            CDEFGAB[int(WhiteNotes[i])] = 'A'+str(Octave)
            if i+1 in range(0, len(WhiteNotes)-1):
                CDEFGAB[int(WhiteNotes[i+1])] = 'B'+str(Octave)
            if i+2 in range(0, len(WhiteNotes)-1):
                CDEFGAB[int(WhiteNotes[i+2])] = 'C'+str(Octave+1)
            if i+3 in range(0, len(WhiteNotes)-1):
                CDEFGAB[int(WhiteNotes[i+3])] = 'D'+str(Octave+1)
            if i+4 in range(0, len(WhiteNotes)-1):
                CDEFGAB[int(WhiteNotes[i+4])] = 'E'+str(Octave+1)
            if i+5 in range(0, len(WhiteNotes)-1):
                CDEFGAB[int(WhiteNotes[i+5])] = 'F'+str(Octave+1)
            if i+6 in range(0, len(WhiteNotes)-1):
                CDEFGAB[int(WhiteNotes[i+6])] = 'G'+str(Octave+1)
            Octave += 1
    Octave = 0
    for i in range(0, len(BlackNotes)-1):
        if BlackNotes[i][0] in AFlat:
            DEGAB_Flat[int(BlackNotes[i][0])] = 'A'+str(Octave)+'♭'
            if i+1 in range(0, len(BlackNotes)-1):
                DEGAB_Flat[int(BlackNotes[i+1][0])] = 'B'+str(Octave)+'♭'
            if i+2 in range(0, len(BlackNotes)-1):
                DEGAB_Flat[int(BlackNotes[i+2][0])] = 'D'+str(Octave+1)+'♭'
            if i+3 in range(0, len(BlackNotes)-1):
                DEGAB_Flat[int(BlackNotes[i+3][0])] = 'E'+str(Octave+1)+'♭'
            if i+4 in range(0, len(BlackNotes)-1):
                DEGAB_Flat[int(BlackNotes[i+4][0])] = 'G'+str(Octave+1)+'♭'
            Octave += 1
    return CDEFGAB, DEGAB_Flat


def GetNotes(CDEFGAB: dict, DEGAB_Flat: dict, aoi_ero, frame: int, Frames_Notes: list):
    """This function takes 2 dictionaries and the aoi
    It looks at pixel values in the aoi corresponding to the dictionary keys to determine if a note is pressed
    It then returns a list with the notes pressed and the frame they were played at"""
    at = 1
    for i in aoi_ero[0]:
        """"""
        at += 1
        intensity = i
        if intensity > 200:
            if at in CDEFGAB.keys():
                Frames_Notes.append([CDEFGAB.get(at), frame])
                print(CDEFGAB.get(at))
        if intensity > 200:
            if at in DEGAB_Flat.keys():
                Frames_Notes.append([DEGAB_Flat.get(at), frame])
                print(DEGAB_Flat.get(at))
    return Frames_Notes

    # for i in DEGAB_Flat:
    #     """"""
    #     if i in range(0, len(aoi_ero)-1):
    #         intensity = aoi_ero[i][1]
    #         if intensity > 200:
    #             print(DEGAB_Flat.get(i))

    # WhiteNotes = []
    # for i in range(0, 20):
    #     WhiteNotes.append(i)

    # A_Notes = [0, 7, 14]
    # CDEFGAB = LabelNotes(WhiteNotes, A_Notes)
    # j = int()
    # r = CDEFGAB.values()
    # print(r)
