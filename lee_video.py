import cv2
#captura= cv2.VideoCapture('videoSalida.avi')
captura= cv2.VideoCapture('marcianito.mp4')
while(captura.isOpened()):
    ret,imagen=captura.read()
    #ret: booleano true o falte(cuando no se hizo la captura)
    if ret==True:
        cv2.imshow('video',imagen)
        
        if cv2.waitKey(30) & 0xFF == ord('s'):
            #Se puede subir el wait key para visuaizar más rapido el video
            break
    else:
        #Para salir cuando acabe el video
        break
        
captura.release()
#Open cv busca procesar el video lo más rapído posible

cv2.destroyAllWindows()