import argparse
import os
import numpy as np
import face_recognition
from PIL import Image, ImageDraw

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Recognize faces in an image.')
    parser.add_argument('--train', required=True, help='Path to the training directory with subfolders named after each person.')
    parser.add_argument('--input', required=True, help='Path to the input image for face recognition.')
    parser.add_argument('--output', required=True, help='Path to save the output image with bounding boxes.')
    args = parser.parse_args()

    # Load known faces and their encodings
    known_encodings = []
    known_names = []

    for name in os.listdir(args.train):
        person_dir = os.path.join(args.train, name)
        if os.path.isdir(person_dir):
            for image_file in os.listdir(person_dir):
                image_path = os.path.join(person_dir, image_file)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                if len(encodings) > 0:
                    known_encodings.append(encodings[0])
                    known_names.append(name)

    # Load input image
    input_image = face_recognition.load_image_file(args.input)
    face_locations = face_recognition.face_locations(input_image)
    face_encodings = face_recognition.face_encodings(input_image, face_locations)

    # Convert to PIL image for drawing
    pil_image = Image.fromarray(input_image)
    draw = ImageDraw.Draw(pil_image)

    # Process each face in the input image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "Unknown"
        if known_encodings:
            # Calculate distances to known faces
            distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(distances)
            if distances[best_match_index] <= 0.6:
                name = known_names[best_match_index]

        # Draw bounding box
        draw.rectangle([left, top, right, bottom], outline=(0, 255, 0), width=2)

        # Draw label
        text_width, text_height = draw.textsize(name)
        draw.rectangle(
            [left, bottom - text_height - 10, left + text_width, bottom],
            fill=(0, 255, 0),
            outline=(0, 255, 0)
        )
        draw.text(
            (left + 6, bottom - text_height - 5),
            name,
            fill=(0, 0, 0)
        )

    # Save the output image
    pil_image.save(args.output)
    print(f"Result saved to {args.output}")

if __name__ == "__main__":
    main()