from pprint import pprint

from low_png.image import PngImage


if __name__ == "__main__":
    img = PngImage("resources/png-tiny.png")
    chunks = img.chunks()

    for chunk in chunks:
        print(chunk.type)
