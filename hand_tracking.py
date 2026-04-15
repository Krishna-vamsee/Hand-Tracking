import cv2
import mediapipe as mp
import time
import math

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

pTime = 0



# Physics variables
rest_length = 150
velocity = 0
current_length = rest_length

# Physics tuning
k = 0.2      # spring strength
damping = 0.85

def get_point(hand_landmarks, index, w, h):
    x = int(hand_landmarks.landmark[index].x * w)
    y = int(hand_landmarks.landmark[index].y * h)
    return x, y

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def is_pinch(hand_landmarks, w, h):
    thumb = get_point(hand_landmarks, 4, w, h)
    index = get_point(hand_landmarks, 8, w, h)
    dist = distance(thumb, index)
    return dist < 40, thumb

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    pinch_points = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            pinch, point = is_pinch(handLms, w, h)
            if pinch:
                pinch_points.append(point)
                cv2.circle(img, point, 10, (0, 255, 0), cv2.FILLED)

    # 🧵 Physics-based elastic
    if len(pinch_points) == 2:
        (x1, y1), (x2, y2) = pinch_points

        target_length = distance((x1, y1), (x2, y2))

        # Hooke's Law (spring)
        force = k * (target_length - current_length)

        # Update velocity
        velocity += force
        velocity *= damping

        # Update length
        current_length += velocity

        thickness = max(2, min(15, int(current_length / 20)))

        # Draw band
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), thickness)

        cv2.putText(img, f"Stretch: {int(current_length)}", (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    else:
        # 💥 Snap back when released
        force = k * (rest_length - current_length)
        velocity += force
        velocity *= damping
        current_length += velocity

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) != 0 else 0
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Elastic Physics Interaction", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()



