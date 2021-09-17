import sys
from pathlib import Path
from os.path import exists
import random

from low_png.image import PngImage
from low_png.chunk import ChunkType
from helper import IHDR

if __name__ == "__main__":
    img = PngImage("in.png")
    chunks = img.chunks()

    increment_done = False

    for chunk in chunks:
        if chunk.type == ChunkType.IHDR.name:
            metadata = IHDR.get_metadata(chunk)
            metadata["color_type"] += 1
            IHDR.set_metadata(chunk, metadata)

    img.save("out.png")
