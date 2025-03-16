import upcean
from PIL import Image, ImageFilter, ImageEnhance

def generate_upca_with_string(my_numbers):
    # Check if digits have the correct length
    if len(my_numbers) != 12 or not my_numbers.isdigit():
        raise ValueError("Provided digits must be a 12-digit numeric string.")
    
    return my_numbers

try:
    # EDIT DIGITS HERE!!!!!
    my_numbers = "123456789012"
    
    # Generate a UPC-A number with the digits
    valid_upca_number = generate_upca_with_string(my_numbers)
    print(f"Using UPC-A Number: {valid_upca_number}")

    # Create a barcode object
    barcode = upcean.oopfuncs.barcode('upca', valid_upca_number)

    # Validate the barcode number
    is_valid = barcode.validate_checksum()
    print(f"Checksum Valid: {is_valid}")

    if is_valid:
        # Generate the barcode image
        barcode.create_barcode(filename="./IMAGE.png")
        print("Barcode image created successfully at './IMAGE.png'.")

        # Open the generated image using Pillow
        img = Image.open('./IMAGE.png')

        # Resize the barcode image with high-quality resampling
        large_img_size = (441, 306)
        resized_img = img.resize(large_img_size, Image.LANCZOS)

        # Apply sharpening to enhance clarity on the resized image
        sharpened_img = resized_img.filter(ImageFilter.SHARPEN)

        # Adjust brightness and contrast as needed
        enhancer = ImageEnhance.Contrast(sharpened_img)
        contrast_enhanced_img = enhancer.enhance(1.5)

        enhancer = ImageEnhance.Brightness(contrast_enhanced_img)
        brightened_img = enhancer.enhance(1.2)  # Adjust brightness factor as needed

        # Save the final cleaned image with higher DPI for better quality
        brightened_img.save('./RESIZED_IMAGE.png', dpi=(300, 300))
        print("Resized, sharpened, and enhanced barcode image saved at './RESIZED_IMAGE.png'.")

        # Show the resized, sharpened, and enhanced image
        brightened_img.show()
    else:
        print("The provided barcode number is invalid.")

except Exception as e:
    print(f"An error occurred: {e}")
