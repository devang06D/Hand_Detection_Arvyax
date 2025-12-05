import cv2
import numpy as np

W, H = 640, 480
center_x, center_y = 320, 240

box_w, box_h = 180, 180                  
buffer = 35                               

half_w = box_w // 2
half_h = box_h // 2

#red box
left   = center_x - half_w
right  = center_x + half_w
top    = center_y - half_h
bottom = center_y + half_h

# warning zone 
warn_left   = left - buffer
warn_right  = right + buffer
warn_top    = top - buffer
warn_bottom = bottom + buffer
# 

cap = cv2.VideoCapture(0)
cap.set(3, W)
cap.set(4, H)

ret, frame = cap.read()
if not ret:
    print("Can't open camera")
    exit()

prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
prev_gray = cv2.GaussianBlur(prev_gray, (9,9), 0)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    frame = cv2.flip(frame, 1)
    img = frame.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9,9), 0)

    
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, _ = cv2.cartToPolar(flow[...,0], flow[...,1])
    motion = (mag > 1.6).astype(np.uint8) * 255

    ycc = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    skin = cv2.inRange(ycc, (0, 133, 77), (255, 180, 135))
    
    mask = cv2.bitwise_and(motion, skin)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((16,16)))
    mask = cv2.dilate(mask, None, iterations=5)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    state = "SAFE"
    tips = []

    if contours:
        hand = max(contours, key=cv2.contourArea)
        
        if cv2.contourArea(hand) > 7000:
            cv2.drawContours(img, [hand], -1, (70, 200, 70), 2)

            # for fingertips
            hull = cv2.convexHull(hand, returnPoints=False)
            defects = cv2.convexityDefects(hand, hull)
            
            if defects is not None:
                for i in range(defects.shape[0]):
                    s,e,f,d = defects[i,0]
                    if d > 13000:
                        far = tuple(hand[f][0])
                        tips.append(far)
                        cv2.circle(img, far, 12, (255, 180, 0), -1)
                        cv2.circle(img, far, 16, (255, 100, 0), 4)

            
            pts = hand.reshape(-1, 2)
            x, y = pts[:,0], pts[:,1]

            
            in_danger = ((x > left) & (x < right) & (y > top) & (y < bottom)).sum()
            in_warning = ((x > warn_left) & (x < warn_right) & 
                         (y > warn_top) & (y < warn_bottom)).sum()

            if in_danger > 20:
                state = "DANGER"
            elif in_warning > 30:
                state = "WARNING"

            
            for tx, ty in tips:
                if left < tx < right and top < ty < bottom:
                    state = "DANGER"
                    break
                elif warn_left < tx < warn_right and warn_top < ty < warn_bottom:
                    if state != "DANGER":
                        state = "WARNING"

    
    cv2.rectangle(img, (warn_left, warn_top), (warn_right, warn_bottom), (0, 255, 255), 5)

    
    box_color = (0, 0, 255)
    box_thick = 10 if state == "DANGER" else 8
    cv2.rectangle(img, (left, top), (right, bottom), box_color, box_thick)

    
    glow = frame.copy()
    cv2.rectangle(glow, (left, top), (right, bottom), (0, 0, 255), -1)
    alpha = 0.6 if state == "DANGER" else 0.35 if state == "WARNING" else 0.1
    cv2.addWeighted(glow, alpha, img, 1-alpha, 0, img)

    
    font = cv2.FONT_HERSHEY_DUPLEX
    if state == "DANGER":
        txt, col, scale, th = "DANGER", (0, 0, 255), 4.2, 14
    elif state == "WARNING":
        txt, col, scale, th = "WARNING", (0, 255, 255), 3.8, 11
    else:
        txt, col, scale, th = "SAFE", (0, 255, 100), 3.5, 10

    size = cv2.getTextSize(txt, font, scale, th)[0]
    x = (W - size[0]) // 2
    y = H - 60

    cv2.putText(img, txt, (x, y), font, scale, (255, 255, 255), th + 16)
    cv2.putText(img, txt, (x, y), font, scale, col, th)

    cv2.imshow("Hand Safety Zone", img)
    prev_gray = gray.copy()

    if cv2.waitKey(1) == 27:  
        break

cap.release()
cv2.destroyAllWindows()