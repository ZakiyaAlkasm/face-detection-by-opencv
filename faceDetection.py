import cv2

faces = cv2.CascadeClassifier("C://Users//Hard-Soft//PycharmProjects//OPENCV//venv//Lib//site-packages//cv2//data"
                              "//haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier("C://Users//Hard-Soft//PycharmProjects//OPENCV//venv//Lib//site-packages//cv2//data"
                              "//haarcascade_eye.xml")
im = cv2.imread("img/face.jpg")
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
F = faces.detectMultiScale(gray,1.3,5)
for (x, y, w, h) in F:
    im = cv2.rectangle(im, (x, y), (x+w,y+h),(255, 0, 0), 2)
    ro = gray[y:y+h,x:x+w]
    co = im[y:y+h:x+w]
    m = eye.detectMultiScale(ro)
    for (ex, ey, ew, eh) in m:
         cv2.rectangle(ro, (ex,ey), (ex+ew,ey+eh),(0, 255, 0), 2)
cv2.imshow('i', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
