import sys
from pathlib import Path
from os.path import exists
import random

from low_png.image import PngImage
from low_png.chunk import ChunkType
from helper import IHDR

if __name__ == "__main__":
    filepath: Path = None
    outpath: Path = None

    if len(sys.argv) > 2:
        filepath = Path(sys.argv[1])

        if not exists(filepath):
            raise Exception("Input Image does not exist")
    if len(sys.argv) > 1:
        outpath = Path(sys.argv[2])

        if exists(outpath):
            # raise Warning("Output Image does already exist")
            pass

    if not filepath:
        raise Exception("Please enter path to Input Image")
    if not outpath:
        raise Exception("Please enter path to Output Image")

    img = PngImage(filepath)
    chunks = img.chunks()

    increment_done = False

    for chunk in chunks:
        if chunk.type == ChunkType.IHDR.name:
            metadata = IHDR.get_metadata(chunk)
            metadata["color_type"] += 1
            IHDR.set_metadata(chunk, metadata)

    img.save(outpath)