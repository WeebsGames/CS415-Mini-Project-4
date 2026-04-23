import cv2
import numpy as np
import math
from matplotlib import pyplot as plt


img = np.ones((500, 500, 3), dtype=np.uint8) * 255
a = np.array([100, 40])
cv2.circle(img, tuple(a.astype(int)), 10, (0, 0, 255), -1)

# Rotation matrix for 60 degrees clockwise
theta = -60 * np.pi / 180
rotation = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])

# Rotate a around origin to get b
b = rotation @ a
cv2.circle(img, tuple(b.astype(int)), 10, (0, 255, 0), -1)

# Point c
c = np.array([100, 100])
cv2.circle(img, tuple(c.astype(int)), 10, (0, 0, 0), -1)

# Rotate a around c by 60 degrees clockwise to get d
# Translate a to origin relative to c
a_trans = a - c
d_trans = rotation @ a_trans
d = d_trans + c

# Draw solid blue circle at d
cv2.circle(img, tuple(d.astype(int)), 10, (255, 0, 0), -1)


cv2.imwrite('output.png', img)

cv2.imshow('Transformed Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# img = cv2.imread("lena.png")
# rows, cols, ch, = img.shape

# translation = np.array([[1,0],
#                        [0,1],
#                        [100,200]])

# translated = cv2.warpAffine(img, translation, (cols, rows))
img = cv2.imread('lena.png')
rows, cols, ch = img.shape

#start
pts1 = np.float32([[50, 50],
                   [200, 50], 
                   [50, 200]])

#end
pts2 = np.float32([[150, 250],
                   [300, 250], 
                   [150, 400]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite("lena_transform.png", dst)
cv2.imshow("transform", dst)

# Flip horizontally with respect to the image center.
# This uses a 2x3 affine matrix with translation so the mirror axis is the center.
M = np.float32([[-1, 0, cols - 1],
                [0, 1, 0]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite("lena_flip.png", dst)
cv2.imshow("flip", dst)

M = np.float32([[math.cos(math.radians(45)), -1 * math.sin(math.radians(45)), 0],
                [math.sin(math.radians(45)), math.cos(math.radians(45)), 0]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite("lena_rot_origin.png", dst)
cv2.imshow("rot_origin", dst)

# Rotate lena.png around the center by 45 degrees clockwise
center = (cols / 2, rows / 2)
M = cv2.getRotationMatrix2D(center, -45, 1)  # -45 degrees for clockwise rotation
rotated = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite('lena_rot_center.png', rotated)


cv2.imshow('Rotated Lena', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()
