from image import PngImage


if __name__ == "__main__":
    img = PngImage("lena.png")
    chunk = img.next_chunk()
