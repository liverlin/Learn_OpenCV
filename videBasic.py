import cv2

#Visualizar por camara
captura= cv2.VideoCapture(0)
salida=cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
while(captura.isOpened()):
    ret,imagen=captura.read()
    #ret: booleano true o falte(cuando no se hizo la captura)
    if ret==True:
        cv2.imshow('video',imagen)
        #cv2.inshor('video',imagen)
        #if cv2.waitKey(1):
        if cv2.waitKey(1) & 0xFF == ord('s'):
            #s tecla para detener el procesamiento
            #0xFF recomendado cuando trabajemos con una maquina de 64 bits
            break
        
captura.release()
#Para finalizar captura
cv2.destroyAllWindows()
#Para cerrar cualquier ventana abierta


