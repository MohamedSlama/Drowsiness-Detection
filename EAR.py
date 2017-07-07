import numpy as np
from math import sqrt


class EAR:
    """docstring for EAR."""
    def ear(self,lefteye,righteye):
            # EAR = ( ||p2-p6|| + ||p3-p5|| ) / 2*( ||p1-p4|| )

            LeftEAR = (self.Euclidean(lefteye[1], lefteye[5]) + self.Euclidean(lefteye[2], lefteye[4])) / (2 * self.Euclidean(lefteye[0], lefteye[3]))
            RightEAR = (self.Euclidean(righteye[1], righteye[5]) + self.Euclidean(righteye[2], righteye[4]))  / (2 * self.Euclidean(righteye[0], righteye[3]))

            return (LeftEAR + RightEAR) / 2



    def Euclidean(self,p, q):
        # res = np.squeeze(np.asarray(q))
        # ecl = sqrt((res.item(0)*res.item(0))+(res.item(1)*res.item(1)))
        res = p - q
        return np.linalg.norm(res)
