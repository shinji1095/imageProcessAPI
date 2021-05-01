import cv2
from matplotlib import pyplot as plt

class ImageController():
    def __init__(self):
        image = None

    def getImage(self):, 
        self.image = 

    def _getThreshold(self):
        pass

    def outputBinary(self, threshold):
        pass

fileName = "image2.jpg"
img = cv2.imread(fileName)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray.png", img_gray)
hist = cv2.calcHist([img_gray],[0],None,[256],[0,256])
data = list(map(lambda v: v[0], hist))
def test():
    return "test"

def get_threshold(hist, rate):
    total = sum(hist)
    print("total is ", total)
    threshNum = total * rate
    print("backgraund is ", threshNum)
    count = 0
    for i, v in enumerate(hist):
        count += v
        if count >= threshNum:
            index = i
            break
    return index

threshold = get_threshold(data, 0.3)
print("threshold is ", threshold)
ret, img_thresh = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
cv2.imwrite("binary2.png", img_thresh)
plt.hist(img_gray.ravel(),256,[0,256]); plt.show()
