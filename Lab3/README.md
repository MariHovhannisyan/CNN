<h1 align="center"><strong>YOLOv8 Object Detection: Training, Evaluation & Demo App</strong></h1>

---

<h2 align="center"><strong>1. Model and Dataset</strong></h2>

This project uses the <strong>YOLOv8</strong> architecture for object detection, trained on the <strong>PASCAL VOC 2012</strong> dataset.

- <strong>Model file:</strong> [best.pt](https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/best.pt)
- <strong>Dataset:</strong> PASCAL VOC 2012  
  - 20 object categories  
  - Used for detection, localization, and classification

---

<h2 align="center"><strong>2. Training Results: Loss & Accuracy Curves</strong></h2>

<p align="center">
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/generated_images/loss.png" width="650"><br>
  <em>YOLOv8 Loss Curves (Box & Class, Train/Val)</em>
</p>

<p align="center">
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/generated_images/accuracy.png" width="750"><br>
  <em>YOLOv8 Accuracy & Metric Curves (Precision, Recall, mAP@0.5, mAP@0.5:0.95)</em>
</p>

- **Loss Curves:** Track box/class loss for train and val sets to show convergence and spot overfitting/underfitting.
- **Accuracy Curves:** 
  - <strong>Precision</strong>, <strong>Recall</strong>
  - <strong>mAP@0.5</strong> (best: <b>0.760</b> at epoch 17)
  - <strong>mAP@0.5:0.95</strong> (best: <b>0.497</b> at epoch 83)

---

<h2 align="center"><strong>Experimenting with Hyperparameters</strong></h2>

To achieve higher accuracy and address **overfitting**, we experimented with various hyperparameters (learning rate, batch size, optimizer, data augmentation, etc.).  
Below are the loss and accuracy curves **before** and **after** the hyperparameter improvements:

<p align="center">
  <b>Before Hyperparameter Tuning:</b><br>
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/images/Before.png" width="650"><br>
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/generated_images/Experiment_Loss.png" width="650"><br>
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/generated_images/Experiment_Accuracy.png" width="750"><br>
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/generated_images/Experiment_Random.png" width="750"><br>
<em>
    Before tuning, the model suffered from high validation loss and unstable metrics, indicating possible overfitting and poor generalization.
    <br>
    Detection results were also unreliable: as seen above, the bounding boxes are often inaccurate or duplicate, showing poor object localization and class confidence due to suboptimal hyperparameters.
  </em>
</p>

<p align="center">
  <b>After Hyperparameter Tuning:</b><br>
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/images/After.png" width="650"><br>
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/generated_images/After_Random.png" width="650"><br>
  <em>
    After improvements, loss curves became smoother and validation metrics improved, showing better generalization and less overfitting.
    <br>
    Detection results also became much more accurate: bounding boxes are now tighter and more precise, correctly identifying objects with higher confidence and fewer duplicates, reflecting stronger model performance after tuning.
  </em>
</p>

- <strong>Key changes:</strong>
  - Adjusted learning rate and batch size
  - Switched optimizer (e.g., SGD)
  - Added strong data augmentation (mosaic, mixup, flip, etc.)
  - Increased patience and training epochs

---

<h2 align="center"><strong>3. Benchmark Comparison</strong></h2>

<p align="center">
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/generated_images/Benchmark.png" width="550"><br>
  <em>My Results vs Community Benchmark</em>
</p>

- <strong>mAP@0.5:</strong> <b>0.760</b> (within typical YOLOv8s range: 0.70–0.80)
- <strong>mAP@0.5:0.95:</strong> <b>0.497</b> (within typical YOLOv8s range: 0.50–0.57)

---
<h2 align="center"><strong>4. Running the Demo App</strong></h2>

<strong>You can choose between two input sources:</strong>
- <strong>Webcam</strong>: Run detection live on your camera.
- <strong>Video File</strong>: Upload and process a video (e.g., mp4).

<p align="center">
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/images/Option.png" ><br>
</p>

<p align="center">
  <b>Example: Detection via Video File</b><br>
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/images/VideoFile.png" width="1150" ><br>
  <em>Sample video detection output—bounding boxes and class labels appear on every frame.</em>
</p>

<p align="center">
  <b>Example: Detection via Webcam</b><br>
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/images/WebCam.png" width="1150" ><br>
  <em>Sample webcam detection output—run real-time detection on your own camera feed.</em>
</p>

<p align="center">
  <b>Terminal Output During Webcam Detection</b><br>
  <img src="https://github.com/MariHovhannisyan/CNN/blob/master/Lab3/images/Terminal.png" width="550" ><br>
  <em>The terminal shows inference speed, frame details, and detected objects in real time while running webcam detection.</em>
</p>

<h2 align="center"><strong>5. How to use this project</strong></h2>

1. **Clone this repository to your local machine:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Download or place the trained model weights:**
    - Ensure the file `best.pt` (your trained YOLOv8 weights) is in the same folder as `app.py`.

3. **Install dependencies:**
    ```bash
    pip install streamlit ultralytics opencv-python
    ```

4. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
   

![Demo](/Users/admin/Desktop/CNN/Video-ezgif.com-optimize.gif)
