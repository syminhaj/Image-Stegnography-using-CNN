import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def plot_image_changes(image_path, encoded_image_path, save_diff_path=None):
    original_image = np.array(Image.open(image_path).convert("RGB"))
    encoded_image = np.array(Image.open(encoded_image_path).convert("RGB"))

    if original_image.shape != encoded_image.shape:
        print("Resizing encoded image to match original image size.")
        encoded_image = np.array(Image.fromarray(encoded_image).resize(original_image.shape[1::-1]))

    difference = np.abs(original_image - encoded_image)
    diff_image = np.sum(difference, axis=2)

    max_val = diff_image.max()
    if max_val > 0:
        diff_image_normalized = (diff_image / max_val) * 255
    else:
        diff_image_normalized = diff_image
    diff_image_normalized = diff_image_normalized.astype(np.uint8)

    if save_diff_path:
        Image.fromarray(diff_image_normalized).save(save_diff_path)
        print(f"Difference image saved as '{save_diff_path}'")

    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    ax[0].imshow(original_image)
    ax[0].set_title("Original Image")
    ax[0].axis("off")
    ax[1].imshow(encoded_image)
    ax[1].set_title("Encoded Image")
    ax[1].axis("off")
    ax[2].imshow(diff_image_normalized, cmap='hot')
    ax[2].set_title("Difference Heatmap")
    ax[2].axis("off")
    plt.suptitle("LSB Steganography Visualization", fontsize=16)
    plt.tight_layout()
    plt.show()
