import functions as fs
import cv2
import os

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    grayscale = fs.convert_to_grayscale(frame)
    resized = fs.resize_image(grayscale, (280,80))
    ascii = fs.convert_to_ascii(resized)
    r = '\n'.join(map(''.join,ascii))
    os.system('cls')
    print(r)
    # Display the resulting frame
    cv2.imshow('Camera stream', frame)
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
