import landmarks
import EAR
import Predict

Landmarks = landmarks.FindLandMarks()
Ear = EAR.EAR()
predict = Predict.Predict()
feature,target= predict.read('dataset.txt')

def main(Img):
    Res = Landmarks.GetLeftAndRight(Img)
    if Res is not None:
        opLeft, opRight = Res
        opEar = Ear.ear(opLeft, opRight)

        # Using SVM
        # return predict.Svm(opEar,feature,target)

        # Using Treash
        return predict.Tresh(opEar)
    else:
        return -1

if __name__ == '__main__':
    try:
        main(openedImg)
    except:
        print('error')
