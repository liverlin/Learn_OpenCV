import cv2
import numpy as np

#bgr=np.zeros((300,300,3),dtype=np.uint8) negro
bgr=np.zeros((300,300,3),dtype=np.uint8) 
#Defino una matriz de 3D con puros ceros
bgr[:,:,:]=[255,255,0] #Azul
cv2.imshow('BGR',bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()