import cv2 

cap=cv2.VideoCapture(1,cv2.CAP_V4L2)

if not cap.isOpened():
    print('Error')
    exit()
    
w=round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h=round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps=cap.get(cv2.CAP_PROP_FPS)

forc=cv2.VideoWriter_fourcc(*'DIVX')
#forc=cv2.VideoWriter_Fourcc(*'DIVX')
delay=round(1000/fps)
out=cv2.VideoWriter('output1.avi',forc,fps,(w,h))



while True:
    ret,frame=cap.read()
    
    if not ret:
        cap.release()
        break
    inversed=~frame
    edge=cv2.Canny(frame,50,150)
    edge_color=cv2.cvtColor(edge,cv2.COLOR_GRAY2BGR)
    out.write(frame) 
    cv2.imshow('video',frame)
    cv2.imshow('inversed',inversed)
    cv2.imshow('edge',edge)
    
    #cv2.imshow('video',~frame)
    if cv2.waitKey(delay)==ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
    
    