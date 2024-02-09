import cv2
from deepface import DeepFace

# Load the pre-trained models for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the webcam (you may need to change the index based on your system)
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 1
color = (255, 255, 255)  
thickness = 2

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    # print(faces)
    # For each detected face, perform face verification
    for (x, y, w, h) in faces:
        # Extract the detected face region
        face = frame[y:y + h, x:x + w]

        # Perform face verification
        try:
            # result = DeepFace.verify("./picture/pic4.jpg", face,model_name="VGG-Face", enforce_detection=False)
            result=DeepFace.analyze(face,actions=("gender"))
            # Print the result
            # print("Verification result:", result["verified"])
            # print("Distance:", result["distance"])
            # print("Model:", result["model"])
            # print(result[0]['dominant_emotion'])

            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            text_gender = f"Gender: {result[0]['dominant_gender']}"
            cv2.putText(frame, text_gender, (x, y + h + 40), font, fontScale, color, thickness, cv2.LINE_AA)
        except ValueError as e:
            print(f"Error: {e}")

    # Display the frame
    cv2.imshow('Face Verification', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()