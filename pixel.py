from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Encrypt by shifting RGB values with the key
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Decrypt by reversing the shift
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Example usage:
if __name__ == "__main__":
    original_image = "input.jpg"     # Replace with your image file
    encrypted_image = "encrypted.png"
    decrypted_image = "decrypted.png"
    key = 50  # Choose an integer as key

    encrypt_image(original_image, encrypted_image, key)
    decrypt_image(encrypted_image, decrypted_image, key)
