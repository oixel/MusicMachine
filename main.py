import cv2
import player

# Uses camera to capture current video
capture = cv2.VideoCapture(0)

# Used to detect whether a QR Code is in camera
detector = cv2.QRCodeDetector()

while True:
    # Dumps unneeded return and then stores current image into variable
    _, image = capture.read()

    # Stores data into variable and dumps unneeded returns
    data, _, _ = detector.detectAndDecode(image)

    # If a QR Code is found, store the data as command and end the loop
    if data:
        command = data
        break

    # Closes loop if q is pressed
    if cv2.waitKey(1) == ord("q"):
        command = None
        break

# Stops scanning functionality and turns off camera
capture.release()

# Runs command on QR Code
player.play(command)