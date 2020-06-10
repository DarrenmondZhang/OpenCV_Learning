import cv2 as cv
import numpy as np


def canny_demo(image):
    t = 80
    canny_output = cv.Canny(image, t, t * 2)
    # cv.imwrite("D:/canny_output.png", canny_output)
    return canny_output


src = cv.imread("H:/OpenCV_Learning/059_Hough_Line/test.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
binary = canny_demo(src)
cv.imshow("binary", binary)

linesP = cv.HoughLinesP(binary, 1, np.pi / 180, 50, None, 50, 10)
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(src, (l[0], l[1]), (l[2], l[3]), (255, 0, 0), 1, cv.LINE_AA)

# 显示
cv.imshow("hough line demo", src)
cv.imwrite("hough_line_2.png", src)
cv.waitKey(0)
cv.destroyAllWindows()


