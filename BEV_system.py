import cv2
import numpy as np
image_path = "road.jpg"  # ← замени на свой путь
img = cv2.imread(image_path)
pts_img = []
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pts_img.append((x, y))
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("image", img)
cv2.imshow("image", img)
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
if len(pts_img) != 4:
    raise ValueError("Нужно выбрать ровно 4 точки!")
pts_world = []
for i in range(4):
    coords = input(f"Точка {i+1}: ").split()
    pts_world.append((float(coords[0]), float(coords[1])))

pts_img = np.array(pts_img, dtype=np.float32)
pts_world = np.array(pts_world, dtype=np.float32)
H, _ = cv2.findHomography(pts_img, pts_world)
print("Матрица H:")
print(H)
width, height = 500, 800  # размер результата в пикселях
bev = cv2.warpPerspective(img, H, (width, height))
cv2.imshow("BEV view", bev)
cv2.waitKey(0)
cv2.destroyAllWindows()
