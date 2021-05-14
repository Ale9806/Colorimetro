import cv2
import numpy as np
import time
import ImageSpaceConvertor as isc

#### SFTP 
print("Initatating ColorSpace-Protocol-beta")
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)   # Use External Camara

while cap.isOpened():       # Loop till Camara is opened

    ret,frame = cap.read()  # Read Frame
    
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # Convert image to Gray
    img = cv2.medianBlur(img,5)                   # Blur Image
    H,W = img.shape                               # get shape
    img2= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)   # Convert image to RGB
    
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=50,maxRadius=55)  # Find Circles

    ### There may be times that the circle might no be there, therefore, we should add a try and excpet
    try:
      circles = np.uint16(np.around(circles))
      for i in circles[0,:]:  
        x =    i[0]       
        y =    i[1]    
        r =    i[2]                
        cv2.circle(frame,(x,y),r,(0,255,0),2)           
        cv2.circle(frame,(x,y),2,(0,0,255),2)   

        rgb = np.array([img2[x,y,0],img2[x,y,1],img2[x,y,2]],np.uint8)
        RGB = np.around(isc.Regularize(rgb),decimals=3)

        try:
          HSV  = np.around(isc.RGB2HSV(RGB),decimals=3)
        except:
          HSV  = -1
            
        try:
          YIQ  = np.around(isc.RGB2YIQ(RGB),decimals=3)
        except:
          YIQ  = -1
        
        try:
          XYZ = np.around(isc.RGB2XYZ(RGB),decimals=3)
     
        except:
          XYZ  = -1

        try:
          LAB = np.around(isc.RGB2LAB(RGB),decimals=3)

        except:
          LAB  = -1

        try:
          HSI = np.around(isc.RGB2HSI(RGB),decimals=3)
         
        except:
          HSI  = -1
        
        
        ##### BOX ####
        ## Status BOX ##
        cv2.rectangle(frame,(0,0),(160,H),(255,255,255),-1)
        cv2.rectangle(frame,(0,0),(160,H),(0,0,0),1)
        ## Display Class Agian ##
        cv2.putText(frame,"RGB",(30,20),font,0.5,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(frame,str(RGB),(0,40),font,0.4,(0,0,0),1,cv2.LINE_AA)

        cv2.putText(frame,"HSV",(30,80),font,0.5,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(frame,str(HSV),(0,100),font,0.4,(0,0,0),1,cv2.LINE_AA)

        cv2.putText(frame,"YIQ",(30,140),font,0.5,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(frame,str(YIQ),(0,160),font,0.4,(0,0,0),1,cv2.LINE_AA)

        cv2.putText(frame,"XYZ",(30,200),font,0.5,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(frame,str(XYZ),(0,220),font,0.4,(0,0,0),1,cv2.LINE_AA)

        cv2.putText(frame,"LAB",(30,260),font,0.5,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(frame,str(LAB),(0,280),font,0.4,(0,0,0),1,cv2.LINE_AA)

        cv2.putText(frame,"HSI",(30,320),font,0.5,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(frame,str(HSI),(0,340),font,0.4,(0,0,0),1,cv2.LINE_AA)


     

       
      
            
      

    except:
      pass

    cv2.imshow("Pose Detection",frame)

    if cv2.waitKey(10) & 0xFF == ord('s'):
      time.sleep(10)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break