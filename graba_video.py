import cv2
captura= cv2.VideoCapture(0)
salida=cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
# nombre de video ,comando de escritura de video fps, tamaño de video
while(captura.isOpened()):
    ret,imagen=captura.read()
    #ret: booleano true o falte(cuando no se hizo la captura)
    if ret==True:
        cv2.imshow('video',imagen)
        #cv2.inshor('video',imagen)
        #if cv2.waitKey(1):
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        
captura.release()
salida.release()
cv2.destroyAllWindows()
            