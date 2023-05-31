import cv2

mifoto = cv2.imread('josevicente.jpg')
gris = cv2.cvtColor(mifoto, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original',mifoto)
cv2.imshow('Gris', gris)
