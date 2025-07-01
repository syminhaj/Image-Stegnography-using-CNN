
---

## 🔍 Overview of Components

### 1. `steganography_lsb.py` - 🔐 **LSB Steganography with XOR Encryption**
This script provides a **menu-driven command-line tool** that allows users to:
- **Encrypt** a secret message using a custom XOR key.
- **Embed** the encrypted message into the least significant bits (LSB) of an image.
- **Extract** and **decrypt** the hidden message from an image.
- Works seamlessly with Google Colab's `files.upload()` and `files.download()`.

✅ **Key Features**:
- LSB image manipulation using NumPy and PIL.
- XOR-based encryption for lightweight security.
- Error handling for image size limits.

---

### 2. `visualize_differences.py` - 🔍 **Image Difference Visualizer**
This module visualizes pixel-level changes between the original and encoded images:
- Computes **absolute pixel differences** across RGB channels.
- Produces a **heatmap** using Matplotlib to show the impact of encoding.
- Useful for visually validating where the message bits were embedded.

✅ **Use Cases**:
- Visual validation of steganographic changes.
- Debugging message embedding accuracy.

---

### 3. `cnn_feature_extractor.py` - 🤖 **CNN-Based Feature Map Extractor**
This script uses a custom-built `SimpleCNN` to:
- Extract and visualize **intermediate convolutional feature maps**.
- Show how a neural network interprets stego vs. original images.
- Saves the **averaged convolutional map** as a new image for further analysis.

✅ **Educational Insight**:
- Understand internal CNN behavior for image classification tasks.
- A stepping stone toward stego-detection using deep learning.

---

### 4. `plot_message_vs_pixels.py` - 📊 **Scatter Plot for Message vs Pixel Changes**
This script uses Seaborn and Matplotlib to:
- Plot **message length vs. number of altered pixels**.
- Understand the **relationship between data payload and image distortion**.
- Simulate scalability and capacity of LSB encoding.

✅ **Why It Matters**:
- Helps estimate how much data can safely be embedded.
- Useful for designing capacity-aware steganographic systems.

---

## 📚 Requirements

Install the following libraries before running the code:

```bash
pip install numpy pillow matplotlib seaborn torch torchvision
