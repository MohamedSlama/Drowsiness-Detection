import cv2
import sys
import Status as st
import Alarm


def ContrastHist(Img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(Img)


def Camera():
    if len(sys.argv) > 1:
        CamNum = sys.argv[1]
    else:
        print("This's The Main Camera")
        CamNum = 0

    # Resize Capture
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300);
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300);

    return cv2.VideoCapture(int(CamNum))


cap = Camera()


def writeText(frame, text, color):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, (20, 20), font, 1, color, 2, cv2.LINE_AA)


def detect():
    alarm = Alarm.Alarm()
    Time = 0
    cv2.namedWindow('frame')
    while (cap.isOpened() and cv2.getWindowProperty('frame', 0) >= 0):
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = ContrastHist(gray)
            state = st.main(gray)

            if state == -1:
                writeText(frame, '', (0, 0, 0))
                Time = Time + 1
                if Time == 10:
                    if not alarm.Status():
                        alarm.Start()
            elif state:
                writeText(frame, 'Opened', (0, 255, 0))
                Time = 0
                if alarm.Status():
                    alarm.Stop()
            else:
                writeText(frame, 'Closed', (0, 0, 255))
                Time = Time + 1
                if Time == 10:
                    if not alarm.Status():
                        alarm.Start()

            cv2.imshow('frame', frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


detect()
