from PIL import Image
import time


def generate_n():
    # Generate the number n using the provided algorithm
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50
    if generated_number % 2 == 0:
        generated_number += 10
    return generated_number


def process_image(input_image_path, output_image_path):
    # Load the image
    image = Image.open(input_image_path)
    pixels = image.load()
    width, height = image.size

    # Generate number n
    n = generate_n()

    # Create a new image to store the modified pixels
    new_image = Image.new('RGB', (width, height))
    new_pixels = new_image.load()

    # Initialize red sum
    red_sum = 0

    # Modify pixels
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Modify the pixel values
            new_r = min(255, r + n)  # Ensure the value doesn't exceed 255
            new_g = min(255, g + n)  # Ensure the value doesn't exceed 255
            new_b = min(255, b + n)  # Ensure the value doesn't exceed 255
            # Assign to the new image
            new_pixels[x, y] = (new_r, new_g, new_b)
            # Add to red_sum
            red_sum += new_r

    # Save the new image
    new_image.save(output_image_path)

    # Print the sum of red values
    print(f"Sum of all red pixel values: {red_sum}")


# Usage
input_image_path = 'chapter1.jpg'  # Path to the input image
output_image_path = 'chapter1out.png'  # Path to save the output image
process_image(input_image_path, output_image_path)
print("https://github.com/Rahman421-star/Assignment-2")