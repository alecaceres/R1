#https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
import cv2 as cv

cap = cv.VideoCapture(0)
# Definir CODEC y confirar tamaño de frame del objeto
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)

fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('output.avi', fourcc, 20.0, size)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # frame = cv.flip(frame, 0)
    # write the flipped frame
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()