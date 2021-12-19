import tkinter
import tkinter.messagebox
import cv2
import numpy as np
import face_recognition
import os
import csv
from datetime import datetime
import os.path

access = ' '
path = 'face-recognition/ImagesAttandenceProject'
images = []
classNames = []
myList = os.listdir(path)
cap = ''
today = datetime.today()
# /Users/naukadhabalia/git/library-management/
attendance_csv = 'face-recognition/Attendance' + today.strftime(
    "%m_%d_%y") + '.csv'


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    if os.path.isfile(attendance_csv):
        access = 'r+'
    else:
        access = 'w+'
    print(access)
    with open(attendance_csv, access) as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


for img in myList:
    curImg = cv2.imread(f'{path}/{img}')
    images.append(curImg)
    classNames.append(os.path.splitext(img)[0])

encodeListKnown = findEncodings(images)


class main:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title('Controlling Webcam for Face Recognition')

        self.bottom_frame = tkinter.Frame()

        self.start_btn = tkinter.Button(self.bottom_frame,
                                        text='Start Webcam',
                                        command=self.start_cam)
        self.stop_btn = tkinter.Button(self.bottom_frame,
                                       text='Stop Webcam',
                                       command=self.stop_cam)

        self.read_csv_btn = tkinter.Button(self.bottom_frame,
                                           text='Read CSV',
                                           command=self.read_csv)

        self.start_btn.pack(side='left', padx=10, pady=10)
        self.stop_btn.pack(side='left', padx=10, pady=10)
        self.read_csv_btn.pack(side='left')

        self.bottom_frame.pack(ipadx=10, ipady=10)

        tkinter.mainloop()

    def read_csv(self):
        with open(attendance_csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def start_cam(self):

        global cap
        # print(encodeListKnown)

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Scale image to small.0.25
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    markAttendance(name)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            cv2.imshow('Webcam', img)
            cv2.waitKey(1)

        # tkinter.messagebox.showinfo('Starting Webcam...!')

    def stop_cam(self):

        global cap
        print('stop')

        cap.release()
        cv2.destroyAllWindows()
        self.main_window.quit()

        # tkinter.messagebox.showinfo('Stoping Webcam...!')


if __name__ == '__main__':
    main()
