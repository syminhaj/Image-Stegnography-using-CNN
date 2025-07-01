from PIL import Image
import numpy as np
from google.colab import files
import os

def xor_encrypt_decrypt(message, key):
    return ''.join(chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(message))

def encode_message_in_image(image_path, message, output_path, key):
    try:
        image = Image.open(image_path).convert("RGB")
        np_image = np.array(image).astype(np.uint8)

        encrypted_message = xor_encrypt_decrypt(message, key) + '\0'
        binary_message = ''.join(format(ord(char), '08b') for char in encrypted_message)

        flat_pixels = np_image.flatten()

        if len(binary_message) > len(flat_pixels):
            raise ValueError("Message is too large to hide in this image!")

        for i, bit in enumerate(binary_message):
            flat_pixels[i] = int((int(flat_pixels[i]) & ~1) | int(bit))

        encoded_image = flat_pixels.reshape(np_image.shape)
        Image.fromarray(encoded_image).save(output_path, format="PNG")
        print(f"Message successfully encoded in '{output_path}'")

    except Exception as e:
        print("Encoding Error:", e)

def decode_message_from_image(image_path, key):
    try:
        image = Image.open(image_path).convert("RGB")
        np_image = np.array(image)

        flat_pixels = np_image.flatten()
        binary_message = ''

        for i in range(0, len(flat_pixels), 8):
            byte = ''
            for j in range(8):
                if i + j < len(flat_pixels):
                    byte += str(flat_pixels[i + j] & 1)
            char = chr(int(byte, 2))
            if char == '\0':
                break
            binary_message += char

        decrypted_message = xor_encrypt_decrypt(binary_message, key)
        print("Decrypted message:", decrypted_message)

    except Exception as e:
        print("Decoding Error:", e)

print("Please upload your image file (PNG recommended)")
uploaded = files.upload()
image_filename = next(iter(uploaded))

while True:
    print("\nImage Steganography Menu:")
    print("1. Encode a message")
    print("2. Decode a message")
    choice = input("Enter your choice (1 for Encode, 2 for Decode): ")

    if choice == '1':
        message = input("Enter the message to hide: ")
        output_filename = input("Enter output image filename (use .png): ")
        key = input("Enter encryption key: ")
        encode_message_in_image(image_filename, message, output_filename, key)

        if os.path.exists(output_filename):
            print("Downloading encoded image...")
            files.download(output_filename)

    elif choice == '2':
        key = input("Enter decryption key: ")
        decode_message_from_image(image_filename, key)

    else:
        print("Invalid choice! Enter 1 or 2.")

    if input("Perform another operation? (yes/no): ").lower() != 'yes':
        print("Exiting...")
        break
