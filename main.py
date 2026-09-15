import argparse
from pathlib import Path
import cv2

from cv_modules.preprocessing import load_image, resize_image, crop_image, rotate_image, grayscale
from cv_modules.enhancement import gaussian_blur, median_blur, sharpen, binary_threshold
from cv_modules.edge_detection import canny_edges
from cv_modules.shape_detection import detect_shapes
from cv_modules.statistics import image_statistics

OPERATIONS = {"grayscale", "resize", "crop", "rotate", "gaussian", "median", "sharpen", "threshold", "edges", "shapes", "stats"}


def parse_args():
    parser = argparse.ArgumentParser(description="Basic image processing and shape detection")
    parser.add_argument("--image", required=True, help="Path to an image")
    parser.add_argument("--operation", required=True, choices=sorted(OPERATIONS), help="Operation to perform")
    parser.add_argument("--output", default="output", help="Output directory")
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        image = load_image(args.image)
    except ValueError as error:
        print(f"Error: {error}")
        return 1
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    if args.operation == "stats":
        for key, value in image_statistics(image).items():
            print(f"{key}: {value}")
        return 0
    operations = {"grayscale": grayscale, "resize": resize_image, "crop": crop_image,
                  "rotate": rotate_image, "gaussian": gaussian_blur, "median": median_blur,
                  "sharpen": sharpen, "threshold": binary_threshold, "edges": canny_edges}
    if args.operation == "shapes":
        result, names = detect_shapes(image)
        print("Detected shapes:", ", ".join(names) if names else "none")
    else:
        result = operations[args.operation](image)
    destination = output_dir / f"{args.operation}.png"
    cv2.imwrite(str(destination), result)
    print(f"Saved result to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
