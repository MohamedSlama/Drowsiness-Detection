from os import listdir
from os.path import isfile, join
import cv2
import dlib
import numpy as np
from math import sqrt


PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)

RIGHT_EYE_POINTS = list(range(36, 42))
LEFT_EYE_POINTS = list(range(42, 48))


def ContrastHist(Img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(Img)


def get_landmarks(im):
    try:
        rects = detector(im)
        if len(rects) == 1:
            return np.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])
        else:
            return None
    except:
        print('Not Image')


def GetLeftAndRight(img):
    Res = get_landmarks(img)
    if Res == None:
        return None
    return Res[LEFT_EYE_POINTS], Res[RIGHT_EYE_POINTS]


def Euclidean(p, q):
    # res = np.squeeze(np.asarray(q))
    # ecl = sqrt((res.item(0)*res.item(0))+(res.item(1)*res.item(1)))
    res = p - q
    return np.linalg.norm(res)


def EAR(lefteye, righteye):
    # EAR = ( ||p2-p6|| + ||p3-p5|| ) / 2*( ||p1-p4|| )

    LeftEAR = (Euclidean(lefteye[1], lefteye[5]) + Euclidean(lefteye[2], lefteye[4])) / (2 * Euclidean(lefteye[0], lefteye[3]))
    RightEAR = (Euclidean(righteye[1], righteye[5]) + Euclidean(righteye[2], righteye[4])) / (2 * Euclidean(righteye[0], righteye[3]))

    return (LeftEAR + RightEAR) / 2


def main(Img):
    Img = ContrastHist(Img)

    Res = GetLeftAndRight(Img)
    if Res != None:
        Left, Right = Res
        Ear = EAR(Left, Right)
        return Ear
    else:
        return -1

cap = cv2.VideoCapture('smile.webm')

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200);

while 1:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ear = main(gray)
        if ear != -1:
            print('1 %s'%(ear))
        cv2.imshow('frame',frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:break

cap.release()
cv2.destroyAllWindows()
