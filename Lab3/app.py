import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import os

st.title("YOLO Object Detection")

model_path = st.text_input("Path to your YOLO model (.pt):", "best.pt")
if not os.path.exists(model_path):
    st.warning(f"Model file '{model_path}' not found in {os.getcwd()}!")
    st.stop()
model = YOLO(model_path)

option = st.selectbox("Select Input Source:", ("Webcam", "Video File"))

if option == "Webcam":
    st.write("Click 'Start' to use your webcam for detection.")
    run_webcam = st.button("Start Webcam Detection")
    if run_webcam:
        cap = cv2.VideoCapture(0)
        stframe = st.empty()
        st.info("Press CTRL+C in the terminal to stop the webcam.")
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to grab frame from webcam.")
                break
            results = model(frame)
            annotated = results[0].plot()
            stframe.image(annotated, channels="BGR", caption=f"Webcam Frame {frame_count+1}")
            frame_count += 1
            if frame_count >= 100:
                st.info("Stopped after 100 frames (demo limit). Restart to continue.")
                break
        cap.release()
        cv2.destroyAllWindows()

elif option == "Video File":
    uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        tfile.write(uploaded_file.read())
        video_path = tfile.name
        st.video(video_path)
        if st.button("Run Detection"):
            cap = cv2.VideoCapture(video_path)
            stframe = st.empty()
            frame_count = 0
            while cap.isOpened() and frame_count < 100:
                ret, frame = cap.read()
                if not ret:
                    break
                results = model(frame)
                annotated = results[0].plot()
                stframe.image(annotated, channels="BGR", caption=f"Frame {frame_count+1}")
                frame_count += 1
            cap.release()
            st.success(f"Processed {frame_count} frames.")
            os.remove(video_path)