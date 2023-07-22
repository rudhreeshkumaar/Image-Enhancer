# Image Enhancemer

This Python script uses the `Pillow` library to perform various image enhancements on images present in the specified folder. It applies a series of enhancements to each image and saves the edited images in a separate folder.

## Prerequisites

Before running the script, make sure you have the `Pillow` library installed. You can install it using `pip`:

```
pip install Pillow
```

## Configuration

1. Create two folders in the same directory as the script: `imgs` and `editedImgs`.
2. Place the images you want to enhance in the `imgs` folder.

## Usage

1. Save the script in a Python file, e.g., `image_enhancer.py`.
2. Place the images you want to enhance in the `imgs` folder.
3. Execute the script in your preferred Python environment.

## Script Description

1. The script imports necessary functions from the `Pillow` library.
2. It sets the `path` variable to the path of the folder containing the unedited images (`imgs`).
3. It sets the `pathOut` variable to the path of the folder where the edited images will be saved (`editedImgs`).
4. The script iterates through all the files in the `imgs` folder using `os.listdir(path)`.
5. For each image, it performs the following image enhancements:
   - **Brightness Enhancement**: Increases the brightness of the image by 20% using the `ImageEnhance.Brightness` function.
   - **Contrast Enhancement**: Increases the contrast of the image by 50% using the `ImageEnhance.Contrast` function.
   - **Color Saturation Enhancement**: Increases the color saturation of the image by 20% using the `ImageEnhance.Color` function.
   - **Additional Filters**: Applies the sharpening filter using the `ImageFilter.SHARPEN` filter to further enhance image details.
   - **Resizing (Optional)**: Resizes the edited image to half of its original size using the `resize()` method. This step is optional and can be adjusted based on your preference.
6. The edited image is saved in the `editedImgs` folder with the filename format: `<clean_name>_edited.jpg`, where `<clean_name>` is the name of the original image without the file extension.

## Note

- The script applies various enhancements to improve the image quality and details.
- You can modify the enhancement values or add more enhancements based on your specific requirements. The [Pillow documentation](https://pillow.readthedocs.io/en/stable/) provides a comprehensive list of available enhancements and filters that you can explore and experiment with.
- Ensure that the `Pillow` library is correctly installed and compatible with your Python environment.
- The script will overwrite existing edited images with the same name. Make sure to back up any important files before running the script.

Enjoy using this enhanced image editing script to improve your images with ease!
