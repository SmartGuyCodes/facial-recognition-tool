# Face Recognition Tool

A Python-based tool to detect and recognize faces in images using machine learning. Built with `face_recognition`, `Pillow`, and `argparse`.

![Example Output](output/result.jpg) *(Example output with bounding boxes and labels)*

---

## Features
- **Face Detection**: Locate faces in an image.
- **Face Recognition**: Match detected faces to known individuals using ML encodings.
- **CLI Support**: Configure via command-line arguments.
- **Bounding Boxes & Labels**: Annotate results with Pillow.

---

## Installation

### Prerequisites
- Python 3.6+
- `pip` or `pip3`

### Steps
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install face-recognition numpy Pillow
   ```
   or for Python 3.x:
   ```bash
   pip3 install face-recognition numpy Pillow
   ```

---

## Usage

### Command-Line Syntax
```bash
python face_recognition_tool.py \
  --train [TRAINING_DATA_DIR] \
  --input [INPUT_IMAGE_PATH] \
  --output [OUTPUT_IMAGE_PATH]
```

### Example
```bash
python face_recognition_tool.py \
  --train known_faces \
  --input input/test.jpg \
  --output output/result.jpg
```

### Training Data Structure
- Create a directory (e.g., `known_faces`) with subfolders named after each person.
- Place images of each person in their respective subfolder:

```
  known_faces/
  ├── Duke/
  │   ├── duke1.jpg
  │   └── duke2.jpg
  └── Og/
      ├── ogego1.jpg
      └── ogego2.jpg
  ```

---

## File Structure

```
project_root/
├── known_faces/       # Training images
├── input/             # Test images
├── output/            # Annotated results
├── face_recognition_tool.py  # Main script
└── requirements.txt   # Dependencies (optional)
```

---

## Dependencies
- `face-recognition`: Face detection and encoding.
- `Pillow`: Image processing and bounding boxes.
- `argparse`: Command-line argument parsing.

---

## Notes
- **Threshold Adjustment**: Modify the `0.6` distance threshold in the code for stricter/looser matches.
- **Performance**: Works best with front-facing, well-lit faces.
- **Training Images**: Use multiple images per person for better accuracy.

---

License: MIT  