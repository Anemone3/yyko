

## Image utils

from PIL import Image
from io import BytesIO

some_image = BytesIO()
img = Image.open(some_image)
width, height = img.size


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


divisor = gcd(width, height)
aspect_ratio = f"{width // divisor}:{height // divisor}"
print(aspect_ratio)
