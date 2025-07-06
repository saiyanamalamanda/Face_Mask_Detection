import cv2
import numpy as np

img = np.zeros((200, 200, 3), dtype=np.uint8)
cv2.putText(img, 'Test', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv2.imshow('Test Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
