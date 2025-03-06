# Usage Instructions

## Prepare Training Data:

- Create a directory (e.g., known_faces) with subdirectories named after each person (e.g., Duke, Charles).

- Place images of each person in their respective subdirectory.

## Run the Script:

- Execute the script from the command line with the required arguments:

```bash
python face_recognition_tool.py --train known_faces --input test_image.jpg --output result.jpg
```

## Output:

- The processed image (result.jpg) will have bounding boxes and labels for recognized faces.

## Conclusion

- This tool detects faces in an image, recognizes them based on the provided training data, and outputs the result with labeled bounding boxes. Adjust the distance threshold (0.6) as needed for recognition accuracy.