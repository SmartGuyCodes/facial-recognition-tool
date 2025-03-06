# Step-by-Step Explanation

## 1. Install Required Libraries:

 - Install face_recognition, numpy, and Pillow using pip:

```bash
pip install face-recognition numpy Pillow
```

## 2. Set Up Command-Line Arguments:

- Use argparse to accept the training directory, input image, and output image paths.

## 3. Load Known Faces:

- Read images from subdirectories in the training directory. Each subdirectory represents a person's name and contains their images.

- Extract face encodings from these images and store them with corresponding labels.

## 4. Process Input Image:

- Detect faces and compute their encodings in the input image.

## 5. Recognize Faces:

- Compare each detected face's encoding with known encodings to find the closest match using a distance threshold.

## 6. Draw Bounding Boxes and Labels:

- Use Pillow to draw bounding boxes around detected faces and label them with recognized names or "Unknown".