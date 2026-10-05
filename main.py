import cv2
import mediapipe as mp
import time

mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

count = 0
state = "UP"
last_count = 0

while True:

    ok, frame = cap.read()

    if not ok:
        break

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)

    if result.pose_landmarks:

        p = result.pose_landmarks.landmark

        nose = p[mp_pose.PoseLandmark.NOSE]
        left = p[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right = p[mp_pose.PoseLandmark.RIGHT_SHOULDER]

        shoulder = (left.y + right.y) / 2

        movement = nose.y - shoulder

        if movement > 0.03:
            new_state = "DOWN"

        elif movement < -0.01:
            new_state = "UP"

        else:
            new_state = state

        if state == "DOWN" and new_state == "UP":
            if time.time() - last_count > 0.25:
                count += 1
                last_count = time.time()

        state = new_state

        lx = int(left.x * w)
        ly = int(left.y * h)

        rx = int(right.x * w)
        ry = int(right.y * h)

        cv2.line(
            frame,
            (lx, ly),
            (rx, ry),
            (0, 255, 0),
            3
        )

        cv2.circle(
            frame,
            (lx, ly),
            8,
            (0, 255, 0),
            -1
        )

        cv2.circle(
            frame,
            (rx, ry),
            8,
            (0, 255, 0),
            -1
        )

        cv2.putText(
            frame,
            "Push-ups: " + str(count),
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0, 255, 255),
            3
        )

        cv2.putText(
            frame,
            state,
            (30, 95),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

    cv2.imshow("Push Up Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()