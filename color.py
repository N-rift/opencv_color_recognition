import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # Green
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # Blue
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    colors = [
        ("Red", lower_red, upper_red),
        ("Green", lower_green, upper_green),
        ("Blue", lower_blue, upper_blue)
    ]

    for name, lower, upper in colors:

        mask = cv2.inRange(hsv, lower, upper)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:

            area = cv2.contourArea(contour)

            if area > 500:

                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (255, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    name,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                )

    cv2.imshow("Color Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()