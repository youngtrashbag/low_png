from pprint import pprint
from pathlib import Path

from low_png.image import PngImage
from low_png.chunk import ChunkType

if __name__ == "__main__":
    img = PngImage(Path("resources/png-tiny.png"))
    chunks = img.chunks()

    for chunk in chunks:
        print(chunk.type)
        if chunk.type == ChunkType.IDAT.name:
            chunk.data[len(chunk.data)-1] += 1

    img.save(Path("resources") / "out.png")
