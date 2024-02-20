import cv2
import requests
from io import BytesIO
import numpy as np

# URL of the Flask server
flask_url = "http://127.0.0.1:8080/video_feed"

def show_video():
    
    while True:
        
        # Request video stream from Flask server
        response = requests.get(flask_url, stream=True)
        print(response)
        if not response.ok:
            
            print("Error receiving video stream")
            break
        
        # Read the frame as an image
        
        image_bytes = BytesIO(response.content) #ติด
        print("sjfkljdsjklsajfd")
        frame = cv2.imdecode(np.frombuffer(image_bytes.read(), np.uint8), -1)
       
        # Display the frame
        cv2.imshow("Video Stream", frame)
        
        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    show_video()