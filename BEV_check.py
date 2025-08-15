import cv2
import numpy as np

# === 1. Вставь сюда свою матрицу H ===
H = np.array([
])

# === 2. Ожидаемые координаты в метрах ===
pts_world_expected = [
]

# === 3. Глобальный список для кликнутых точек ===
clicked_points = []

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        print(f"Точка {len(clicked_points)}: пиксели ({x}, {y})")
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("Image", img)

        if len(clicked_points) == 4:
            check_points()

def img_to_world(pt, H):
    p = np.array([pt[0], pt[1], 1.0])
    q = H @ p
    q /= q[2]  # нормализация
    return (q[0], q[1])
def check_points():
    print("\n=== Результат проверки ===")
    for i, pt in enumerate(clicked_points):
        X, Y = img_to_world(pt, H)
        print(f"Точка {i+1}: пиксели {pt}")
        print(f"→ Перевод в мир: ({X:.4f}, {Y:.4f}) м")
        print(f"Ожидалось: {pts_world_expected[i]}\n")
img = cv2.imread()  
cv2.imshow("Image", img)
cv2.setMouseCallback("Image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
