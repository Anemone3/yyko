"""
    Crea un programa que se encargue de calcular el aspect ratio de una
    imagen a partir de una url.
    - Url de ejemplo:
    https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
    - Por ratio hacemos referencia por ejemplo a los "16:9" de una
    imagen de 1920*1080px.


    Solución:
    https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge5.kt
"""


def get_aspect_ratio(url: str) -> str:
    from PIL import Image
    import requests
    from io import BytesIO

    response = requests.get(url)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    width, height = img.size

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    divisor = gcd(width, height)
    aspect_ratio = f"{width // divisor}:{height // divisor}"
    return aspect_ratio


print(get_aspect_ratio(
    "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
))