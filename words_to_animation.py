import cv2

def play_video(filename):
    cap = cv2.VideoCapture(filename)
    ret, frame = cap.read()
    while(1):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        if(cv2.waitKey(5) & 0xFF == ord('q') or ret==False):
            cap.release()
            cv2.destroyAllWindows()
            break
        cv2.imshow('frame',frame)
play_video("C:/Users/Pravallika Myneni/Desktop/Work/Personal-Projects/Speech_to_ASL/assets/God.mp4")