import cv2

# Defining prototext and caffemodel paths
caffeModel = "C:/Users/robjl/Documents/Python Playground/Spotify Emotion Automator/spotifyEmotionAutomator/spotifyEmotionBasedRecommenderSystem/deploy.prototxt.txt"
prototextPath = "C:/Users/robjl/Documents/Python Playground/Spotify Emotion Automator/spotifyEmotionAutomator/spotifyEmotionBasedRecommenderSystem/res10_300x300_ssd_iter_140000.caffemodel"

# Load the pre-trained emotion detection model
emotion_model = cv2.dnn.readNetFromCaffe(prototextPath, caffeModel)

# Define the list of emotions
EMOTIONS = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

# Define a function to detect emotions from a frame
def detect_emotion(frame):
    # Resize the frame to the input size required by the model
    frame = cv2.resize(frame, (64, 64))
    frame = frame.astype("float") / 255.0
    frame = frame - 0.5
    frame = frame * 2.0

    # Pass the frame through the emotion detection model
    emotion_model.setInput(cv2.dnn.blobFromImage(frame))
    emotions = emotion_model.forward()

    # Get the emotion with the highest probability
    emotion_index = emotions[0].argmax()

    return EMOTIONS[emotion_index]

# Define a function to capture video from the camera
def capture_video():
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera

    while True:
        ret, frame = cap.read()

        # Detect emotion
        emotion = detect_emotion(frame)

        # Display the frame with the detected emotion
        cv2.putText(frame, emotion, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Emotion Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    capture_video()
