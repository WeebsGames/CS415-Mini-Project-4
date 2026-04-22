import cv2
import numpy as np


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