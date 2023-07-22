from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"  # folder for unedited images
pathOut = "./editedImgs"  # folder for edited images

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # Image Enhancements
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.2)  # Increase brightness by 20%

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)  # Increase contrast by 50%

    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.2)  # Increase color saturation by 20%

    # Additional Filters
    img = img.filter(ImageFilter.SHARPEN)

    # Resize the image (optional)
    img = img.resize((img.width // 2, img.height // 2))

    # Save the edited image
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{pathOut}/{clean_name}_edited.jpg')
