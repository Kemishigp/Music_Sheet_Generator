import pandas as pd
import numpy as np
import csv


def sort_csv():
    nf = pd.read_csv('Notes_Played.csv')
    # print(nf)
    # 1. SORT
    sorted = nf.sort_values(['Note', 'Frame'], ascending=True)
    # 2. Create a new csv file with sorted notes
    fields = ['Note', 'Frame']
    filename = "Notes_Played_Sortedd.csv"
    for row in sorted:
        print(row)
    Sorted_List = []
    for index, row in sorted.iterrows():
        Sorted_List.append([row['Note'], row['Frame']])
        print(row['Note'], row['Frame'])
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerows(Sorted_List)
    print(Sorted_List)
# 3. Manipulate the sorted csv file


def group_consec_frames():
    # Get the sorted notes csv file
    ns = pd.read_csv('Notes_Played_sorted.csv')
    # Create a list of lists
    Lists = []
    List_No = 0
    Lists.append([])

    # Iterate through the csv file
    for i in range(1, len(ns)):
        prev_row = ns.iloc[i-1]
        curr_row = ns.iloc[i]
        prev_frame = prev_row['Frame']
        curr_frame = curr_row['Frame']
        # Compare the previous frame to the current frame
        if i == len(ns)-1:
            Lists[List_No].append([prev_row['Note'], prev_row['Frame']])
            Lists[List_No].append([curr_row['Note'], curr_row['Frame']])
        else:
            if prev_frame+1 == curr_frame:
                # If frame numbers are consecutive then append the prev frame
                Lists[List_No].append([prev_row['Note'], prev_row['Frame']])
                # print("IF")
            else:
                # If frame numbers are not consecutive then append prev_frame and start a new list
                Lists[List_No].append([prev_row['Note'], prev_row['Frame']])
                Lists.append([])
                List_No += 1
    # [Note, Length, Starting Frame]
    List_No = 0
    NLF_List = []
    for i in Lists:
        Note = Lists[List_No][0][0]
        Length = len(Lists[List_No])
        Starting_Frame = Lists[List_No][0][1]
        NLF_List.append([Note, Length, Starting_Frame])
        List_No += 1
    fields = ['Note', 'Length', 'Starting_Frame']
    filename = 'Note_Length_Framee.csv'
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerows(NLF_List)
