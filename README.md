# UPC-A Barcode Generator

This Python project generates UPC-A barcodes and enhances the images using the Pillow library. Customize your barcode by providing a 12-digit numeric string, and get an image output of the barcode.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Details](#project-details)
- [Enhancements](#enhancements)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/barcode-generator.git
   cd barcode-generator
   ```

2. **Install required packages:**

   Ensure you have Python installed, then install dependencies with pip:

   ```bash
   pip install upcean Pillow
   ```

## Usage

### Generate Barcode

To generate a UPC-A barcode, edit the `my_numbers` variable with your desired 12-digit number in the Python script.

```python
my_numbers = "123456789012"  # EDIT YOUR DIGITS HERE
```

### Run the Script

Execute the script to create and save the barcode:

```bash
python create_barcode.py
```

The script will produce two outputs:

1. **IMAGE.png** - The raw barcode image.
2. **RESIZED_IMAGE.png** - The enhanced barcode image with increased resolution and clarity.

## Project Details

- **Input:** 12-digit numeric string for generating a valid UPC-A barcode.
- **Libraries Used:**
  - `upcean`: For barcode creation and validation.
  - `Pillow`: For image processing tasks such as resizing, sharpening, and enhancing contrast and brightness.

## Enhancements

- **Resizing:** High-quality resampling using `Image.LANCZOS`.
- **Sharpening:** Image clarity improved using `ImageFilter.SHARPEN`.
- **Contrast and Brightness:** Fine-tuned using `ImageEnhance.Contrast` and `ImageEnhance.Brightness`.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with any enhancements, bug fixes, or additional features.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute as needed.

---

For any queries or issues, please contact me via email or open an issue on GitHub. Happy coding!
