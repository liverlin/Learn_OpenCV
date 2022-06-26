import cv2
import numpy as np

print(cv2.__version__)

imagen=cv2.imread('frugos.jpg',0)
#1: a color por defecto
#Si le pongo 0 lo pasa a escala de grises
cv2.imshow('Prueba de imagen',imagen)

cv2.imwrite('grises.jpg',imagen)
#Guaradra la imagen, para este caso como escala de grises
cv2.waitKey(0)
# INdeterminadamente 
# 1000: prendido por 1 seg
cv2.destroyAllWindows()