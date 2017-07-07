import dlib
import numpy as np

PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)
RIGHT_EYE_POINTS = list(range(36, 42))
LEFT_EYE_POINTS = list(range(42, 48))

class FindLandMarks:
    """Get Person Face LandMarks"""

    def get_landmarks(self,Img):
        try:
            rects = detector(Img)
            if len(rects) == 1:
                return np.matrix([[p.x, p.y] for p in predictor(Img, rects[0]).parts()])
            else:
                return None
        except:
            print('Not Image')

    def GetLeftAndRight(self,Image):

        Res = self.get_landmarks(Image)
        if Res is None:
            return None
        return Res[LEFT_EYE_POINTS],Res[RIGHT_EYE_POINTS]
